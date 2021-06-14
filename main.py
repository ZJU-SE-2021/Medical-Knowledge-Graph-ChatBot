from fastapi import FastAPI

from chatbot_graph import ChatBotGraph

handler = ChatBotGraph()
app = FastAPI()


@app.get("/api/chatterbot")
async def read_item(question: str = ''):
    if question == '' or question.isspace():
        answer = '...'
    else:
        answer = handler.chat_main(question)
    return {'answer': answer}
