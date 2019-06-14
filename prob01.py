# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요
s = '/usr/local/bin/python'
list = s.split('/')
list2 = s.rsplit('/', 1)
if list.count('') !=0:
    list.remove('')


print(list)
print(list2)
