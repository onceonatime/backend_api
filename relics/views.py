from .models import Datas
from django.shortcuts import render
from django.views.generic import ListView
# rest_framework의 클래스 기반 뷰인 APIView
from rest_framework.views import APIView
#
from rest_framework.response import Response

# serializer를 가져오기
from .serializers import DatasSerializer

class DatasList(APIView):
    # List를 읽기 위한 메서드
    def get(self, request, format=None):
        datas = Datas.objects.all()
        serializer = DatasSerializer(datas, many=True)
        return Response(serializer.data)
