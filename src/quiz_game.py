import json
from quiz import Quiz  # quiz.py 파일에서 Quiz 클래스를 가져옴

class QuizGame:
 
    STATE_FILE = "state.json"   # 저장 파일 이름
 
    # 기본 퀴즈 5개 - json 파일이 없을 때 사용
    DEFAULT_QUIZZES = [
        Quiz("print(2 + 3 * 2) ?",
             ["10", "8", "7", "12"], 2),
        Quiz("다음중 리스트는??",
             ["'1, 2, 3'", "{1, 2, 3}", "(1, 2, 3)", "[1, 2, 3]"], 4),
        Quiz("1GB의 크기는?",
             ["100", "1000", "1024", "1234"], 3),
        Quiz("print(2 ** 3) ?",
             ["5", "6", "7", "8"], 4),
        Quiz("print(\"2\" + \"3\")",
             ["5", "8", "18", "23"], 4),
    ]
#json 불러오기
def load(self):
        try:
            with open(self.STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", 0)
            print(f"    📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except FileNotFoundError:  #json파일이 없다면
            print("    [안내] 저장 파일이 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = list(self.DEFAULT_QUIZZES)
            self.save()
        except (json.JSONDecodeError, KeyError):
            print("    [경고] 저장 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
            self.quizzes = list(self.DEFAULT_QUIZZES)
            self.save()
#json에 저장
def save(self):
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(self.STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"[오류] 파일 저장 실패: {e}")

#---------------JSON-----------------
# 메뉴 프린트
def show_menu(self):
        print("\n" + "=" * 40)
        print("            🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("    1. 퀴즈 풀기")
        print("    2. 퀴즈 추가")
        print("    3. 퀴즈 목록")
        print("    4. 점수 확인")
        print("    5. 종료")
        print("=" * 40)
# 게임 시작
def play(self):
        if not self.quizzes:
            print("\n    [안내] 등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)
        print(f"\n    📝 퀴즈를 시작합니다! (총 {total}문제)")

        for idx, quiz in enumerate(self.quizzes, start=1):
            quiz.display(idx, total)
            while True:
                ans = input("    정답 입력 (1~4): ").strip()
                if ans.isdigit() and 1 <= int(ans) <= 4:
                    user_answer = int(ans)
                    break
                print("  ⚠️  1~4 사이의 숫자를 입력하세요.")

            if quiz.check_answer(user_answer):
                print("    ✅ 정답입니다!\n")
                score += 1
            else:
                correct = quiz.choices[quiz.answer - 1]
                print(f"    ❌ 오답! 정답은 {quiz.answer}번 '{correct}' 입니다.\n")

        percent = score / total * 100
        print("=" * 40)
        print(f"    🏆 결과: {total}문제 중 {score}문제 정답! ({percent:.0f}점)")

        if score > self.best_score:
            print(f"    🎉 새로운 최고 점수입니다!")
            self.best_score = score
            self.save()
        print("=" * 40)

# 퀴즈 추가
def add_quiz(self):
        print("\n    📌 새로운 퀴즈를 추가합니다.")
        question = input("    문제를 입력하세요: ").strip()
        choices = [input(f"    선택지 {i}: ").strip() for i in range(1, 5)]
        while True:
            ans = input("    정답 번호 (1~4): ").strip()
            if ans.isdigit() and 1 <= int(ans) <= 4:
                answer = int(ans)
                break
            print("  ⚠️  1~4 사이의 숫자를 입력하세요.")
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save()
        print("\n    ✅ 퀴즈가 추가되었습니다!")

# 퀴즈 목록 출력
def list_quizzes(self):
        print(f"\n    📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"    [{idx}] {quiz.question}")

# 최고 점수 출력
def show_score(self):
        total = len(self.quizzes)
        percent = (self.best_score / total * 100) if total > 0 else 0
        print(f"\n🏆 최고 점수: {percent:.0f}점 ({total}문제 중 {self.best_score}문제 정답)")