import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

# from langchain import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


#----------------------- Load Documents ------------------------------------
def get_pdf_text(pdf_docs):
    text = ""
    pdf_reader = PdfReader(pdf_docs)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def create_docs(pdf_list, unique_id):
    docs = []
    for filename in pdf_list:
        chunks = get_pdf_text(filename)
        docs.append(Document(
            page_content=chunks,
            metadata={"name":filename.name, 
                      "id":filename.file_id,
                      "type":filename.type, 
                      "size":filename.size,
                      "unique_id":unique_id}))
    return docs

def load_docs(directory="Docs/"):
    loader = PyPDFDirectoryLoader(directory)
    documents = loader.load()
    return documents

def get_load_docs(pdfs):
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


#---------------Transform(Split) Documents -----------------------------
def split_docs(documents, chunk_size=2000, chunk_overlap=250):
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n", "\n\n","\n\n\n"], chunk_size=chunk_size, chunk_overlap=chunk_overlap) # Break large documents in few chunks
    docs = text_splitter.split_documents(documents=documents)
    # docs = text_splitter.split_text(document_in_text_formatat)
    # chunks = text_splitter.create_documents(docs)
    return docs


def get_embeddings(OPENAI_API_KEY):
    load_dotenv()
    # embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl") 
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return embeddings

def get_vectorstore(documents, embeddings):
    return Chroma.from_documents(documents=documents, embedding=embeddings)

def get_similar_docs(db, query, k=2):
    return db.similarity_search(query, k=k)

def get_chain(OPENAI_API_KEY):
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    # llm = HuggingFaceHub(repo_id="bigscience/bloom",model_kwargs={"temperature":1e-10})
    # llm = HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0.9})

    # template = """Você é um assertivo assistente virtual do banco AngolaBank. Seu nome é LOBITO. Use as informações dadas no contexto para responder à pergunta no final. Responda sempre de modo assertivo e formal. Se você não sabe ou não encontrar a resposta a pergunta, apenas diga que não encontrou a resposta e peça que o cliente formule a pergunta de outra maneira, não tente inventar uma resposta. Após cada resposta pergunte sempre se deseja saber mais alguma coisa.
    #     {context}
    #     {chat_history}
    #     Questão: {question}
    #     Resposta útil:
    # """
    template = """Você é um assertivo assistente virtual do banco AngolaBank. Um consultor bancário, seu nome é LOBITO. 
        Use as informações dadas no contexto para responder à pergunta no final do modo mais completo e detalhado possível.
        Responda sempre de modo formal.
        Faça cálculos, forneça informações, dê conselhos, avise, raciocine, seja um consultor, ajudando o usuário no que ele precisar saber. 
        Se você não sabe ou não encontrar a resposta a pergunta, apenas diga que não encontrou a resposta e peça que o cliente formule a pergunta de outra maneira, não tente inventar uma resposta. 
        Após cada resposta pergunte sempre se deseja saber mais alguma coisa.
        {context}
        {chat_history}
        Questão: {question}
        Resposta útil:
    """
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "chat_history", "question"], 
        template=template
    )
    return load_qa_chain(
        llm=OpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-instruct"), 
        chain_type="stuff",
        memory=ConversationBufferMemory(memory_key="chat_history", input_key="question"), 
        prompt=QA_CHAIN_PROMPT
    )

def get_answer(chain,query, relevant_docs):
    response = chain.invoke({"input_documents":relevant_docs, "question":query}, return_only_outputs=True)["output_text"]
    # print(chain.memory.buffer)
    return response

if __name__== '__main__':
    load_dotenv()
    directory = 'Docs/'
    OPENAI_API_KEY=str(os.getenv('OPENAI_API_KEY'))
    
    documents = load_docs(directory)
    print(f"Num docs(pages):{len(documents)}")

    docs = split_docs(documents)
    embeddings = get_embeddings()
    db = get_vectorstore(documents=docs, embeddings=embeddings)
    chain = get_chain()

    try:
        while True:
            our_query = input("O que deseja saber:")
            if our_query.lower() == 'exit':
                raise KeyboardInterrupt("saindo")
            
            relevant_docs = get_similar_docs(db=db, query=our_query)
            # print(f"Documentos Base da resposta:{relevant_docs}")
            answer = get_answer(chain=chain,query=our_query, relevant_docs=relevant_docs)
            print(answer)
            # print(f"Resposta:{answer}")
    except KeyboardInterrupt:
        print("\n\n")
        print("Saindo e finalizando o programa!")

