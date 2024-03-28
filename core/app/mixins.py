from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

class CustomMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        # Добавление более комплексных свойств (например, проверка на необходимость логина)
        if not request.user.is_authenticated:
            raise Http404("Необходимо выполнить вход")

        return super().dispatch(request, *args, **kwargs)

    # Добавление еще каких-то свойств и методов по вашему усмотрению