def view(request):
  queryset = this.objects.exclude(publish='no').order_by("-publication_date")
  page = request.GET.get('page', 1)
	paginator = Paginator(queryset, 1)
	try:
		article = paginator.page(page)
	except PageNotAnInteger:
		article = paginator.page(1) # If page is not an integer, deliver first page. / SQL INJECTION
	except EmptyPage:
		article = paginator.page(paginator.num_pages) # If page is out of range, deliver last page of results.
	index = article.number
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 2 if index <= max_index else 0
	if index <= 2 :
		end_index = 5
	elif max_index - 2 <= index :
		start_index = -5
	page_range = paginator.page_range[start_index:end_index] # New page range
	return render(request, 'blog_view.html', {'article': article,'page_range': page_range,})
