# Install :
pip install djangorestframework
settings = 'rest_framework'

#Urls.py
url(r'^endpoint/$', ListAPI.as_view(), name="")

#Views.py :
from rest_framework.views import APIView
from rest_framework.response import Response

#vista basada en clase + define get, porque obtengo un recurso
#el objeto se debe serializar para transportarlo a través de http. Se trabaja serializers.py o se importa
#esta clase no busca PK por tanto se busca lista y se crea objeto
class ListAPI(APIView):
  
  def get(self,request):
    var = Elem.objects.all
    var_json = ElemSerializer(var, many=True)
    return Response(var_json.data)
    
  #CREAR
  def post(self, request):
    var_json = ElemSerializer(data=request.data)
    if var_json.is_valid():
      var_json.save()
      return Response(var_json.data, status=200)
    return Response(var_json.errors, status=400)
    
class DetailAPI(APIView):
  def get_object(self, pk):
    try:
      var = Elem.objects.get(pk=pk)
    except Elem.DoesNotExist:
      raise Http404
      
  def get(self, request, pk):
    var = self.get_object(pk)
    var_json = ElemSerializer(var)
    return Response(var_json.data)
      
  #put es para actualizar un registro
  def put(self, request, pk):
    var = self.get_object(pk)
    var_json = ElemSerializer(var, data=request.data)
    if var_json.is_valid():
      var_json.save()
      return Response(var_json.data)
    return Response(var_json.errors, status=400)

  def delete(self, request, pk):
    var = self.get_object(pk)
    var.delete()
    return Response(status=204)

#serializers.py
from rest_framework import serializers
from .models import Elem

class ElemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Elem
    fields = ('charfield_one','charfield_two') #los input del modelo
