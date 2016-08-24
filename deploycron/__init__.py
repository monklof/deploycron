# coding: utf-8

import subprocess
import os

def deploycron(filename="", content="", override=False):
    """install crontabs into the system if it's not installed.
    This will not remove the other crontabs installed in the system if not specified
    as override. It just merge the new one with the existing one. 
    If you provide `filename`, then will install the crontabs in that file
    otherwise install crontabs specified in content

    filename - file contains crontab, one crontab for a line
    content  - string that contains crontab, one crontab for a line
    override - override the origin crontab
    """
    if not filename and not content:
        raise ValueError("neither filename or crontab must be specified")

    if filename:
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except Exception as e:
            raise ValueError("cannot open the file: %s" % str(e))
    if override:
        installed_content = ""
    else:
        # currently installed crontabs
        retcode, err, installed_content = _runcmd("crontab -l")
        if retcode != 0 and 'no crontab for' not in err:
            raise OSError("crontab not supported in your system")
        # merge the new crontab with the old one
        installed_content = installed_content.rstrip("\n")
    installed_crontabs = installed_content.split("\n")
    for crontab in content.split("\n"):
        if crontab and crontab not in installed_crontabs:
            if not installed_content:
                installed_content += crontab
            else:
                installed_content += "\n%s" % crontab
    if installed_content:
        installed_content += "\n"
    # install back
    retcode, err, out = _runcmd("crontab", installed_content)
    if retcode != 0:
        raise ValueError("failed to install crontab, check if crontab is valid")

def _runcmd(cmd, input=None):
    '''run shell command and return the a tuple of the cmd's return code, std error and std out
    WARN: DO NOT RUN COMMANDS THAT NEED TO INTERACT WITH STDIN WITHOUT SPECIFY INPUT,
         (eg cat), IT WILL NEVER TERMINATE.
    '''

    if input is not None:
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             close_fds=True, preexec_fn=os.setsid)
    else:
        p = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             close_fds=True, preexec_fn=os.setsid)

    stdoutdata, stderrdata = p.communicate(input)
    return p.returncode, stderrdata, stdoutdata


