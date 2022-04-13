from . import views 
from django.urls import path,include

urlpatterns = [
    path('list/',views.list_todo_items),
    path('list/',views.insert_todo_item)

]