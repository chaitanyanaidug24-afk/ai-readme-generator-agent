from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.agents import run_genai,run_agent2

app = FastAPI(title="LangChain Gemini Agent Tutorial")

@app.post("/genai/chat", response_model=ChatResponse)
def chat_with_agent(payload: ChatRequest):
    answer = run_genai(payload.question)
    return ChatResponse(answer=answer)


@app.post("/genai/agent", response_model=ChatResponse)
def chat_with_agent(payload: ChatRequest):
    answer = run_agent2(payload.question)
    return ChatResponse(answer=answer)
