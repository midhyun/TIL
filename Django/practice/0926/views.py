from django.shortcuts import render
import random
# Create your views here.
def base(request):
    return render(request)


def oddeven(request, number):
    if number % 2 == 0:
        result = "짝수"
    elif number % 2 == 1:
        result = "홀수"
    elif number == 0:
        result = "0"
    context = {
        "result": result,
        "number": number,
    }

    return render(request, "oddeven.html", context)


def calculate(request, num1, num2):
    result = [num1 + num2, num1 - num2, num1 * num2, num1 // num2]
    context = {
        "result": result,
        "num1": num1,
        "num2": num2,
    }
    return render(request, "calculate.html", context)


def dormitory(request):
    return render(request, "dormitory.html")


def dormitory_s(request):
    dormitories = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    dormitories_img = [
        "https://mblogthumb-phinf.pstatic.net/MjAxODAzMDNfMTAw/MDAxNTIwMDYyODc1NTkz.8JUhBQ0UYI1miZtu3OMgS3kitQ5ep125OlAZ5uGJKnEg.sJuzZ0FuPAeHBt0o5SNz_HXabDdjbxETrsdd_5Zv0dcg.GIF.nong236/http3A2F2F38.media.tumblr.com2F5600ed5f5cb0c8fd602578a1971f72372Ftumblr_n72.gif?type=w800",
        "https://mblogthumb-phinf.pstatic.net/MjAxODAzMDNfMTAx/MDAxNTIwMDYyODc1ODg5.rjBLfrrl6_rOnjSNdkB1YvbbhpBV6wBwSRscrzHE5Ewg.sITEQoABYdbmcCcWbdthvcNqI2z-yUIJToAZ7JVCf7Yg.GIF.nong236/http3A2F2F38.media.tumblr.com2F58fdabf8f4f52c6aeffcfe0afcb273cd2Ftumblr_n72.gif?type=w800",
        "https://mblogthumb-phinf.pstatic.net/MjAxODAzMDNfMTY3/MDAxNTIwMDYyODc2NTg3.l_zyAFyn8_eOUNdk5Ou9IgkIL8p9cL_F4kFwyeYjU94g.lAtvRF_YOpvEV2Vxj6sUjRjS9hLGIMCKSS3GsnLntxwg.GIF.nong236/http3A2F2F37.media.tumblr.com2Fad19ec8a68e8806f3335b1dbb3c8792e2Ftumblr_n72.gif?type=w800",
        "https://mblogthumb-phinf.pstatic.net/MjAxODAzMDNfMTUx/MDAxNTIwMDYyODc2MTc0.UZS34mZI84ic1vFMkMyk7JCTmkpzZxprjFshkllOV7Qg.rpVd2C64B5uhqqWYkljZUfOylS50sEDSRFt5cvuS40Ag.GIF.nong236/http3A2F2F37.media.tumblr.com2F32885aabaff4223b8af12735b33b28702Ftumblr_n72.gif?type=w800",
    ]
    familyname = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오"]
    name = request.GET.get("name")
    for i in range(len(familyname)):
        if familyname[i] == name[0]:
            f_name = i
    else:
        f_name = 0
    birthday = int(request.GET.get("birthday"))
    result = (f_name + birthday) % 4
    context = {
        "result": dormitories[result],
        "img": dormitories_img[result],
        "name": name,
    }
    return render(request, "dormitory_s.html", context)


def lorem_kor(request):

    return render(request, "lorem_kor.html")


def lorem_kor_result(request):
    sentence = ['계절이', '지나가는', '하늘에는', '가을로', '가득', '차', '있습니다.', '나는', '아무', '걱정도', '없이', '가을', '속의', '별들을', '다', '헤일', '듯합니다.', '가슴', '속에', '하나', '둘', '새겨지는', '별을', '이제', '다', '못', '헤는', '것은', '쉬이', '아침이', '오는', '까닭이요,', '내일', '밤이', '남은', '까닭이요,', '아직', '나의', '청춘이', '다하지', '않은', '까닭입니다.', '별', '하나에', '추억과', '별', '하나에', '사랑과', '별', '하나에', '쓸쓸함과', '별', '하나에', '동경과', '별', '하나에', '시와', '별', '하나에', '어머니,', '어머니,', '어머님,', '나는', '별', '하나에', '아름다운', '말', '한마디씩', '불러', '봅니다.', '소학교', '때', '책상을', '같이', '했던', '아이들의', '이름과,', '패,', '경,', '옥,', '이런', '이국', '소녀들의', '이름과,', '벌써', '아기', '어머니', '된', '계집애들의', '이름과,', '가난한', '이웃', '사람들의', '이름과,', '비둘기,', '강아지,', '토끼,', '노새,', '노루,', "'프랑시스", "잠[1]',", "'라이너", '마리아', "릴케[2]'", '이런', '시인의', '이름을', '불러', '봅니다.', '이네들은', '너무나', '멀리', '있습니다.', '별이', '아스라이', '멀듯이.', '어머님,', '그리고', '당신은', '멀리', '북간도에', '계십니다.', '나는', '무엇인지', '그리워', '이', '많은', '별빛이', '내린', '언덕', '위에', '내', '이름자를', '써', '보고', '흙으로', '덮어', '버리었습니다.', '따는', '밤을', '새워', '우는', '벌레는', '부끄러운', '이름을', '슬퍼하는', '까닭입니다.', '그러나', '겨울이', '지나고', '나의', '별에도', '봄이', '오면', '무덤', '위에', '파란', '잔디가', '피어나듯이', '내', '이름자', '묻힌', '언덕', '위에도', '자랑처럼', '풀이', '무성할', '거외다.']
    moondan = int(request.GET.get("moondan"))
    words = int(request.GET.get("words"))
    result = []
    for i in range(moondan):
        temp = ''
        for j in range(words):
            temp += random.choice(sentence)
            temp += ' '
        result.append(temp)
    context = {
        'result' : result,
        'moondan' : moondan,
    }

    return render(request, "lorem_kor_result.html", context)
