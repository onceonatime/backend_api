import xml.etree.ElementTree as ET
import urllib.request
from .models import Datas
import json

url = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do?pageUnit=2&pageIndex=1&ccbaPcd1=09"
# from relics.makes import detail_get


class DetailProxy():
    def get_image(*args, **kwargs):
        URL = "http://www.cha.go.kr/cha/SearchImageOpenapi.do?"
        PARAMS = ""
        for key, val in kwargs.items():
            PARAMS = PARAMS + key + "=" + val[0] + "&"

        URL = URL + PARAMS
        print(URL)
        targetXML = urllib.request.urlopen(URL).read().decode('utf-8')
        root = ET.fromstring(targetXML)
        # print(root.find('totalCnt').text)
        # item_length = int(root.find('totalCnt').text)
        item = root.find('item')
        ccimDesc = item.findall('ccimDesc')
        imageUrl = item.findall('imageUrl')
        item_list = []
        for item in range(len(imageUrl)):
            item_dict = {
                'imageUrl': imageUrl[item].text,
                'ccimDesc': ccimDesc[item].text
            }
            item_list.append(item_dict)
        return item_list

    def get_detail(*args, **kwargs):
        URL = "http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?"
        PARAMS = ""
        for key, val in kwargs.items():
            PARAMS = PARAMS + key + "=" + val[0] + "&"

        URL = URL + PARAMS
        print(URL)
        result = urllib.request.urlopen(URL)
        print(result)
        targetXML = result.read().decode('utf-8')
        root = ET.fromstring(targetXML)
        item = root.find('./item')
        item_dict = {
            'ccbaMnm1': item.find('./ccbaMnm1').text,
            'ccbaLcad': item.find('./ccbaLcad').text.strip(),
            'content': item.find('./content').text,
        }
        return item_dict


def listGet(unit, index, times):
    URL = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do"
    URL = URL + '?pageUnit=' + \
        str(unit) + '&pageIndex='+str(index)+'&ccbaPcda1=' + times
    targetXML = urllib.request.urlopen(URL).read().decode('utf-8')

    root = ET.fromstring(targetXML)

    for child in root.iter("item"):
        i = 0
        a = list()
        for cchild in child:
            a.insert(i, cchild.text)
            i = i+1

        # print(a)
        data = Datas.objects.create(
            ccbaKdcd=a[9],  # int,지정종목(종목코드)
            ccbaAsno=a[11],  # int,지정번호
            ccbaCtcd=a[10],  # int,시도코드
            ccbaPcd1=times,  # int,시대
            ccbaMnm1=a[4],  # String,문화재명
            ccbaMnm2=a[5],  # string,문화재명2
            ccmaName=a[2],  # string,문화재유형
            ccbaCtcdNm=a[6],  # string,시도명
            ccsiName=a[7],  # string,시군구명
            longitude=a[14],
            latitude=a[15]
            # ccbaLcad =          #string,주소 상세
            # content =           #string,내용
        )


def for_list():
    times = [
        {'code': '01', 'length': 42},
        {'code': '03', 'length': 15},
        {'code': '05', 'length': 77},
        {'code': '07', 'length': 19},
        {'code': '09', 'length': 9},
        {'code': '10', 'length': 219},
        {'code': '11', 'length': 8},
        {'code': '12', 'length': 181, },
        {'code': '13', 'length': 150, },
        {'code': '20', 'length': 460, },
        {'code': '30', 'length': 1129, },
        {'code': '40', 'length': 5172, },
        {'code': '45', 'length': 204, },
        {'code': '50', 'length': 651, },
    ]

    for time in times:
        listGet(time['length'], 1, time['code'])


def detail_get():
    all_datas = Datas.objects.all()

    for one in all_datas:
        ccbaKdcd2 = str(one.ccbaKdcd)
        ccbaAsno2 = str(one.ccbaAsno)
        ccbaCtcd2 = str(one.ccbaCtcd)

        url = "http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?ccbaKdcd=" + \
            ccbaKdcd2+"&ccbaAsno="+ccbaAsno2+"&ccbaCtcd="+ccbaCtcd2
        result = urllib.request.urlopen(url)

        if(result.headers.get_content_type() == 'text/html'):
            print(one)
            print(result.headers.get_content_type())
            continue

        targetXML = result.read().decode('utf-8')
        root = ET.fromstring(targetXML)

        for child in root.iter("item"):
            i = 0
            a = list()
            for cchild in child:
                a.insert(i, cchild.text)
                i = i+1
            Datas.objects.filter(ccbaKdcd=ccbaKdcd2, ccbaAsno=ccbaAsno2, ccbaCtcd=ccbaCtcd2).update(
                ccbaLcad=a[12],  # string,주소 상세
                content=a[19]  # string,내용
            )
