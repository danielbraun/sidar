from backoffice.models import Discipline


def default(request):
    return {'disciplines': Discipline.objects.all()}
