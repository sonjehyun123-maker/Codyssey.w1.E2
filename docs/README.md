# Codyssey.w1.E2

## 결과물
    다음 3가지 조건을 만족하는 Python 콘솔 프로그램 1개와 GitHub 저장소 1개를 완성한다.

### 동작하는 퀴즈 게임
    프로그램 실행 시 메뉴에서 번호를 선택하면, 선택 결과에 따라 퀴즈 출제/등록/목록/점수 확인/종료 화면이 출력된다.
    퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인 기능이 동작한다.
    본인이 선택한 주제의 퀴즈가 5개 이상 포함되어 있다.
    프로그램을 종료하고 다시 실행해도 추가한 퀴즈와 최고 점수가 유지된다. (파일 저장)
### 코드 구조
    최소 2개 이상의 클래스가 정의되어 있다. (예: Quiz, QuizGame)
    기능별로 메서드가 분리되어 있다. (입력 처리/게임 진행/저장 로직 등)
    데이터는 프로젝트 루트의 state.json에 UTF-8 인코딩으로 저장하고 불러온다.
    
### GitHub 저장소
    프로젝트 코드가 GitHub에 업로드되어 있다.
    > https://github.com/sonjehyun123-maker/Codyssey.w1.E2
    최소 10개 이상의 의미 있는 커밋이 존재한다.
    > 
    최소 1회 이상의 브랜치 생성 및 병합(checkout, merge) 기록이 있다.
    > git log --oneline --graph
    clone과 pull을 각각 1회 이상 사용한 기록이 있다.
    > git clone 주소
    > git pull
    README.md에 아래 항목이 포함되어 있다.
        > 프로젝트 개요
            > 동작하는 퀴즈 게임 프로그램을 개발
            >python 기초 공부
        > 퀴즈 주제 선정 이유
            > 간단한 파이썬 문제
        > 실행 방법
            > python main.py
        > 기능 목록
            (1) 퀴즈풀기
                - 저장된 문제 출력/실행 // 점수 누적 및 점수 기억 
            (2) 퀴즈추가
                - 저장된 문제 이외에 사용자가 문제를 낼 수 있도록 함
            (3) 퀴즈목록
                - 저장된 문제 출력
            (4) 점수확인
                - 퀴즈 풀기(1)에서 저장된 최고 점수를 출력
            (5) 종료
                - eixt
            etc. 예외처리(숫자가 아닌 잘못된 입력 처리)
                데이터 저장(종료 후에도 데이터 유지)
        > 파일 구조
            >  src/
                ├── main.py          # 프로그램 실행 진입점 
                ├── quiz_game.py     # 게임 흐름 제어 및 전체 로직 담당 (Menu, Play 등등...)
                ├── quiz.py          # 개별 퀴즈 객체 정의 및 데이터 모델
                └── state.json       # 최고 점수 및 퀴즈 데이터 영속성 저장 파일

        > 데이터 파일 설명
            > state.json
                - 위치: src 디렉토리
                - 역할: 퀴즈 데이터 및 최점 점수 저장
                ```JSON
                { "quizzes": [ //저장된 퀴즈 목록
                    {
                    "question": "문제 내용",
                    "choices": ["보기1", "보기2", "보기3", "보기4"],
                    "answer": 1 //정답 번호
                    }
                ],
                "best_score": 3 //최고점수 저장
                }
                ```
## Python 기초
 - 변수란? : 값이 들어가있는 공간. (변경 가능)
 - int, str, bool, list, dict의 차이
    - int: 소수점이 없는 숫자 = 정수
    - str: 글자들의 묶음 = 문자열
    - bool: 참과 거짓 판별 = 판별기
    - list: 여러개의 값을 순서대로 저장 = 묶음
    - dict: list에서 진화 / 여러가지 이름표 + 값 
 - if/elif/else로 조건
    - if : 만약이라는 뜻으로 조건을 달아 아래 명령 실행
    - elif : if가 아닌 다른 조건으로 명령 실행
    - else : if도 elif도 아닌 나머지 가능성 모두
 - for와 while의 차이
    - for : 정해진 횟수까지 반복
    - while : 정해진 조건까지 반복
 - 함수를 정의하고, 매개변수와 반환값을 활용
    - 함수 정의 
        - def main():dsply(self): save(self): load(self) run(self), play(self), add(self), show(self) etc...
    - 매개변수와 반환값 활용
        - Quiz생성: Quiz(question, choices, answer)

## 클래스와 객체
 - 클래스란? : 데어터 속성 + 데이터를 다루는 매서드
 - __init__ 메서드와 self의 역할
    - __init__역할 : 생성된 객체 초기화, 초기 값 설정.
    - self 역할 : QizeGame내 속성과 메서드에 접근할수 있게함.
    ```QuizGame
        def __init__(self):
        self.quizzes = []   #퀴즈 목록
        self.best_score = 0 #최고점수
        self.load()         #시작 시 데이터를 가져옴.
    ```

## 파일입출력
 - 파일을 열고, 읽고, 쓰는 기본 과정
    - 열기: content = f.read()
    - 읽기: f = open("파일명", "명령")
        - r: 읽기 / w : 쓰기 / a : 추가
    - 쓰기: f = open("data.txt", "w")
            f.write("hello")
 - JSON 형식이 무엇이고, 왜 데이터 저장에 사용
    - JSON: 데이터를 구조화해서 저장하는 텍스트
    - 사용 이유 1. 구조유지 / 2. 파일로 저장 가능 / 3. 다양한언어에서 사용 가능
 - try/except 필요 이유
    - 오류로 인한 프로그램 중단 방지 및 흐름 유지, 데이터 손상 방지
    - 발생 가능한 실패 케이스: 

