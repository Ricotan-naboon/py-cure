# coding: utf-8
from . import girl, precure
from datetime import date
import random

__version__ = '0.0.3'

Precure = precure.PrecureDict()
Precure.add('',
            'ふたりはプリキュア',
            date(2004, 2, 1),
            date(2005, 1, 30))
Precure.add('maxheart',
            'ふたりはプリキュア Max Heart',
            date(2005, 2, 6),
            date(2006, 1, 29))
Precure.add('splashstar',
            'ふたりはプリキュア Splash Star',
            date(2006, 2, 5),
            date(2007, 1, 28))
Precure.add('yes',
            'Yes！ プリキュア5',
            date(2007, 2, 4),
            date(2008, 1, 27))
Precure.add('gogo',
            'Yes！ プリキュア5 Go Go！',
            date(2008, 2, 3),
            date(2009, 1, 25))
Precure.add('fresh',
            'フレッシュプリキュア！',
            date(2009, 2, 1),
            date(2010, 1, 31))
Precure.add('heartcatch',
            'ハートキャッチプリキュア！',
            date(2010, 2, 7),
            date(2011, 1, 30))
Precure.add('suite',
            'スイートプリキュア♪',
            date(2011, 2, 6),
            date(2012, 1, 29))
Precure.add('smile',
            'スマイルプリキュア！',
            date(2012, 2, 5),
            date(2013, 1, 27))
Precure.add('dokidoki',
            'ドキドキ！プリキュア',
            date(2013, 2, 3),
            date(2014, 1, 26))
Precure.add('happinesscharge',
            'ハピネスチャージプリキュア！',
            date(2014, 2, 2),
            date(2015, 1, 25))
Precure.add('goprincess',
            'Go！プリンセスプリキュア',
            date(2015, 2, 1),
            date(2016, 1, 31))
Precure.add('mahotsukai',
            '魔法つかいプリキュア！',
            date(2016, 2, 7),
            date(2017, 1, 29))
Precure.add('kirakira',
            'キラキラ☆プリキュアアラモード！',
            #kirakiraで良いのかわからないので適度に修正お願いします．
            date(2017, 2, 5),
            date(2018, 1, 28))
Precure.add('hagtto',
            'HUGっと！プリキュア',
            date(2018, 2, 4),
            date(2019, 1, 27))
Precure.add('startwinkle',
            'スター☆トゥインクルプリキュア',
            date(2019, 2, 3),
            date(2020, 1, 26))
Precure.add('Healin Good',
            #これは表記的にありなのか...???
            'ヒーリングっど♥プリキュア',
            date(2018, 2, 4),
            None,
            True)

nagisa = girl.FirstGirl(
    '美墨なぎさ', 'キュアブラック',
    "光の使者、キュアブラック！\n"
    "光の使者、キュアホワイト！\n"
    "ふたりはプリキュア！\n"
    "闇の力のしもべ達よ！\n"
    "とっととお家に帰りなさい！")
honoka = girl.FirstGirl(
    '雪城ほのか', 'キュアホワイト',
    "光の使者、キュアブラック！\n"
    "光の使者、キュアホワイト！\n"
    "ふたりはプリキュア！\n"
    "闇の力のしもべ達よ！\n"
    "とっととお家に帰りなさい！")
nagisa.partner = honoka
honoka.partner = nagisa
Precure[''].girls = [nagisa, honoka]

Precure['maxheart'].girls = [
    nagisa,
    honoka,
    girl.FirstGirl(
        '九条ひかり', 'シャイニールミナス',
        "輝く命！ シャイニールミナス！\n"
        "光の心と光の意志、すべてを一つにするために！")
]

Precure['splashstar'].girls = [
    girl.Girl(
        '日向咲', 'キュアブルーム',
        "花開け大地に！\n"
        "輝く金の花！ キュアブルーム！\n"
        "聖なる泉を汚す者よ！\n"
        "阿漕な真似はお止めなさい！\n"),
    girl.Girl(
        '美翔舞', 'キュアイーグレット',
        "羽ばたけ空に！\n"
        "煌めく銀の翼！ キュアイーグレット！\n"
        "聖なる泉を汚す者よ！\n"
        "阿漕な真似はお止めなさい！\n"),
]

nozomi = girl.Girl(
    '夢原のぞみ', 'キュアドリーム',
    "大いなる希望の力、キュアドリーム！"),
rin = girl.Girl(
    '夏木りん', 'キュアルージュ',
    "情熱の赤い炎、キュアルージュ！"),
urara = girl.Girl(
    '春日野うらら', 'かすがのうらら',
    "はじけるレモンの香り、キュアレモネード！"),
komachi = girl.Girl(
    '秋元こまち', 'キュアミント',
    "安らぎの緑の大地、キュアミント！"),
karen = girl.Girl(
    '水無月かれん', 'キュアアクア',
    "知性の青き泉、キュアアクア！"),
Precure['yes'].girls = [
    nozomi,
    rin,
    urara,
    komachi,
    karen
]

Precure['gogo'].girls = [
    nozomi,
    rin,
    urara,
    komachi,
    karen,
    girl.Girl(
        '美々野くるみ', 'ミルキィローズ',
        "青いバラは秘密のしるし！ ミルキィローズ！"),
]

