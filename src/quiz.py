import json
import os 
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

    # 정답 비교 - 맞으면 True 반환
    def check_answer(self, user_answer):
        return user_answer == self.answer

    # JSON에 저장하기 위한 딕셔너리 변환
    def to_dict(self):
        return {
            "question": self.question,
            "choices" : self.choices,
            "answer"  : self.answer
        }

    # JSON 데이터를 불러와서 Quiz 객체로 생성
    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])