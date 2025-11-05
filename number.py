# 정수를 입력 받아 2의 배수 또는 3의 배수인 경우 리스트로 출력
input_value = int(input("정수를 입력하세요:"))

inputvalue = [] 
einput = [] # 리스트 초기화

for i in range(input_value): 
    if i % 2 == 0:  # 2로 나누었을 때 나머지가 0이면, 2의 배수이다.
        einput.append(i) # 리스트에 값을 넣는다
    elif i % 3 == 0: # 3으로 나누었을 때 나머지가 0이면, 3의 배수이다.
        inputvalue.append(i)

print(inputvalue) # 출력
print(einput)
