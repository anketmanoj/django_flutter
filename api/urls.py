from django.urls import path
from api.views import *

urlpatterns = [
    path('', getRoutes),
    path('notes/', getNotes, name='notes'),
    path('notes/create/', createNote, name='notes-create'),
    path('notes/update/<str:pk>/', updateNote, name='notes-update'),
    path('notes/delete/<str:pk>/', deleteNote, name='notes-delete'),
    path('notes/<str:pk>/', getNote, name='notes-detail'),
]
