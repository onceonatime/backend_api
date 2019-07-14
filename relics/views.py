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
# TODO
# 위도 경도로 get할 수 있는 api
# 인자 : 현재 위도, 현재 경도, 범위 값


class CoordinateList(APIView):
    def get(self, request, format=None):
        northWestLatitude = request.GET['northWestLatitude']
        northWestLongitude = request.GET['northWestLongitude']
        southEastLatitude = request.GET['southEastLatitude']
        southEastLongitude = request.GET['southEastLongitude']

        datas = Datas.objects.filter(
            latitude__range=(southEastLatitude, northWestLatitude),
            longitude__range=(southEastLongitude, northWestLongitude))
        
        serializer = DatasSerializer(datas, many=True)
        return Response(serializer.data)

class SiteList(APIView):
    def get(self, request, city, town, fromat=None):
        datas = Datas.objects.filter(ccbaCtcdNm=city).filter(ccsiName=town)
        serializer = DatasSerializer(datas, many=True)
        return Response(serializer.data)


class CityList(APIView):
    def get(self, request, city, fromat=None):
        datas = Datas.objects.filter(ccbaCtcdNm=city)
        serializer = DatasSerializer(datas, many=True)
        return Response(serializer.data)


class TimesList(APIView):
    def get(self, request, times, fromat=None):
        datas = Datas.objects.filter(ccbaPcd1=times)
        serializer = DatasSerializer(datas, many=True)
        return Response(serializer.data)
