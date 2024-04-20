from .utils import is_medic

def global_context(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        context['is_medic'] = is_medic(user)
    return context