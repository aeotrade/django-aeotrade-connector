# Overview

Django Aeotrade Connector is a framework that allows you to easily create your `connector`
with [Aeotrade OS](https://www.aeotrade.com/portal).

Latest version: [0.1.0rc2](https://pypi.org/project/django-aeotrade-connector/)

# Quickstart

## Install

```bash
pip install django-aeotrade-connector
```
After installing the package, you should add `aeotrade_connector` to django's `INSTALLED_APPS`

## Usage

### Initialize connector in django project
Before you initialize your connector. You must set `AC_MANAGEMENT_ENDPOINT` in django.settings.py, which is the endpoint
of aeotrade connector management api.

```bash
python manage.py initconnector
```

This will create `urls.py` and `dispatcher.py` to your project

### Create connector app

```bash
python manage.py startconnector <my_connector>
```

After executing this command, you should add `my_connector` to `INSTALLED_APPS` also. Then you will see a new django app named
`my_connector` in your django project.
In this app, you can see `services.py` and `task.py` python files. In `services.py`, you must implement some connector methods,
which are inherited from `ConnectorServices`. and in `task.py`, you can define your connector tasks. those tasks will be
registered when django setup.

### Configuration

In `app.py`:

Before you start to run your connector, you must configure your connector in the `app.py` file. The configuration file
is located in the `my_connector/app.py` file.

```Python
class MyConnectorConfig(AppConfig):
    name = 'my_connector'

    class Config:
        # required config
        connector = True
        connector_config_model = ConnectorBaseConfig(
            # required config
            label="my_first_connector",
            code="my_first_connector_code",
            mq_recv_model=MQManagerConfig(
                url="amqp://root:123456@localhost:5672/",
                exchange="test",
                queue="q_receive",
                pot=POT.Thread
            ),
            # optional config
            event_up_chain = True,
            files_up_chain = False,
            callback = some_function_name,
            callback_args = ['arg1', 'arg2'],
            callback_kwargs = {'key1': 'value1', 'key2': 'value2'},
            task_stop_when_error = False,
            auto_heartbeat = True,
            kw = {"extra_key": "extra_value"},
        )


```

In django.settings.py:

```Python
INSTALLED_APPS = [
    ...,
    'aeotrade_connector'
    'my_connector',
]

AC_MANAGEMENT_ENDPOINT = 'http://www.example.com:8000'

IS_TEST = False  # or True

# Redis is used to implement a distributed lock, ensuring that the scheduled task
# is executed only once even when multiple workers are started.
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://localhost:6379/0',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}
```

NOTICE：

This software is licensed under the GNU Lesser General Public License (LGPL) version 3.0 or later. However, it is not permitted to use this software for commercial purposes without explicit permission from the copyright holder.
If the above restrictions are violated, all commercial profits generated during unauthorized commercial use shall belong to the copyright holder. 
The copyright holder reserves the right to pursue legal liability against infringers through legal means, including but not limited to demanding the cessation of infringement and compensation for losses suffered as a result of infringement.
本软件根据GNU较宽松通用公共许可证（LGPL）3.0或更高版本获得许可。但是，未经版权所有者明确许可，不得将本软件用于商业目的。
若违反上述限制，在未经授权的商业化使用过程中所产生的一切商业收益，均归版权所有者。
版权所有者保留通过法律途径追究侵权者法律责任的权利，包括但不限于要求停止侵权行为、赔偿因侵权行为所遭受的损失等。
