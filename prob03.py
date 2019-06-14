# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요
# 2)각 단어의 빈도수도 함께 출력해 보세요
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.replace('.', '').replace(',', '').upper()
# while True:
#     index = 0
#     if s.find('.') != -1:
#         index = s.find('.')
#     elif s.find(',') != -1:
#         index = s.find(',')
#     elif s.find('\n') != -1:
#         index = s.find('\n')
#     else:
#         break
#     s = s[:index] + s[index+1:]

li = s.split(' ')

li2 = list(set(li))
print(li2)
for e in li2:
    print(e, li.count(e))



