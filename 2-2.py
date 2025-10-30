import random

def game():
    scissors = "가위"
    rock = "바위"
    paper = "보"

    win_count = 0
    draw_count = 0
    lose_count = 0
    total_count = 0

    while True:
        # 사용자 입력 받기
        answer = input("가위, 바위, 보 중 하나를 입력하세요 (종료하려면 '끝'): ").strip()

        # '끝' 입력 시 게임 종료
        if answer == "끝":
            if total_count > 0:
                win_rate = (win_count / total_count) * 100
                print(f"게임을 종료합니다. 총 {total_count}판 중 이긴 횟수: {win_count}번, 비긴 횟수: {draw_count}번, 진 횟수: {lose_count}번")
                print(f"승률: {win_rate:.2f}%")
            else:
                print("게임을 시작하지 않았습니다.")
            break
        
        # 잘못된 입력 처리
        if answer not in [scissors, rock, paper]:
            print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력해주세요.")
            continue

        # 컴퓨터의 선택
        computer_choice = random.choice([scissors, rock, paper])
        print(f"컴퓨터의 선택: {computer_choice}")

        # 승패 판별
        if answer == computer_choice:
            print("비겼습니다!")
            draw_count += 1
        elif (answer == scissors and computer_choice == paper) or \
             (answer == rock and computer_choice == scissors) or \
             (answer == paper and computer_choice == rock):
            print("당신이 이겼습니다!")
            win_count += 1
        else:
            print("컴퓨터가 이겼습니다!")
            lose_count += 1

        # 게임 진행 후 결과 출력
        total_count += 1
        print(f"현재까지 승률: {win_count / total_count * 100:.2f}%")
        print(f"이긴 횟수: {win_count}번, 비긴 횟수: {draw_count}번, 진 횟수: {lose_count}번")
        print("-" * 40)

if __name__ == "__main__":
    game()
