#from django.contrib import admin   
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter # type: ignore
from .views import create, list, api_overview, separate_records, unique, total_sessions_duration
#from .views import api_overview            #, students_list, student_detail
#from . import views
#from .views import MyModelListCreate


# Define a router for the SessionDataViewSet
urlpatterns = [
    
    # API Overview
    path('', api_overview, name='api_overview'),
    re_path('add/', create),
    re_path('view/', list),
    re_path('separated/', separate_records ),
    re_path('unique/', unique),
    re_path('total_sessions_duration/', total_sessions_duration),
    #path('api/data/', MyModelListCreate.as_view(), name='my_model-list-create'),
    
]
#hello
#urlpatterns = format_suffix_patterns(urlpatterns)
