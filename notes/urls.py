from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='detail'),
    path('notes/popular', views.PopularNotesListView.as_view(),
         name='popular'),
    path('notes/new', views.CreateNoteView.as_view(), name='new'),
]
