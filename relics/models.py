from django.db import models

# Create your models here.
class ByTime(models.Model):
    period =models.IntegerField(default=0)
    year =models.IntegerField(default=0)
    name =models.CharField(max_length=50)
    incidents =models.CharField(max_length=200,default='-')
    clickable =models.BooleanField( null=True)


class Datas(models.Model):
    ccbaKdcd = models.IntegerField(default=0)  # int,지정종목(종목코드)
    ccbaAsno = models.CharField(
        max_length=20, null=True, blank=True)  # int,지정번호
    ccbaCtcd = models.CharField(max_length=3, default=0)  # int,시도코드
    ccbaPcd1 = models.CharField(max_length=3, default=0)  # int,시대
    ccbaMnm1 = models.CharField(
        max_length=20, null=True, blank=True)  # String,문화재명
    ccbaMnm2 = models.CharField(
        max_length=20, null=True, blank=True)  # string,문화재명2
    ccmaName = models.CharField(
        max_length=20, null=True, blank=True)  # string,문화재유형
    ccbaCtcdNm = models.CharField(
        max_length=20, null=True, blank=True)  # string,시도명
    ccsiName = models.CharField(
        max_length=20, null=True, blank=True)  # string,시군구명
    longitude = models.FloatField(null=True)  # 위도
    latitude = models.FloatField(null=True)  # 경도
    ccbaLcad = models.TextField(null=True)  # string,주소 상세
    content = models.TextField(null=True)  # string,내용
