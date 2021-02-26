from rest_framework.response import Response
from rest_framework import status, generics
from .models import MovieDetail
from .serializers import MovieSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class movie_detail(generics.ListCreateAPIView):
    queryset = MovieDetail.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'description']

    def post(self, request, *args, **kwargs):
        saveserialize = MovieSerializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=201)
        print(saveserialize.is_valid())
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)
