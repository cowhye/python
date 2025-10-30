# 덧셈, 뺄셈, 곱셈, 나눗셈 계산기
# 사용자로부터 두 개의 정수 숫자를 입력 받고, 그 합, 차, 곱 , 나눗셈의 결과를 출력하는 프로그램을 작성
# - 사용자에게 두 정수 숫자를 입력 받습니다
number1 = int(input("첫 번째 숫자를 입력하세요:"))
number2 = int(input("두 번째 숫자를 입력하세요:"))
# - 입력받은 숫자들의 합, 차, 곱, 나눗셈 결과를 계산합니다
# 입력받은 숫자들의 합을 구합니다
total_amount = float(number1 + number2)
# 입력받은 숫자들의 차를 구합니다
minus = float(number1-number2)
# 입력받은 숫자들의 곱을 구합니다
multiplication = float(number1*number2)
# 입력받은 숫자들의 나눗셈 결과를 구합니다
division = float(number1/number2)
# - 계산된 결과를 출력합니다
print(f"""
합:{total_amount}
차: {minus}
곱 : {multiplication}
나눗셈: {division}
""")
# print(f"""
#합: {total_amount}
#차: {minus}
#곱: {multiplication}
#나눗셈: {division}
#""")
# 안녕핫요요요