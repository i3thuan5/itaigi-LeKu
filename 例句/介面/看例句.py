from django.http.response import JsonResponse


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 例句.models import 例句表
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


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
    例句 = 例句表.objects.filter(分詞__contains=句物件.看分詞()).values()
    return JsonResponse({'例句': list(例句)})
