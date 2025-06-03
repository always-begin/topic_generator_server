from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, LangChain!"}

llm = ChatOpenAI(model="gpt-3.5-turbo")  # 또는 gpt-3.5-turbo
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    response = llm([HumanMessage(content=user_input)])
    return {"response": response.content}