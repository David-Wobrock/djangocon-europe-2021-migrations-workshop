from django.views.generic.edit import CreateView

from .forms import TreeForm
from .models import Tree


class TreeView(CreateView):
    form_class = TreeForm
    template_name = 'trees/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trees'] = Tree.objects.all()
        return context

    def get_success_url(self):
        return self.request.path