Precure['fresh'].girls = [
    girl.Girl(
        '桃園ラブ', 'キュアピーチ',
        "ピンクのハートは愛あるしるし！\n"
        "もぎたてフレッシュ、キュアピーチ！"),
    girl.Girl(
        '蒼乃美希', 'キュアベリー',
        "ブルーのハートは希望のしるし！\n"
        "つみたてフレッシュ、キュアベリー！"),
    girl.Girl(
        '山吹祈里', 'キュアパイン',
        "イエローハートは祈りのしるし！\n"
        "とれたてフレッシュ、キュアパイン！"),
    girl.Girl(
        '東せつな', 'キュアパッション',
        "真っ赤なハートは幸せの証！\n"
        "熟れたてフレッシュ、キュアパッション！"),
]

Precure['heartcatch'].girls = [
    girl.Girl(
        '花咲つぼみ', 'キュアブロッサム',
        "大地に咲く一輪の花！ キュアブロッサム！"),
    girl.Girl(
        '来海えりか', 'キュアマリン',
        "海風に揺れる一輪の花！ キュアマリン！"),
    girl.Girl(
        '明堂院いつき', 'キュアサンシャイン',
        "陽の光浴びる一輪の花！ キュアサンシャイン！"),
    girl.Girl(
        '月影ゆり', 'キュアムーンライト',
        "月光に冴える一輪の花 キュアムーンライト！"),
    girl.Girl(
        '花咲薫子', 'キュアフラワー',
        "聖なる光に輝く一輪の花 キュアフラワー！"),
]

Precure['suite'].girls = [
    girl.Girl(
        '北条響', 'キュアメロディ',
        "爪弾くは荒ぶる調べ！ キュアメロディ！"),
    girl.Girl(
        '南野奏', 'キュアリズム',
        "爪弾くはたおやかな調べ！ キュアリズム！"),
    girl.Girl(
        '黒川エレン', 'キュアビート',
        "爪弾くは魂の調べ！ キュアビート！"),
    girl.Girl(
        '調辺アコ', 'キュアミューズ',
        "爪弾くは女神の調べ！ キュアミューズ！"),
]

Precure['smile'].girls = [
    girl.Girl(
        '星空みゆき', 'キュアハッピー',
        "キラキラ輝く未来の光！ キュアハッピー！"),
    girl.Girl(
        '日野あかね', 'キュアサニー',
        "太陽サンサン熱血パワー！ キュアサニー！"),
    girl.Girl(
        '黄瀬やよい', 'キュアピース',
        "ピカピカピカリンジャンケンポン！"+random.choice(["(グー！)","(チョキ！)","(パー！)"])+"キュアピース！"),
        #黄瀬やよい専用にrandomを使用．
    girl.Girl(
        '緑川なお', 'キュアマーチ',
        "勇気リンリン直球勝負！ キュアマーチ！"),
    girl.Girl(
        '青木れいか', 'キュアビューティ',
        "しんしんと降り積もる清き心！ キュアビューティ！"),
]

Precure['dokidoki'].girls = [
    girl.Girl(
        '相田マナ', 'キュアハート',
        "みなぎる愛！ キュアハート！\n"
        "愛を無くした悲しいジコチューさん、"
        "このキュアハートがあなたのドキドキ取り戻してみせる！"),
    girl.Girl(
        '菱川六花', 'キュアダイヤモンド',
        "英知の光！ キュアダイヤモンド！\n"
        "人の思いを踏みにじるなんて許せない、"
        "このキュアダイヤモンドがあなたの頭を冷やしてあげる！"),
    girl.Girl(
        '四葉ありす', 'キュアロゼッタ',
        "ひだまりポカポカ キュアロゼッタ！\n"
        "世界を制するのは愛だけです、"
        "さぁ、あなたも私と愛を育んでくださいな"),
    girl.Girl(
        '剣崎真琴', 'キュアソード',
        "勇気の刃！ キュアソード！\n"
        "このキュアソードが愛の剣で"
        "あなたの野望を断ち切ってみせる！"),
    girl.Girl(
        '円亜久里', 'キュアエース',
        "愛の切り札！ キュアエース！\n"
        "美しさは正義の証し、ウインク一つで、"
        "あなたのハートを射抜いて差し上げますわ"),
]

Precure['happinesscharge'].girls = [
    girl.Girl(
        '愛乃めぐみ', 'キュアラブリー',
        "世界に広がるビッグな愛！ キュアラブリー！"),
    girl.Girl(
        '白雪ひめ', 'キュアプリンセス',
        "天空に舞う蒼き風！ キュアプリンセス！"),
    girl.Girl(
        '大森ゆうこ', 'キュアハニー',
        "大地に実る命の光！キュアハニー！"),
    girl.Girl(
        '氷川いおな', 'キュアフォーチュン',
        "夜空にきらめく希望の星！ キュアフォーチュン！")
]

