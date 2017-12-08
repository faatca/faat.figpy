faat-figpy package
==================

This package enables you to easily read python files as configuration.

Python is an elegant way of expressing configuration. This package facilitates
the reading those files in your script. Define the symbols you want to keep in
UPPER_CASE and all the others are ignored as they are loaded into a settings
object.

For example code, the following code defines values for USERNAME, DOMAIN, and
LOGPATH.

.. code: python

    import os
    here = os.path.dirname(__file__)

    USERNAME = 'user@example.com'
    DOMAIN = 'example.com'
    LOG_PATH = os.path.join(here, 'log.txt')
