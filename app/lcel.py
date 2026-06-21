# LCEL (LangChain Expression Language)

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from core.llm_config import get_llm

# 필요할 때 호출만 하면 항상 동일한 설정의 llm 객체가 생성됩니다.
llm = get_llm()

# 2. 템플릿 생성 (가변 문자열 포맷 역할)
template = ChatPromptTemplate.from_template("{topic}에 대해 짧게 설명해줘.")

# 3. 파이프(|) 연산자로 템플릿과 LLM을 연결 (체이닝)
chain = template | llm

# 4. 실행 및 결과 출력
response = chain.invoke({"topic": "자바와 파이썬의 차이"})
print(response)