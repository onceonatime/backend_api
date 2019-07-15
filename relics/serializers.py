from rest_framework import serializers

# from .models import Datas
from .models import Datas


class ImageSerializer(serializers.Serializer):
    imageUrl = serializers.CharField()
    ccimDesc = serializers.CharField()


class DetailSerializer(serializers.Serializer):
    ccbaMnm1 = serializers.CharField()
    ccbaLcad = serializers.CharField()
    content = serializers.CharField()

class DatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datas
        fields = ('ccbaKdcd', 'ccbaAsno', 'ccbaCtcd', 'ccbaPcd1', 'ccbaMnm1', 'ccbaMnm2',
                  'ccmaName', 'ccbaCtcdNm', 'ccsiName', 'longitude', 'latitude', 'content')
