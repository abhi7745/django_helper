from django.urls import path

from .views import *

urlpatterns = [
    path('advocatesclass/<str:username>/', AdvocatesDetail.as_view(), name='advocate_detail_class'),
]