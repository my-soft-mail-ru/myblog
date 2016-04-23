# ~*~ coding: utf-8 ~*~

# импортируем админку
from django.contrib import admin

# Makes the patterns() function available
from django.conf.urls.defaults import *

# импортируем нашу вьюху (см. ниже описание файла вьюхи)
from myproject.blog.views import main_page, get_post

# Above we used admin.autodiscover() to automatically load the INSTALLED_APPS admin.py modules
admin.autodiscover()

urlpatterns = patterns('',
    # Если ничего не введено, то отдаем управление mainpage вьюхе
    (r'^$', main_page),
    # Если передан id поста, то отдаем управление get_post вьюхе
    (r'^post/([0-9]{1,5})', get_post),
    # Если введен /admin/, то идем в админку
    (r'^admin/', include(admin.site.urls)),
)