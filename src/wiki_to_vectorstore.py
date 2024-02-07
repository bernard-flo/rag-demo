import dotenv

from langchain_community.document_loaders.generic import GenericLoader

import langchain_extensions.language_parser_extension
from langchain.text_splitter import RecursiveCharacterTextSplitter

from vectorstore import get_vectorstore

dotenv.load_dotenv()

wiki_path = "./wiki"

# Load
loader = GenericLoader.from_filesystem(
    wiki_path,
    glob="**/*",
    suffixes=[".txt"],
)
documents = loader.load()
print(f"Documents: {len(documents)}")

# Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(documents)
print(f"Splits: {len(splits)}")

# Store
db = get_vectorstore()
db.add_documents(splits)
