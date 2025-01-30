from django.shortcuts import render
from core.models import Person

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.meilisearch import client
from core.serializer import PersonSearializer


class SearchApiView(APIView):

    def get(self, request):
        query = request.query_params.get('q','')
        results = client.index('persons').search(query, {
            'attributesToRetrieve':['id','name','address'],
            'limit':10
        })
        serializer = PersonSearializer(results['hits'], many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )



def index(request):
    return render(request,'index.html')

# Create your views here.
