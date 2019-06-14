# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요
until = 333
for i in range(1, until + 1):
     i = str(i)
     r = i.count('3') + i.count('6') + i.count('9')
     if r > 0:
         print(i, '짝'*r)


