# Import necessary module and function
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Define a function named text_to_doc_splitter that takes a string (text) as a parameter
def text_to_doc_splitter(text: str):
    # Create an instance of the RecursiveCharacterTextSplitter class with specified parameters
    spliiter = RecursiveCharacterTextSplitter(
        chunk_size=10000,  # The maximum size of each chunk of text
        chunk_overlap=0,   # The overlap between consecutive chunks
        length_function=len,  # A function to calculate the length of the text
        add_start_index=True,  # Whether to add a start index to each chunk
    )
    
    # Create a document by splitting the input text using the splitter
    document = spliiter.create_documents([text])
    
    # Return the resulting document
    return document



# Define a function named load_pdf that takes a PDF file path (pdf) as a parameter
def load_pdf(pdf):
    # Create a PdfReader object to read the PDF file
    pdf_reader = PdfReader(pdf)
    
    # Initialize an empty string to store the extracted text from the PDF
    text = ""
    
    # Iterate through each page in the PDF
    for page in pdf_reader.pages:
        # Extract the text content from the current page and append it to the 'text' variable
        text += page.extract_text()
    
    # Use the text_to_doc_splitter function to split the extracted text into a document
    document = text_to_doc_splitter(text)
    
    # Return the resulting document
    return document
