from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name="home"),
    path('add_stu/', views.add_stu , name="add_stu"),
    path('delete_std/<int:roll>',views.delete_std),
    path('update_std/<int:roll>',views.update_std),
    path('stud/do-update_std/<int:roll>',views.do_update_std , name="do-update_std")
]
    
    

