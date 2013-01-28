from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import DeleteView

from backoffice.models import Work
from collection.models import Collectable


class CollectView(View):
    def post(self, request, pk, **kwargs):
        work = Work.objects.get(pk=pk)
        Collectable.objects.create(original_work=work, user=request.user)
        return HttpResponse("OK")


class CollectableUpdateView(View):
    def post(self, request, pk):
        obj = Collectable.objects.get(pk=pk, user=request.user)
        obj.comments = request.POST['comments']
        obj.save()
        return HttpResponse("OK")


class CollectableDeleteView(DeleteView):
    model = Collectable
    success_url = reverse_lazy('collection-home')

    def get_object(self):
        obj = super(CollectableDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class UpAction(View):
    def post(self, request, pk):
        Collectable.objects.get(pk=pk).move_up()
        return HttpResponseRedirect(reverse('collection-home'))


class DownAction(View):
    def post(self, request, pk):
        Collectable.objects.get(pk=pk).move_down()
        return HttpResponseRedirect(reverse('collection-home'))
