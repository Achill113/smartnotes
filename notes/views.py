from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

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

class UpdateNoteView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'

class DeleteNoteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse("notes:detail", args=(pk,)))
    raise Http404
