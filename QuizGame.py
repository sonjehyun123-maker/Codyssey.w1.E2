import json
from Quiz import Quiz  # quiz.py 파일에서 Quiz 클래스를 가져옴

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