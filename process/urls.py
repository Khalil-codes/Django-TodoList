from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.addTask, name="add"),
    path("complete/<int:pk>", views.completeTask, name='complete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
    path('deleteCompleted/', views.deleteCompleted, name='deleteCompleted'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)