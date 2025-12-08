from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='detail'),
    path('notes/<int:pk>/edit', views.UpdateNoteView.as_view(), name='update'),
    path('notes/<int:pk>/delete', views.DeleteNoteView.as_view(), name='delete'),
    path('notes/popular', views.PopularNotesListView.as_view(),
         name='popular'),
    path('notes/new', views.CreateNoteView.as_view(), name='new'),
    path('notes/<int:pk>/add_like', views.add_like_view, name='add_like'),
    path('notes/<int:pk>/change_visibility', views.change_visibility_view, name='change_visibility')
]
