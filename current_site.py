from django.contrib.sites.shortcuts import get_current_site


def lcl(request):

#NO IN VIEWS
  var = get_current_site(request)

#IN VIEWS  
  var = request.get_host()
