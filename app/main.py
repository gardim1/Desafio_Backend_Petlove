from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import QuestionRequest, AnswerResponse
from app.config import get_settings
from openai import OpenAI

settings = get_settings()

client = OpenAI(api_key=settings.OPENAI_API_KEY)

app = FastAPI(
    title="Petlove AI Assistant",
    description="API de assistente de vendas para o e-commerce Petlove.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/question-and-answer", response_model=AnswerResponse, status_code=status.HTTP_200_OK)
async def question_and_answer(payload: QuestionRequest):
    try:
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente de vendas da Petlove. "
                        "Forneça respostas objetivas, empáticas e recheadas "
                        "de informações veterinárias confiáveis sobre produtos pet. "
                        "Cite sempre 3 opções de produtos relevantes da Petlove."
                    ),
                },
                {"role": "user", "content": payload.question},
            ],
            temperature=settings.TEMPERATURE,
        )
        answer = response.choices[0].message.content.strip()
        return AnswerResponse(response=answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
