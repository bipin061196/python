from django.urls import path
from . import views
app_name = "devops"
urlpatterns = [
    path('', views.index, name='index'),
    path('servers/', views.servers, name='servers'),
    path('servers/<int:server_id>', views.server, name='server'),
    path('new_server/', views.new_server, name='new_server'),
    path('new_specification/<int:server_id>/', views.new_specification, name='new_specification'),
    path('edit_specification/<int:specification_id>/', views.edit_specification, name="edit_specification"),
]