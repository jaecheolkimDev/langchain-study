from core.llm_config import get_llm

# 필요할 때 호출만 하면 항상 동일한 설정의 llm 객체가 생성됩니다.
llm = get_llm()

# 2. AI에게 질문 던지기
response = llm.invoke("왜 하늘은 파랗지? 한 문장으로 답해줘.")

# AI가 생성한 답변(문자열)을 콘솔 창에 출력합니다.
print(response)