from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework import response, schemas
# from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

# @api_view()
# @renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
# def schema_view(request):
#     generator = schemas.SchemaGenerator(title='Accubets API')
#     return response.Response(generator.get_schema(request=request))