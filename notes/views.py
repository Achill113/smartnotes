from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Note

class CreateNoteView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = "notes/note_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

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

def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse("notes:detail", args=(pk,)))
    raise Http404
