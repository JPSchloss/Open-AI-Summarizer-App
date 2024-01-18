from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA 
import os
from pdf_reader import load_pdf
from langchain.text_splitter import CharacterTextSplitter


# Define a function named split_text_documents that takes a list of text documents (docs) as a parameter
def split_text_documents(docs: list):
    # Create an instance of the CharacterTextSplitter class with specified parameters
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,  # The maximum size of each chunk of text
        chunk_overlap=20   # The overlap between consecutive chunks
    )
    
    # Split the input list of text documents into smaller chunks using the text splitter
    documents = text_splitter.split_documents(docs)
    
    # Return the resulting list of split documents
    return documents


def get_summary(pdf, model, openai_api_key):
    
    # Loading The PDF Document
    pdf_doc = load_pdf(pdf)

    # Splitting The Documents For Processing
    documents = split_text_documents(pdf_doc)

    # Building a Vector DB For The Documents
    vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(openai_api_key = openai_api_key))

    # Initializing the ChatGPT Model.
    llm = ChatOpenAI(temperature=0.3, model_name=model, openai_api_key = openai_api_key)

    # Creating a RetrivalIQA model combining the langauge model and vector database. 
    pdf_qa = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(search_kwargs={'k': 4}),
        chain_type="stuff",
    )

    # Defining the Query. 
    query = """ Write a summary for the document passed to you. You are getting a PDF document and your job \
        is to interpret the information in the document and to provide a summary. This summary should highlight \
        key points and identify the main takeaways from the document. If there are important names, dates, events, \
        facts, etc. please try to keep those in your summary. Do not make up information or facts. The returned \
        summary should be a few paragraphs. 
                """
    
    # Executing the RetreivalIQA model with the defined query. 
    result = pdf_qa.run(query)

    return result


