from django.contrib import admin
from django.urls import path

import liker.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', liker.views.index),
    path('get_user_<int:user_id>/', liker.views.get_like),
    path('user_<int:user_id>/', liker.views.user_page),
    path('like_<int:user_id>/', liker.views.like),
]
