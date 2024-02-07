import logging

import dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI

from vectorstore import get_vectorstore


logging.basicConfig(level=logging.CRITICAL)

dotenv.load_dotenv()

# RetrievalQA
db = get_vectorstore()
retriever = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)

# Chat
llm = ChatOpenAI(model_name="gpt-4")
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)


def ask_loop():
    while True:
        question = input("> ")
        result = qa.invoke({"question": question})
        print(result["answer"])


def ask_once(question):
    print("> " + question)
    print()
    result = qa.invoke({"question": question})
    print(result["answer"])


ask_once("T멤버십과 관련된 코드에 대해 알려주세요")
ask_once("그렇다면 정책에 맞는 코드를 알려주세요")
