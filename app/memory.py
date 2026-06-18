from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 1. LLM 객체 생성
llm = OllamaLLM(model="llama3")

# 2. 프롬프트 템플릿 생성 (과거 대화 내역이 들어갈 공간인 MessagesPlaceholder가 추가됨)
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="history"), # 자바의 List<Message> 자리를 비워두는 것과 같음
    ("human", "{question}")
])

# 3. 기본 체인 생성 (프롬프트 | LLM)
base_chain = prompt | llm

# 4. 세션별로 대화 내역(메모리)을 저장할 딕셔너리 (자바의 Map<String, ChatMessageHistory> 역할)
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 5. [핵심] 기존 체인에 메모리 관리 기능을 래핑(Wrapping)
with_history_chain = RunnableWithMessageHistory(
    base_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# 6. 테스트 진행 (동일한 session_id로 연속 질문)
config = {"configurable": {"session_id": "user_session_123"}}

# 첫 번째 질문
response1 = with_history_chain.invoke({"question": "내 이름은 홍길동이야. 기억해줘!"}, config=config)
print("AI 답변 1:", response1)

# 두 번째 질문 (이전 대화를 기억하는지 확인)
response2 = with_history_chain.invoke({"question": "내 이름이 뭐라고 했지?"}, config=config)
print("AI 답변 2:", response2)