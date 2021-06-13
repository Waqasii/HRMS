from django.conf.urls import url
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index,name='index'),
    path('addView/',addView,name='addView'),
    path('storeEmployee/',storeEmployee,name='storeEmployee'),
    path('delete/<str:cnic>',Delete,name='delete'),
    path('showUpdate/<str:cnic>',showUpdate,name='showUpdate'),
    path('update/<str:cnic>',update,name='update'),
    path('open/<str:cnic>',open,name='open'),
]


if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)