# Petlove AI Assistant API

Assistente de vendas inteligente para os usuários do e-commerce da **Petlove**, integrado com a API da OpenAI.


## Rodando localmente (Windows)

```bash
git clone https://github.com/gardim1/Desafio_Backend_Petlove
cd Desafio_Backend_Petlove

copy .env.example .env  # preencha sua OPENAI_API_KEY, OPENAI_MODEL e TEMPERATURE

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

> Acesse em [http://localhost:8000/docs](http://localhost:8000/docs) para a documentação interativa via Swagger.

---

## Endpoint

**POST** `/api/question-and-answer`

### Request
```json
{
  "question": "qual a melhor ração para golden?"
}
```

### Response
```json
{
  "response": "Escolher a melhor ração para um Golden Retriever envolve considerar..."
}
```

---

## Arquivo `.env`

Exemplo do conteúdo:

```env
OPENAI_API_KEY=sk-xxxxx
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0.2
```
