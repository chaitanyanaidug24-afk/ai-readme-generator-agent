from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.agents import run_genai,run_agent2
from app.models import ReadmeRequest
from app.agents import generate_readme_from_folder
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="LangChain Gemini Agent Tutorial")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for hackathon
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/genai/chat", response_model=ChatResponse)
def chat_with_agent(payload: ChatRequest):
    answer = run_genai(payload.question)
    return ChatResponse(answer=answer)


@app.post("/genai/agent", response_model=ChatResponse)
def chat_with_agent(payload: ChatRequest):
    answer = run_agent2(payload.question)
    return ChatResponse(answer=answer)

@app.post("/genai/readme")
def generate_readme(request: ReadmeRequest):
    result = generate_readme_from_folder(request.folder_path)

    return Response(
        content=result,
        media_type="text/markdown",
        headers={
            "Content-Disposition": "attachment; filename=README.md"
        }
    )


