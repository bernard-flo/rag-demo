import chromadb.config
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def get_vectorstore():
    return Chroma(
        embedding_function=OpenAIEmbeddings(disallowed_special=()),
        client_settings=chromadb.config.Settings(
            anonymized_telemetry=False,
            is_persistent=True,
        ))
