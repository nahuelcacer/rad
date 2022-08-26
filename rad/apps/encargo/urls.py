from django.urls import re_path,path
from . import views
app_name = 'apps.encargo'

urlpatterns = [
    path('addEncargo/', views.addEncargo.as_view(), name="addEncargo")

]