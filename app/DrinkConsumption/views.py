from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductContainerViewSet(viewsets.ModelViewSet):
    queryset = ProductContainer.objects.all()
    serializer_class = ProductContainerSerializer


@api_view(['POST'])
def tag_scan(request):
    reader = get_object_or_404(Reader, physical_id=request.data['reader_id'])
    tag = get_object_or_404(Tag, uid=request.data['tag_id'])

    product = reader.forTap.onTap
    user = tag.owner
    container = tag.linked_container

    refill = Refill.objects.create(user=user, tag=tag, product=product, container=container).save()

    result = {}
    result['result'] = 'success'
    result['container'] = container.name
    result['user'] = UserSerializer(user).data
    result['product'] = ProductSerializer(product.product).data


    return Response(result)
