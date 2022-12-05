from django.db.models import Count, Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormMixin



# Create your views here.
from post_module.models import Post, Profession


class PersonListView(ListView):
    template_name = 'post_module/list_of_person.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']

    def get_queryset(self):
        query = super(PersonListView, self).get_queryset()
        profession_name = self.kwargs.get('pro')
        if profession_name is not None:
            query = query.filter(profession__title_url__iexact=profession_name)
        return query


class PersonDetailView(DetailView):
    template_name = 'post_module/detail_of_person.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data()
        loaded_posts = self.object
        context['related_posts'] = Post.objects.filter(profession_id=loaded_posts.profession_id).exclude(
            pk=loaded_posts.id)

        return context


def profession_categories_component(request):
    profession: Profession = Profession.objects.annotate(persons_count=Count('persons')).filter(is_active=True,
                                                                                                persons__gt=0)
    context = {
        'professions': profession
    }
    return render(request, 'post_module/components/profession_categories_component.html', context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'post_module/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
