faat-figpy package
==================

This package enables you to easily read python files as configuration.

Python is an elegant way of expressing configuration.
This package facilitates the reading those files in your script.
Define the symbols you want to keep in UPPER_CASE and all the others are ignored as they are loaded into a settings object.

For example code, the following code defines values for USERNAME, DOMAIN, and LOGPATH.

```python
USERNAME = 'user@example.com'
DOMAIN = 'example.com'
LOG_PATH = '/var/log/my-app/app.log'
```

But because this is python code, not just a simple configuration language, a more advanced deployment could read these settings from elsewhere.

```python
import os
here = os.path.dirname(__file__)

USERNAME = os.environ['user@example.com']
DOMAIN = os.environ['example.com']
LOG_PATH = os.path.join(here, 'log.txt')
```

The configuration can be loaded and used as follows.

```python
import faat.figpy

settings = faat.figpy.load("/path/to/app.conf", requires=["USERNAME", "DOMAIN"])
print(settings.USERNAME)
print(settings["DOMAIN"])
```
