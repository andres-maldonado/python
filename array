To Work whit array in views

		this = entry.objects.get(slug = slug) // the curent instance
		array = entry.objects.all().exclude(publish = "no").order_by("publication_date") // array creation
		maxArray = len(array)-1
		for search in array :
			if array[i].id == this.id :
				thisPosition = i
				break
			i+=1
		try :
			after = array[thisPosition-1].id
		except :
			after = array[maxArray].id
		try :
			before = array[thisPosition+1].id
		except :
			before = array[0].id
