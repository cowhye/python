computerchoice = [ "가위", "바위", "보"]

while True:

    answer = input( "가위, 바위, 보 중 하나를 입력하세요 (종료하려면 '끝'):")

    if answer == computerchoice:
        print("비겼습니다!")

    elif answer == ("끝"):
        print(" 게임을 종료합니다.")
        break

    elif answer not in ["가위", "바위", "보"]:
        print("잘못된 입력입니다. 다시 입력해 주세요.")
        continue
    elif answer == "보" and computerchoice == "바위" or answer == "가위" and computerchoice == "보" and answer == "보" and computerchoice == "바위":
        print( " 당신이 이겼습니다! ")
    else:
        print(" 당신이 졌습니다.")
        break


