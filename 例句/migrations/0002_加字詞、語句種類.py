# -*- coding: utf-8 -*-
from csv import DictReader
from curses.ascii import isupper
from os.path import join, dirname, abspath

from django.db import migrations


from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def _加教育部例句(apps, schema_editor):
    例句表 = apps.get_model("例句", "例句表")

    with open(join(dirname(abspath(__file__)), '..', '語料', '例句.csv')) as 檔:
        讀檔 = DictReader(檔)
        for row in 讀檔:
            漢字 = row['例句'].strip()
            音標 = row['例句標音'].strip()
            華語 = row['華語翻譯'].strip()
            if 華語 == '':
                華語 = 漢字
            if isupper(音標[0]) and 音標[-1] in 標點符號:
                句物件 = (
                    拆文分析器
                    .對齊句物件(漢字, 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音標))
                    .轉音(臺灣閩南語羅馬字拼音)
                )
                例句表.objects.create(漢字=漢字, 臺羅=音標, 華語=華語, 分詞=句物件.看分詞())


class Migration(migrations.Migration):

    dependencies = [
        ('例句', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(_加教育部例句),
    ]
