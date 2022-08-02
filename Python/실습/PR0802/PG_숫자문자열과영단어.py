
def num_trans(s):
    num_dic = {                             # 딕셔너리에 키문자열과 값 문자 추가
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }

    for i in num_dic:
        s = s.replace(i, num_dic[i])        # 문자열에있는 zero ~ nine 까지의 문자를 숫자형태로 바꿈
    result = s
    return int(result)
print(num_trans('12zerozerofoursixfive'))