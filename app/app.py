# langchain_ollama 패키지에서 OllamaLLM이라는 클래스를 가져옵니다.
from langchain_ollama import OllamaLLM

# 1. Ollama에 설치한 llama3 모델 불러오기
# 파이썬은 new 키워드가 없고, 타입 추론이 기본이라 좌변에 자료형을 쓰지 않습니다.
# 로컬 컴퓨터에 설치된 Ollama 프로그램 안의 llama3 모델을 사용하는 AI 객체(llm)를 생성합니다.
llm = OllamaLLM(model="llama3")

# 2. AI에게 질문 던지기
response = llm.invoke("왜 하늘은 파랗지? 한 문장으로 답해줘.")

# AI가 생성한 답변(문자열)을 콘솔 창에 출력합니다.
print(response)