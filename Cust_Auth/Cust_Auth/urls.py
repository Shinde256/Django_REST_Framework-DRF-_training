
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

#register Studentviewset with Router
router.register('studentapi',views.StudentModelViewsSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
