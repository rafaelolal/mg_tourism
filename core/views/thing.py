from typing import Dict, List

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from core.models import Thing, Picture

class ThingDetailView(DetailView):
    # returns model name in lowercase
    # better to change it yourself:
    context_object_name = "thing_detail"
    model = Thing
    template_name = 'core/thing/detail.html'

class ThingDeleteView(DeleteView):
    model = Thing
    success_url = reverse_lazy("core:thing_list")
    template_name = 'core/thing/confirm_delete.html'

class ThingUpdateView(UpdateView):
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe']
    model = Thing
    template_name = 'core/thing/form.html'

class ThingListView(ListView):
    model = Thing
    template_name = 'core/thing/list.html'

    # manually changing data that is sent to the django template
    def get_context_data(self, **kwargs):
        # categories is used to create the switches
        return super().get_context_data(**kwargs,
        categories=self.model.categories)

    def get_queryset(self):
        """Returns the things to be displayed as thing_list
        First gets the categories in the querystrig of the URL
        Filters the query given the categories
        Then gets other filters in the URL
        Filters the query given the other filters
        """
        query_categories = self.get_query_categories()
        category_filtered = self.query_filter_categories(query_categories)
        query_fields = self.get_query_fields()
        return self.query_filter_fields(query_fields, category_filtered)

    def get_query_categories(self) -> List[str]:
        """Returns a list of all categories in the querystring of the URL"""
        query_categories = []
        for category in self.model.categories:
            query_categories.append(self.convert_on(self.request.GET.get(category)))

        return query_categories

    def get_query_fields(self) -> Dict[str, str]:
        """Returns a dictionary with the name of the parameters and their values in the querystring of the URL"""
        query_fields = {}
        querystring = self.request.GET
        for query in querystring:
            if query not in self.model.categories and (querystring[query] and querystring[query] != 'Any'):
                query_fields[query] = querystring[query]

        return query_fields

    @staticmethod
    def convert_on(category):
        """If a switch is set to on, converts that to checked
        Used to remember the state of a switch after submitting the filter form
        """
        if category == 'on':
            return 'checked'
        return ''

    def query_filter_categories(self, query_categories: List[str]):
        """Tries to filter the queryset by category
        If there are no categories to filter, returns all Thing objects"""
        queryset = []
        for category, param in zip(self.model.categories, query_categories):
            if param:
                queryset.append(Thing.objects.filter(category=category))

        if queryset:
            return self.combine(queryset)

        else:
            return Thing.objects.all()

    def query_filter_fields(self, query_fields: Dict[str, str], things):
        """Returns a queryset of all objects that satisfy the querystring parameters in the URL"""

        if 'min_stars' in query_fields:
            things = things.filter(stars__gte=round(float(query_fields['min_stars']), 1))

        # tours is the only category with different fields
        tours = things.filter(category="Tour")
        others = things.filter(category__in=['Attraction', 'Food', 'Outdoor', 'Shopping'])

        # following code looks horrible, but muist be done this way since each category has unique fields
        for field in query_fields:
            if field in 'type max_price max_duration':
                if field == 'type':
                    tours = tours.filter(tour__type=query_fields[field].replace('_', ' '))
            
                elif field == 'max_price':
                    tours = tours.filter(tour__price__lte=round(float(query_fields[field]), 2))
            
                elif field == 'max_duration':
                    # duration is stored in seconds, converting to hours
                    tours = tours.filter(tour__duration__lte=int(query_fields[field])*3600)
            
            if field in 'type neighborhood good_for':
                field_value = query_fields[field]
                if field == 'good_for':
                    field_value = query_fields[field].replace('_', ' ')
                    others = (others.filter(attraction__good_for=field_value)
                        | others.filter(food__good_for=field_value)
                        | others.filter(outdoor__good_for=field_value)
                        | others.filter(shopping__good_for=field_value))

                if field == 'type':
                    field_value = query_fields[field].replace('_', ' ')
                    others = (others.filter(attraction__type=field_value)
                        | others.filter(food__type=field_value)
                        | others.filter(outdoor__type=field_value)
                        | others.filter(shopping__type=field_value))

                elif field == 'neighborhood':
                    others = (others.filter(attraction__neighborhood=query_fields[field])
                        | others.filter(food__neighborhood=query_fields[field])
                        | others.filter(outdoor__neighborhood=query_fields[field])
                        | others.filter(shopping__neighborhood=query_fields[field]))

        return tours | others

    @staticmethod
    def combine(queryset: List):
        """Used to combine querysets in a list of querysets"""
        final_queryset = queryset[0]
        for query in queryset[1:]:
            final_queryset = final_queryset | query

        return final_queryset

class PictureCreateView(CreateView):
    fields = ['image']
    model = Picture

    def form_valid(self, form):
        t = self.request.GET['thing']
        thing = Thing.objects.get(id=t)
        form.instance.thing = thing
        return super().form_valid(form)