from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    question: str = Field(..., example="Qual a melhor ração para golden?")

class AnswerResponse(BaseModel):
    response: str
