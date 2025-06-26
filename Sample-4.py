jumin = input("주민등록번호 : ") # 주민등록번호 입력
jumin = jumin.split('-') # 주민등록번호를 2개의 항목으로 분리
jumin = jumin[0] + jumin[1] # 분리된 값을 리스트가 아닌 문자열로 저장
 
j=2 ; tot=0
# j = 2~9까지 증가, 10이되면 다시 2로 초기화
# tot = 각각의 숫자를 곱한 값의 총 합을 저장 할 변수
 
for i in range(0,len(jumin)-1):
    tot += int(jumin[i]) * j
    j+=1
    if j == 10: j=2
# 절차1. 반복문을 이용하여 계산
print(tot) # 절차1. 값 확인
 
tot = 11 - (tot % 11)
print(tot)
# 절차2와 절차3을 계산한 최종 값 확인
 
if int(jumin[-1]) == tot:
    print("유효")
else:
    print("유효하지 않음")
# 주민등록번호 마지막 자리와 최종 값이 일치하는지 확인
