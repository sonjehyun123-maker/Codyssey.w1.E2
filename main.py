import json
import os
 
 
# ─────────────────────────────────────────
# Quiz 클래스 : 퀴즈 한 문제를 담는 설계도
# ─────────────────────────────────────────
class Quiz:
 
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices  = choices
        self.answer   = answer
 
    def display(self, idx, total):
        print(f"\n----------------------------------------")
        print(f"    [문제 {idx}/{total}]")
        print(f"    {self.question}\n")
        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")
        print(f"----------------------------------------")
 
    def check_answer(self, user_answer):
        return user_answer == self.answer
 
    def to_dict(self):
        return {
            "question": self.question,
            "choices" : self.choices,
            "answer"  : self.answer
        }
 
    # ── [변경 1] @classmethod 제거 → 일반 함수로 변경 ──
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])