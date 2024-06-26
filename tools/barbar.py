from langchain.prompts.prompt import PromptTemplate
#from langchain.llms import LlamaCpp
from langchain_community.llms import LlamaCpp
from langchain.chains import ChatVectorDBChain
import pickle
import time


def get_chain(vectorstore):
    global qa_prompt
    llm =LlamaCpp(n_gpu_layers=12, model_path="./WizardLM-7B-uncensored.ggmlv3.q4_1.bin", temperature=0, n_ctx=2048, verbose=True, use_mlock=True)
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        combine_docs_chain_kwargs={'prompt': qa_prompt},
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain




if __name__ == "__main__":
    question = "When is the museum open"
    with open("vectorstore.pkl", "rb") as f:
        vectorstore = pickle.load(f)
    llm =LlamaCpp(model_path="./WizardLM-7B-uncensored.Q4_K_M.gguf", temperature=0, n_ctx=2048, verbose=False,  n_gpu_layers=-1)


    while True:
        print("Waiting for query>")
        question = input()
        start_time = time.time()
        docs = vectorstore.as_retriever(search_kwargs={"k":2}).get_relevant_documents(query=question)
#        print(f"We got {len(docs)} documents from the vectore store")
#        for doc in docs:
#            print(f'|{doc.page_content}|')
        prompt = """You are an assistant at the Ontario Regiment Museum in Oshawa Ontario. 
           If you don't know the answer, just say "I'm not sure." Don't try to make up an answer.
           Your name is Mary. Use the following pieces of context to answer the user's question. """

        for doc in docs:
            prompt = prompt + "\n" + doc.page_content
        prompt = prompt + f"\n### USER: {question}\n### ASSISTANT:"
    
#        print(f'prompt is |{prompt}|')
        resp = llm(prompt)
        print(f'({time.time()-start_time}) {resp}')
#    qa_chain = get_chain(vectorstore)
#    chat_history = []
#    print("Chat with your docs!")
#    while True:
#        print("Human:")
#        question = input()
#        result = qa_chain({"question": question, "chat_history": chat_history})
#        chat_history.append((question, result["answer"]))
#        print("AI:")
#        print(result["answer"])
