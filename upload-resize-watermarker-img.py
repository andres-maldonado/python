# En una clase de MODEL

from PIL import Image
import sys, time
class Photo(models.Model):
	escort_profile = models.ForeignKey(EscortProfile,on_delete=models.CASCADE)
	photo_original = models.FileField(upload_to=upload_file)
	photo_big = models.CharField(max_length=255, blank=True)
	photo_thumb = models.CharField(max_length=255, blank=True)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.escort_profile.alias+' - '+str(self.pk)

	def save(self):
		from config.settings import WATERMARK_PATH
		import uuid
		my_uuid = str(uuid.uuid4())
		# Se guarda la original
		super(Photo, self).save()

		# Se declaran las variables de tamaños
		sizes = {'small': {'height': 750, 'width': 400},'big': {'height': 900, 'width': 1400},}
		big_img_name = str(my_uuid) + "_" + str(sizes['big']['width']) + "x" + str(sizes['big']['height']) + ".jpg"
		small_img_name = str(my_uuid) + "_" + str(sizes['small']['width']) + "x" + str(sizes['small']['height']) + ".jpg"

		photopath = str(self.photo_original.path)  # El path de la original
		extension = photopath.rsplit('.', 1)[1]  # extensión del archivo
		filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # nombre del archivo
		fullpath = photopath.rsplit('/', 1)[0]  # el path

		# si no es archivo válido, se corta
		if extension not in ['jpg', 'jpeg', 'gif', 'png']: sys.exit()

		# Nombre aleatorio
		watermark = Image.open(WATERMARK_PATH)
		big_img = Image.open(photopath)

		big_img.thumbnail((sizes['big']['width'], sizes['big']['height']), Image.ANTIALIAS)

		watermarkWidth, watermarkHeight = watermark.size
		width, height = big_img.size

		big_img.paste(watermark, (width - watermarkWidth, height - watermarkHeight), watermark)
		big_img.save(fullpath + '/' + big_img_name)
		self.photo_big = big_img

		# Creación imagen chica
		small_img = Image.open(photopath)
		small_img.thumbnail((sizes['small']['width'], sizes['small']['height']), Image.ANTIALIAS)
		small_img.save(fullpath + '/' + small_img_name)
		self.photo_thumb = small_img_name

		super(Photo, self).save()

	class Meta:
		ordering = ['-pk']
