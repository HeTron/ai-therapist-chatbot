import os
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate


def load_therapist_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "therapist.txt")
    with open(prompt_path, "r") as f:
        return f.read()


def create_chain() -> ConversationChain:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY is not set. Add it to your .env file or Streamlit secrets."
        )

    prompt = PromptTemplate(
        input_variables=["chat_history", "input"],
        template=load_therapist_prompt(),
    )

    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-4o-mini",
        openai_api_key=api_key,
    )

    # return_messages=False keeps memory as a plain string, compatible with PromptTemplate
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=False,
    )

    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False,
    )

    return chain
