from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        search_fields = request.GET.getlist('search_fields', None)

        if search_fields:
            return search_fields
        return super().get_search_fields(view, request)
