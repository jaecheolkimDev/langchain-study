# 🍃 랭체인 학습 프로젝트 (by. Python)
> 랭체인을 학습하는 프로젝트입니다.
---

## 📚 Learning Resources (학습한 책/강의)
```
[강사: 제이쓴] "한시간으로 끝내는 LangChain 기본기"
[강사: 제이쓴] "RAG를 활용한 LLM Application 개발 (feat. LangChain)"
[강사: 제이쓴] "LangGraph를 활용한 AI Agent 개발 (feat. MCP)"
```

---

## 📝 학습 기록
```
[o] LangChain
[o] LCEL (LangChain Expression Language)
[ ] RAG
[ ] LangGraph
[ ] MCP
```
---

## 🛠 기술 스택 (Tech Stack)

| 구분                | 기술 스택      | 버전       |
|:------------------|:-----------|:---------|
| **Language**      | Python     | 3.10.8   |
| **IDE**           | Pycharm    | 2023.1.6 |

---

## 📦 프로젝트 구조 (Project Structure)

```
langchain-study
├── .venv/                  # 파이썬 가상환경
├── app/                    # 소스 코드가 담기는 최상위 패키지
│   ├── core/               # 공통
│       ├── llm_config.py   # 설정
│   ├── app.py              # 랭체인
│   ├── lcel.py             # LCEL 테스트
│   ├── app.py              # 랭체인 테스트
├── tests/                  # 테스트 코드 디렉터리
├── .env                    # 로컬 환경 변수 파일 (DB 비밀번호 등 보안 정보)
├── .gitignore              # 깃 제외 설정
├── README.md               # 프로젝트 설명서
└── pyproject.toml          # 현대적인 의존성 관리 및 프로젝트 설정 파일
```
---

## 📦 설정 및 실행 방법 (Configuration & Setup)
```
1) ollama OS에 맞는 버전 다운로드 후 실행
2) Python 가상환경 활성화
3) AI 모델 다운로드
    $ ollama pull llama3
    $ ollama pull gemma2    : (9b)다국어 능력이 뛰어나서 한글 답변 퀄리티가 매우 높음
    $ ollama pull gemma2:2b
    $ ollama pull call518/EEVE-8192ctx:10.8b-q4     : 야놀자 기반 - 커뮤니티 빌드
    $ ollama pull exaone3.5:2.4b    : LG AI 연구원 공식 - 초경량 가성비
4) pip 업그레이드
    $ pip install --upgrade pip
5) ollama 필수 패키지 설치
    $ pip install langchain langchain-ollama
6) ollama 목록 보기
    $ ollama list
    
############
# 기타 설정 #
############
1) ollama GUI > 모델 저장 경로 변경 및 재실행
2) Default 경로에 인증키 있어서 삭제 금지!
```

## 🛠 주요 라이브러리 (Dependencies)
```
프로젝트의 핵심 의존성 구성입니다.
```