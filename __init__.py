"""
@company: 慧贸天下(北京)科技有限公司
@author: wanghao@aeotrade.com
@time: 2024/12/5 17:22
@file: __init__.py
@project: django_aeotrade_connector
@describe: None
"""

__title__ = 'Django Aeotrade Connector'
__version__ = '0.1.0-rc1'

VERSION = __version__

# Require Django
try:
    import django
except ImportError:
    raise ImportError("django_aeotrade_connector requires Django to be installed.")

if django.VERSION < (3, 0):
    raise RuntimeError("django_aeotrade_connector requires Django 3.0 or higher.")

try:
    import rest_framework  # noqa: F401
except ImportError:
    raise ImportError("django_aeotrade_connector requires djangorestframework to be installed.")

# Require apscheduler
try:
    import apscheduler  # noqa: F401
except ImportError:
    raise ImportError("django_aeotrade_connector requires apscheduler to be installed.")
