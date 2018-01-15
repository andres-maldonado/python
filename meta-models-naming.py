	class Meta:
		# db_table = 'the_table_name'
		verbose_name = 'Vendedor'
		verbose_name_plural = 'Vendedores'
	def __str__(self):
		return self.name +', '+ self.rut
