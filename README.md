# deploycron

A small tool for deploying crontab into your system.

It's useful if you want to deploy some crontab scripts into your system when you deploy your software that contains some extra crontab scripts.

# Install

```bash
pip install deploycron
```

# Usage

There's only one function in the package now,

```python
def deploycron(filename="", content="", override=False):
```

> Install crontabs into the system if it's not installed.
> This will not remove the other crontabs installed in the system if not specified
> as override. It just merge the new one with the existing one.  
> If you provide `filename`, then will install the crontabs in that file
> otherwise install crontabs specified in content
> 
> `filename` - file contains crontab, one crontab for a line
> `content`  - string that contains crontab, one crontab for a line
> `override` - override the origin crontab

Example: 

```python
from deploycron import deploycron

# specify a filenmae
deploycron(filename="/tmp/youcrontab.tab")

# or just specify crontab content
deploycron(content="* * * * * echo hello > /tmp/hello")

# if you want to overwrite the existing crontab, set `override` to True
deploycron(content="* * * * * echo hello > /tmp/hello", override=True)
```

## Note

Only support in unix-like system, eg. Linux/Mac

## Author

* Monklof (monklof@gmail.com)

## License

MIT
