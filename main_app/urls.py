# urls.py
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from . import views

router = DefaultRouter()  # can keep default here

student_list = StudentViewSet.as_view({'get': 'list', 'post': 'create'})
student_detail = StudentViewSet.as_view({
    'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
})
bulk_view = StudentViewSet.as_view({'post': 'bulk_create'})

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),  # keep your router if you want other endpoints
    re_path(r'^students/?$', student_list, name='student-list'),
    re_path(r'^students/(?P<pk>\d+)/?$', student_detail, name='student-detail'),
    re_path(r'^students/bulk-create/?$', bulk_view, name='student-bulk-create'),

]