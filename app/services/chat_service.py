import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

def process_chat(message: str) -> str:
    response = llm.invoke([HumanMessage(content=message)])
    return response.content
