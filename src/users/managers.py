from django.db.models import QuerySet
from django.db.models import Q

class UserQuerySet(QuerySet):

    def filter_name(self, name):
       return self.filter(Q(first_name = name) | Q(last_name = name))
