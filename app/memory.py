from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from core.llm_config import get_llm
# 1. 기존 community 패키지 대신 langgraph 패키지 도입
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# 필요할 때 호출만 하면 항상 동일한 설정의 llm 객체가 생성됩니다.
llm = get_llm()

# 2. 프롬프트 템플릿 생성
# (LangGraph의 MessagesState를 사용할 때, 대화 기록 변수명은 'messages'로 지정하는 것이 표준입니다)
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="messages"),
    ("human", "{question}")
])

# 3. 기본 체인 생성 (프롬프트 | LLM)
base_chain = prompt | llm


# 4. LangGraph 노드(Node) 함수 정의
# 이 함수가 실행될 때 과거 대화 내역(state["messages"])이 자동으로 프롬프트에 주입됩니다.
def call_model(state: MessagesState):
    # 가장 최근에 들어온 유저의 질문을 추출합니다.
    user_question = state["messages"][-1].content

    # 기존 대화 기록(state["messages"][:-1])과 새 질문을 함께 체인에 전달합니다.
    response = base_chain.invoke({
        "messages": state["messages"][:-1],
        "question": user_question
    })

    # AI의 답변을 반환하면 자동으로 대화 기록(messages)에 누적 저장됩니다.
    return {"messages": response}


# 5. [핵심] 대화 흐름(Graph) 및 메모리 구조 정의
# 자바의 Map<String, ChatMessageHistory> 역할을 내장된 MemorySaver가 안전하게 대신합니다.
workflow = StateGraph(MessagesState)

# 노드 추가 및 시작점 연결
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

# 메모리(지속성) 레이어를 추가하여 컴파일
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# 6. 테스트 진행 (동일한 thread_id로 연속 질문)
# (LangGraph에서는 session_id 대신 thread_id라는 용어를 사용합니다)
config = {"configurable": {"thread_id": "user_session_123"}}

# 첫 번째 질문
# LangGraph는 메시지 객체 혹은 (역할, 내용) 튜플 형태의 리스트를 입력으로 받습니다.
response1 = app.invoke({"messages": [("user", "내 이름은 홍길동이야. 기억해줘!")]}, config=config)
print("AI 답변 1:", response1["messages"][-1].content)

print("-" * 30)

# 두 번째 질문 (이전 대화를 기억하는지 확인)
response2 = app.invoke({"messages": [("user", "내 이름이 뭐라고 했지?")]}, config=config)
print("AI 답변 2:", response2["messages"][-1].content)