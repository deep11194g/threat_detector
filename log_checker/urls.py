from django.conf.urls import url
from src.LogUpload import LogUpload
from . import views

urlpatterns = [
    url(r'^read_logs/', LogUpload.as_view(), name = 'log_file_uploader'),
]
