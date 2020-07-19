from django.urls import path
from .import views #.이 붙는건 현재 폴더에서 가져오는거

urlpatterns = [
    path('<int:blog_id>/',views.detail,name = 'detail'),
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    path('<int:blog_id>/delete/',views.delete, name='delete'),
    path('<int:blog_id>/update',views.update, name ='update'),
    path('fake/',views.fake, name = 'fake'),
    path('huhsaeng/',views.huhsaeng,name='huhsaeng')
]