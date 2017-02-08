from django.http.response import JsonResponse


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 例句.models import 例句表
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音


def 看(request):
    try:
        漢字 = request.GET['漢字']
        臺羅 = request.GET['臺羅']
    except:
        漢字 = '美'
        臺羅 = 'bi2'
    句物件 = (
        拆文分析器
        .對齊句物件(漢字, 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
        .轉音(臺灣閩南語羅馬字拼音)
    )
    結果 = []
    for 例句 in 例句表.objects.filter(分詞__contains=句物件.看分詞()).values():
        例句['綜合標音'] = 拆文分析器.分詞句物件(例句['分詞']).綜合標音(閩南語綜合標音)
        結果.append(例句)
    return JsonResponse({'例句': 結果})
