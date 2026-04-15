# main.py (변경 사항 없음)
from quiz_game import QuizGame

def main():
    game = QuizGame()
    try:
        while True:
            game.show_menu()
            choice = input("    선택: ").strip()

            if   choice == "1": game.play()
            elif choice == "2": game.add_quiz()
            elif choice == "3": game.list_quizzes()
            elif choice == "4": game.show_score()
            elif choice == "5":
                print("\n    프로그램을 종료합니다. 안녕히 가세요! 👋")
                break
            else:
                print("  ⚠️  잘못된 입력입니다.")

    except (KeyboardInterrupt, EOFError):
        print("\n\n    [안내] 프로그램을 중단합니다. 데이터를 저장 중...")
        game.save()
        print("    저장 완료. 안녕히 가세요! 👋")

if __name__ == "__main__":
    main()