## Git기초
 - Git이란? : 파일 변경내용 관리도구
 - Git명령어
    - init : git 저장소 초기화
    - add : 새롭게 업데이트된 파일을 스테이징 영역에 올림
    - commit : 스테이징 파일을 로컬 저장소에 저장함 (+꼬리표)
    - push: github에 commit 한 내용을 올림
    - pull: github에서 commit 한 내용을 내려받음
    - checkout: 다른 브랜치로 이동하거나 특정 시점 파일 복구시 사용
    - clone: github에서 프로그램을 불러옴 git clone github주소 
 - 브랜치 : 작업 흐름을 분리하는 독립된 작업라인.
 ![브랜치 생성/병합](./images/git%20log%20--oneline%20--graph.png)
    - main안정 but 새로운 기능 추가 할 때 사용.
    -   main:     A --- B --- C
                         \
        feature:          D --- E
        
    - 브랜치 사용 순서
        1) git branch feature / 생성
        2) git switch feature / main->feature로 변경
        3) git switch main / feature->main으로 변경
        4) git merge feature / main + faeture해서 새로운 커밋 생성.
 - 원격저장소를 clone하고 pull로 변경사항 적용(스크린샷)

 ## 체크리스트
    []GitHub에 코드가 업로드되어 있고 10개 이상의 의미 있는 커밋이 존재
        ![](./images/commit.png)
        - https://github.com/sonjehyun123-maker/Codyssey-w1-E2
    []커밋을 어떤 단위로 나누었고, 커밋 메시지 규칙
        초반에는 커밋을 시간 단위로 무분별하게 기록하고, 메시지 또한 의미 없이 작성하였다.
        이후에는 커밋 단위를 하나의 기능 구현 또는 변경 사항 단위로 명확히 나누었으며, 
        커밋 메시지는 어떤 기능을 새로 적었는지, 어떤 코드를 고쳤는지 같이 적어 작업 내용을 구체적으로 작성하도록 개선하였다.

    []Quiz와 QuizGame 등 클래스들의 책임을 어떻게 나눴는지 설명할 수 있는가?
        - Quiz: 데이터 관리, 보관
        - QuizGames: 게임흐름 진행 
            - Quiz 객체 리스트 배열
            - Quiz데이터를 활용하여 실제로 게임이 동작하게 함
            - json파일 없을시 기초데이터로 생성

    []state.json 데이터 구조(필드/중첩 구조)를 현재 형태로 설계한  + json으로 데잍 저장 이유/특징
        - 사람이 직접 읽고 수정 가능
        - Python 내장 json 모듈로 별도 설치 없이 사용 가능
        - to_dict() / from_dict()로 객체 ↔ JSON 변환이 단순함

    []퀴즈 데이터가 1000개 이상으로 늘어난다면 현재 JSON 저장 방식에 어떤 한계
        load()시 전체를 한 번에 메모리에 올림 → 데이터가 클수록 느려짐
        save()도 전체를 덮어씀 → 퀴즈 1개 추가해도 1000개 전부 다시 씀
        검색/필터 기능이 없어서 특정 퀴즈 찾으려면 전체 순회

    []만약 state.json이 손상되어 JSON 파싱에 실패한다면, 사용자가 데이터를 잃지 않도록 어떤 대응(복구/백업/초기화)이 가능한지 설명
        ① 백업 파일 유지
        save() 호출 시 state.json → state_backup.json 복사 후 저장
        손상 감지 시 백업에서 복구

        ② 임시 파일로 안전 저장
        state_tmp.json에 먼저 쓰고
        성공하면 state.json으로 이름 변경 (덮어쓰기 실패 방지)

        ③ 손상 감지 시 사용자에게 선택권 부여
        "파일 손상 - 1.백업복구 2.초기화" 선택하게 함

    []“정답 채점 방식(점수 계산)”이나 “퀴즈 구조(선택지 개수 등)” 요구사항이 바뀐다면, 어떤 파일/클래스/메서드를 수정
        -----------------------------------------------------
        변경 내용           |      수정 파일/메서드점수
        -----------------------------------------------------
        계산 방식           |      QuizGame.play()
        선택지 수 변경       |      Quiz.__init__, display(), get_int() 범위, _init_data()
        정답 채점 기준 변경   |      Quiz.check()
        -----------------------------------------------------

    []clone/pull
        - git clone (github주소)
        
        - git pull origin main
        ```
        From https://github.com/sonjehyun123-maker/Codyssey-w1-E2
        * branch            main       -> FETCH_HEAD
        Already up to date.
        ```
    [] “입력 처리”, “게임 진행”, “데이터 저장/불러오기” 로직을 어떤 기준으로 분리했는지 설명할 수 있는가?
        - 분리 기준: 하나의 파일/클래스가 하나의 역할만 갖도록 함
        - main.py       : 게임 진입점 / 실행
        - Quiz.py       : 퀴즈 데이터 구조 
        - QuizGame.py   : 게임 진행+저장+불러오기 
        - utils.py      : 입력처리/안전 종료

    [] 클래스를 사용한 이유는 무엇이며, 함수만으로 구현할 때와 어떤 차이가 있는지 설명할 수 있는가?
        - 클래스 = 데이터 + 동작 : 객체를 생성하여 데이터, 동작을 한번에 동작하게 함.
        - 함수만으로 했을 때: 데이터와 동작이 묶여있지 않아 매번 return값을 넘기고 받아야함. + 함수 추적의 어려움.
