from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(verbose=True)

memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat,
)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

chain = LLMChain(llm=chat, prompt=prompt, memory=memory, verbose=True)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
