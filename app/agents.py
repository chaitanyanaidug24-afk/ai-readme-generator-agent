from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from app.config import GOOGLE_API_KEY
from app.tools import calculator

tools=[calculator]
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant for whether info",
)

chain = prompt | llm

def run_genai(question: str) -> str:
    response = chain.invoke({"question": question})
    return response.content

# Run the agent
def run_agent2(question: str) -> str:
    result = agent.invoke(
    {"messages": [{"role": "user", "content": question}]}
    )
    return result['messages'][-1].content