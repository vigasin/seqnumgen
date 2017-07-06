from rest_framework.response import Response
from rest_framework.views import APIView

from seqnum.models import Tag
from seqnum.serializers import TagSerializer


class TagView(APIView):
    def post(self, request, name, format=None):
        tag, _ = Tag.objects.get_or_create(name=name)
        tag.num += 1
        tag.save()

        serializer = TagSerializer(tag)
        return Response(serializer.data)
