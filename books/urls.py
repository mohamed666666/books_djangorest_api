from django.urls import path
from . import views


app_name="books"

urlpatterns = [
     path('books/', views.snippet_list),
     path('pages/',views.pages)
]
