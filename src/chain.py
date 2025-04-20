import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load the prompt from file
def load_therapist_prompt():
    with open("prompts/therapist.txt", "r") as f:
        return f.read()

def create_chain():
    prompt = PromptTemplate(
        input_variables=["chat_history", "input"],
        template=load_therapist_prompt()
    )

    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )

    return chain
