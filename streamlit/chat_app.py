import streamlit as st
from langchain_groq import ChatGroq
from langchain import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.chat_message_histories import (StreamlitChatMessageHistory,)
from langchain_core.runnables.history import RunnableWithMessageHistory

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="langchain Chat App", page_icon="🦜")

st.title("🦜 Chat app")
#  Langchain
st.write("welcome to the chat app😍")


models= ["gemma-7b-it","gemma2-9b-it","llama-3.1-8b-instant","llama3-8b-8192","mixtral-8x7b-32768"]

cols=st.columns(2)

with cols[0]:
    model=st.selectbox(label="**LLM Models**", options=models, index=3)


with cols[1]:
    temperature=st.slider(label="**temperature**",
                          min_value=0.0,
                          max_value=2.0,
                          value=1.0,
                          step=0.01)
    
clicked=st.button("clear History")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a assistant that answer history related questions accurately"),
        ("placeholder","{chat_history}"), 
        ("user","{query}"),
    ]
)
llm=ChatGroq(model=model,temperature=temperature)

chain=prompt|llm|StrOutputParser()

msgs=StreamlitChatMessageHistory()
if len(msgs.messages) == 0 or clicked:
    msgs.clear()
    msgs.add_ai_message(chain.invoke(
        {"query":"write a short welcome message",
         "chat_history":[]}
    ))

chain_with_history= RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="query",
    history_messages_key="chat_history",
)

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

chat_input=st.chat_input("Ask me anything")

if chat_input:
    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"query": chat_input}, config)
    st.chat_message("user").write(chat_input)
    st.chat_message("ai").write(response)
    with st.expander("view chat history"):
        # st.write(msg.messages)
        for i, msg in enumerate(msgs.messages):
            st.write(f"{i}. {msg.type.upper()}: {msg.content}")

    st.write(llm.model_name)



