#OBJECT CREATION

#Object + individual property all VAR like LOCAL VAR

#definition Class external
	class Object(object):
		pass
	
	def lcl(request):
		lcl = Object()
		lcl.service = "Services"
		lcl.blog = "Blog"
		lcl.price = "Prix"
		lcl.portfolio = "Portfolio"
		lcl.contact = "Contact"

#Object like dict : all VAR are String not local VAR
	lcl = {
		"service" : "Services YEAH",
		"blog" : "ISOD",
		"price" : "DF",
		"portfolio" : "iqsud",
		"contact" : "isqod",
	}