Precure['goprincess'].girls = [
    girl.Girl(
        '春野はるか', 'キュアフローラ',
        "咲きほこる、花のプリンセス！キュアフローラ！"),
    girl.Girl(
        '海藤みなみ', 'キュアマーメイド',
        "澄み渡る、海のプリンセス！キュアマーメイド！"),
    girl.Girl(
        '天ノ川きらら', 'キュアトゥインクル',
        "きらめく、星のプリンセス！キュアトゥインクル！"),
    girl.Girl(
        'トワ', 'キュアスカーレット',
        "真紅の炎のプリンセス！キュアスカーレット！")
]

Precure['mahotsukai'].girls = [
    girl.Girl(
        '朝日奈みらい', 'キュアミラクル',
        "二人の奇跡！キュアミラクル！"),
    girl.Girl(
        '十六夜リコ', 'キュアマジカル',
        "二人の魔法！キュアマジカル！"),
    girl.Girl(
        '花海ことは', 'キュアフェリーチェ',
        "あまねく命に祝福を！キュアフェリーチェ！")
]

Precure['kirakira'].girls = [
    girl.Girl(
        '宇佐美いちか', 'キュアホイップ',
        "キュアラモード デコレーション！ショートケーキ！\n"
        "元気と笑顔を レッツ・ラ・まぜまぜ！\n"
        "キュアホイップ！ できあがり！"),
    girl.Girl(
        '有栖川ひまり', 'キュアカスタード',
        "キュアラモード デコレーション！プリン！\n"
        "知性と勇気を レッツ・ラ・まぜまぜ！\n"
        "キュアカスタード！できあがり！"),
    girl.Girl(
        '立神あおい', 'キュアジェラート',
        "キュアラモード デコレーション！アイス！\n"
        "自由と情熱を レッツ・ラ・まぜまぜ！\n"
        "キュアジェラート！できあがり！"),
    girl.Girl(
        '琴爪ゆかり', 'キュアマカロン',
        "キュアラモード デコレーション！マカロン！\n"
        "美しさとときめきを レッツ・ラ・まぜまぜ！\n"
        "キュアマカロン！できあがり！"),
    girl.Girl(
        '剣城あきら', 'キュアショコラ',
        "キュアラモード デコレーション！チョコレート！\n"
        "強さと愛を　レッツ・ラ・まぜまぜ！\n"
        "キュアショコラ！できあがり！"),
    girl.Girl(
        'キラ星シエル','キュアパルフェ',
        "キュアラモード デコレーション！パフェ！\n"
        "夢と希望を レッツ・ラ・まぜまぜ！\n"
        "キュアパルフェ！できあがり！")
]

Precure['hagtto'].girls = [
    girl.Girl(
        '野乃はな', 'キュアエール',
        "輝く未来を抱きしめて！みんなを応援！\n"
        "元気のプリキュア キュアエール！"),
    girl.Girl(
        '薬師寺さあや', 'キュアアンジュ',
        "輝く未来を抱きしめて！みんなを癒す！\n"
        "知恵のプリキュア キュアアンジュ！"),
    girl.Girl(
        '輝木ほまれ', 'キュアエトワール',
        "輝く未来を抱きしめて！みんな輝け！\n"
        "力のプリキュア キュアエトワール！"),
    girl.Girl(
        '愛崎えみる', 'キュアマシェリ',
        "輝く未来を抱きしめて！みんな大好き！\n"
        "愛のプリキュア！キュアマシェリ！"),
    girl.Girl(
        'ルールー・アムール', 'キュアアムール',
        "輝く未来を抱きしめて！みんな大好き！\n"
        "愛のプリキュア！キュアアムール！")
    #ここ「・」を付けるべきか迷ってます
]

Precure['startwinkle'].girls = [
    girl.Girl(
        '星奈ひかる', 'キュアスター',
        "宇宙に輝くキラキラ星！キュアスター！"),
    girl.Girl(
        '羽衣ララ', 'キュアミルキー',
        "天にあまねくミルキーウェイ！キュアミルキー！"),
    girl.Girl(
        '天宮えれな', 'キュアソレイユ',
        "宇宙を照らす！灼熱のきらめき！キュアソレイユ！"),
    girl.Girl(
        '香久矢まどか', 'キュアセレーネ',
        "夜空に輝く！神秘の月あかり！キュアセレーネ！"),
    girl.Girl(
        'ユニ', 'キュアコスモ',
        "銀河に光る虹色のスペクトル！キュアコスモ！")
]

Precure['Healin Good'].girls = [
    girl.Girl(
        '花寺のどか', 'キュアグレース',
        "重なる二つの花！キュアグレース！"),
    girl.Girl(
        '沢泉ちゆ', 'キュアフォンテーヌ',
        "交わる二つの流れ！キュアフォンテーヌ！"),
    girl.Girl(
        '平光ひなた', 'キュアスパークル',
        "溶け合う二つの光！キュアスパークル！")
]

#以下将来性の為にテンプレートとして
#Precure[''].girls = [
    #girl.Girl(
        #'', '',
        #""),
    #girl.Girl(
        #'', '',
        #""),
    #girl.Girl(
        #'', '',
        #"")
#]

#Precure.add('',
            #'',
            #date(, , ),
            #date(, , ))
