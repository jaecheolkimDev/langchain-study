from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM  # 사용하는 라이브러리에 맞게 import

# 1. 서로 다른 모델 정의
model_fast = OllamaLLM(model="exaone3.5:2.4b")
model_reasoning = OllamaLLM(model="call518/EEVE-8192ctx:10.8b-q4")

# 2. 체인 구성 (예: 번역은 빠른 모델로, 분석은 좋은 모델로)
prompt1 = ChatPromptTemplate.from_template("{text}를 영어로 번역해줘.")
prompt2 = ChatPromptTemplate.from_template("다음 번역된 문장의 어색한 부분을 심층 분석해줘: {translated_text}")

# 3. 여러 모델을 파이프라인(|)으로 연결
translation_chain = prompt1 | model_fast | StrOutputParser()
analysis_chain = prompt2 | model_reasoning | StrOutputParser()

# 전체 워크플로우 연결
final_chain = {"translated_text": translation_chain} | analysis_chain

# ================= 4. 출력 및 실행 부분 추가 =================

# 테스트할 원문 텍스트
input_text = "오늘 날씨가 너무 좋아서 나가서 가볍게 뛰고 싶다."

print("체인 실행 중... (잠시만 기다려주세요)\n")

# .invoke() 메서드로 체인을 실행합니다.
# prompt1이 {text}를 요구하므로 key 이름을 'text'로 지정합니다.
response = final_chain.invoke({"text": input_text})

print("=== [최종 분석 결과] ===")
print(response)