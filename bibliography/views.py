from django.views.generic.list import ListView
from backoffice.views import DisciplineMixin
from models import Book, BookCategory
from django.shortcuts import get_object_or_404


class BookListView(DisciplineMixin, ListView):
    paginate_by = 20

    def get_queryset(self):
        queryset = Book.objects.filter(discipline=self.discipline)
        try:
            self.category = get_object_or_404(BookCategory, pk=self.args[0])
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
        category_ids = Book.objects.filter(discipline=self.discipline).values_list('category', flat=True).distinct()
        context['categories'] = BookCategory.objects.filter(pk__in=category_ids)
        return context
