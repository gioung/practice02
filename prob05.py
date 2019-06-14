# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def sum(*args):
    total = 0
    for i in args:
        total += i
    return  total


print(sum(1, 2, 4, 8, 9, 4, 6, 4, 8))

