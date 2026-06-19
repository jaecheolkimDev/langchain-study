import os
from dotenv import load_dotenv
# langchain_ollama 패키지에서 OllamaLLM이라는 클래스를 가져옵니다.
from langchain_ollama import OllamaLLM  # 사용하는 라이브러리에 맞게 import

# .env 파일 로드
load_dotenv()

def get_llm():
    #
    # Ollama에 설치한 모델 불러오기
    # 파이썬은 new 키워드가 없고, 타입 추론이 기본이라 좌변에 자료형을 쓰지 않습니다.
    # .env에서 모델명을 가져오고, 없으면 기본값 사용하는 AI 객체(llm)를 생성합니다.
    model_name = os.getenv("LLM_MODEL_NAME", "exaone3.5:2.4b")
    return OllamaLLM(model=model_name)