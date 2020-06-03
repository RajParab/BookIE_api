from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


router=routers.DefaultRouter()
router.register('book',views.BookViewSet,basename='books')
router.register('chapter',views.ChapterViewSet,basename='chapter')

app_name='bookie'
urlpatterns=[
	path('api/',include(router.urls)),
]