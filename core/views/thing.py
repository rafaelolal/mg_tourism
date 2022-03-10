"""Views associated with Thing objects"""

from datetime import timedelta
from re import search

from typing import Any, Dict, List
from django.db.models.query import QuerySet
from django.db.models import Q

from django.core.exceptions import FieldError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from core.models import Thing, Picture, Tour, Attraction, Food, Shopping, Outdoor
from core.mixins import IsSuperuserMixin

class ThingDetailView(DetailView):
    """View to see the details of a Thing object"""

    context_object_name = "thing_detail"
    model = Thing
    template_name = 'core/thing/detail.html'

class ThingDeleteView(IsSuperuserMixin, DeleteView):
    """View to delete a Thing object"""

    login_url = 'core:user_login'
    model = Thing
    success_url = reverse_lazy("core:thing_list")
    template_name = 'core/thing/confirm_delete.html'

class ThingUpdateView(IsSuperuserMixin, UpdateView):
    """View to update a Thing object"""

    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe']
    model = Thing
    template_name = 'core/thing/form.html'

class ThingListView(ListView):
    """View to see the list of all Thing objects"""

    model = Thing
    template_name = 'core/thing/list.html'

    def get(self, request: HttpResponse,
        *args: (Any),
        **kwargs: Dict[str, Any]) -> HttpResponse:
        
        """Gets the link to the appropriate view
        Redirects user to the ThingListView or if there is
        only one Thing object in the QuerySet object,
        redirects to that Thing's DetailView
        Saves the user time
        """
        
        queryset = self.get_queryset()
        if queryset and len(queryset) == 1:
            messages.warning(request,
                'This is the only thing that matches your search.')
            
            return HttpResponseRedirect(reverse('core:thing_detail',
                kwargs={'pk': queryset.first().pk}))

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Dict[str, Any]):
        """Determines the variables accessible within the template for this view"""

        return super().get_context_data(**kwargs,
            categories=self.model.categories)

    def get_queryset(self) -> QuerySet:
        """Gets all the Thing objects to be displayed
        Returns only the Thing objects that fit
        the filters in the request's querystring
        """

        query_fields = self.get_query_fields()
        query_categories = self.get_query_categories()
        queryset = self.get_filtered_query(query_fields, query_categories)
        return queryset

    def get_query_categories(self) -> List[str]:
        """Returns a list of all categories in the querystring of the URL"""
        
        query_categories = []
        for category in self.model.categories:
            checked = self.request.GET.get(category)
            if checked:
                query_categories.append(category)

        if not query_categories:
            return self.model.categories

        return query_categories

    def get_query_fields(self) -> Dict[str, str]:
        """Returns a dictionary with the name of the parameters
        and their values in the querystring of the URL, except categories
        """
        
        query_fields = {}
        querystring = self.request.GET
        for query in querystring:
            if query not in self.model.categories and (querystring[query] and querystring[query] != 'Any'):
                query_fields[query] = querystring[query]

        return query_fields

    def get_filtered_query(self, query_fields: Dict[str, str], query_categories: Dict[str, str]) -> QuerySet:
        """Returns a QuerySet object of all objects that satisfy the querystring parameters in the URL"""

        search_filters = self.get_search_filters(query_fields, query_categories)
        cat_independent_filters = self.get_cat_independent_filters(query_fields)   
        cat_dependent_filters = self.get_cat_dependent_filters(query_fields, query_categories)

        ###########################

        search_querysets = []
        or_filters = list(search_filters.items())
        if search_filters:
            for i, f in enumerate(or_filters):
                try:
                    search_querysets.append(self.model.objects.all().filter(**dict(or_filters[i:i+1])))

                except FieldError:
                    pass
            
<<<<<<< HEAD
            things = self.combine(search_querysets)
=======
            things = self.combine(search_query_sets)
>>>>>>> 54508465363652288aeec1db3b25e5191e826e5b

        else:
            things = self.model.objects.all()

        things = things.filter(**cat_independent_filters)

        ###########################

        querysets = []
        for category in query_categories:
            apply_on = things.filter(category=category)

            apply_now = {}
            for f in cat_dependent_filters:
                if category.lower() in f:
                    apply_now[f] = cat_dependent_filters[f]

            if apply_now:
                querysets.append(apply_on.filter(**apply_now))

            else:
                querysets.append(apply_on)

        if querysets:
            return self.combine(querysets)

        else:
            return things

    @staticmethod
    def get_search_filters(query_fields, query_categories):
        search_filters = {}

        if 'search' in query_fields:
            search_filters[f'name__contains'] = query_fields['search']
            search_filters[f'address__contains'] = query_fields['search']
            search_filters[f'category__contains'] = query_fields['search']
            search_filters[f'short_description__contains'] = query_fields['search']

            for category in query_categories:
                for field, field_type in [(field.name, field.get_internal_type()) for field in eval(f'{category}._meta.fields')]:
                    if field != 'long_description':
                        search_filters[f'{category.lower()}__{field}__contains'] = query_fields['search']                  
                
            del query_fields['search']

        return search_filters

    @staticmethod
    def get_cat_independent_filters(query_fields: Dict[str, str]) -> Dict[str, Any]:
        """Returns a dictionary of all the filters in the querystring
        of the URL that are independent of a Thing's category
        """
        
        cat_independent_filters = {}
        if 'covid_safe' in query_fields:
            cat_independent_filters[f'covid_safe'] = True if query_fields['covid_safe'] == 'on' else False
            del query_fields['covid_safe']
        
        if 'stars' in query_fields:
            cat_independent_filters[f'stars__gte'] = float(query_fields['stars'])
            del query_fields['stars']

        return cat_independent_filters

    @staticmethod
    def get_cat_dependent_filters(query_fields: Dict[str, str],
        query_categories: List[str]) -> Dict[str, Any]:
        
        """Returns a dictionary of all the filters in the querystring
        of the URL that depend on a Thing's category
        """

        cat_dependent_filters = {}
        for category in query_categories:
            for field in query_fields:
                # values in query_fields are strings, but in db are respesctive data types
                # must filter differently depending on the field
                if field in [field.name for field in eval(f'{category}._meta.fields')]:
                    if field == 'price':
                        cat_dependent_filters[f'{category.lower()}__price__lte'] = float(query_fields[field])
                    
                    elif field == 'duration':
                        cat_dependent_filters[f'{category.lower()}__duration__lte'] = timedelta(hours=float(query_fields[field]))                    
                    
                    else:
                        cat_dependent_filters[f'{category.lower()}__{field}'] = query_fields[field].replace('_', ' ')                  

        return cat_dependent_filters

    @staticmethod
    def combine(queryset: List) -> QuerySet:
        """Used to combine QuerySet objects in a list of QuerySet objects"""

        final_queryset = queryset[0]
        for query in queryset[1:]:
            final_queryset |= query

        return final_queryset