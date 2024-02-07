import dotenv

from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser

import langchain_extensions.language_parser_extension
from langchain.text_splitter import RecursiveCharacterTextSplitter

from vectorstore import get_vectorstore


dotenv.load_dotenv()

repo_path = "./repo"

# Load
loader = GenericLoader.from_filesystem(
    repo_path,
    glob="**/*",
    suffixes=[".java"],
    parser=LanguageParser(language=Language.JAVA, parser_threshold=500),
)
documents = loader.load()
print(f"Documents: {len(documents)}")

# Splitting
java_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JAVA, chunk_size=2000, chunk_overlap=200
)
splits = java_splitter.split_documents(documents)
print(f"Splits: {len(splits)}")

# Store
db = get_vectorstore()
db.add_documents(splits)
