import json
import os
 
 
# ─────────────────────────────────────────
# Quiz 클래스 : 퀴즈 한 문제를 담는 설계도
# ─────────────────────────────────────────
class Quiz:
    # 데이터를 객체에 저장
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices  = choices
        self.answer   = answer
    # 문제 출력
    def display(self, idx, total):
        print(f"\n----------------------------------------")
        print(f"    [문제 {idx}/{total}]")
        print(f"    {self.question}\n")
        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")
        print(f"----------------------------------------")
    # 정답 비교 - 맞으면 1반환
    def check_answer(self, user_answer):
        return user_answer == self.answer
    #JSON에 저장
    def to_dict(self):
        return {
            "question": self.question,
            "choices" : self.choices,
            "answer"  : self.answer
        }
    # JSON을 불러옴
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])
    
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