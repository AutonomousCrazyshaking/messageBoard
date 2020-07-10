from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


# 将jinja2模板设置到项目环境
# 然后将environment函数写到配置文件setting中， 否则jinja2文件所定义的函数无法作用到MyDjango项目里
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    return env
