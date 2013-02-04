from django.views.generic.list import ListView

from backoffice.views import DisciplineMixin
from models import Book, BookCategory


class BookListView(DisciplineMixin, ListView):

    def get_queryset(self):
        queryset = Book.objects.filter(discipline=self.discipline)
        try:
            self.category = BookCategory.objects.get(pk=self.args[0])
            queryset = queryset.filter(category=self.category)
        except IndexError:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        try:
            context['category'] = self.category
        except AttributeError:
            pass
        return context
