from langchain.text_splitter import Language
from langchain_community.document_loaders.parsers.language import language_parser

from langchain_extensions.java_segmenter import JavaSegmenter

language_parser.LANGUAGE_EXTENSIONS["java"] = Language.JAVA
language_parser.LANGUAGE_SEGMENTERS[Language.JAVA] = JavaSegmenter
