from django.views.generic import DetailView, ListView, CreateView

from .forms import NotesForm

from .models import Note

class CreateNoteView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Note
    context_object_name = 'note'

class PopularNotesListView(ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(likes__gte=1)
