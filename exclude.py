#Multiple exclude
from django.db.models import Q

objects.exclude(Q(year=2018) & Q(month=5)) #exclude X AND Y
objects.exclude(Q(year=2018) | Q(month=5)) #exclude X OR Y
