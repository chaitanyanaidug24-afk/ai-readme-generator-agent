from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

class ReadmeRequest(BaseModel):
    folder_path: str
