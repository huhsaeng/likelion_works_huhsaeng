
from django.contrib import admin
from django.urls import path, include
import blog.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.blog, name = "blog"),

    path('blog/', include('blog.urls')),
    
    ]
