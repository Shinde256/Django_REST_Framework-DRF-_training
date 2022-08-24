
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# creating router object
router = DefaultRouter()

#register Studentviewset with Router
router.register('studentapi',views.StudentModelViewsSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='tokenobtainpair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='tokenrefreshpair'),
    path('varifytoken/',TokenVerifyView.as_view(),name='tokenvarify'),
]
