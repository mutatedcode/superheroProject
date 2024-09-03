from langchain.agents import AgentType
from langchain.agents import create_pandas_dataframe_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
import pandas as pd
import streamlit as st
from ai import get_api_key

api_key = get_api_key

st_cb = StreamlitCallbackHandler
data = pd.read_csv("https://raw.githubusercontent.com/mutatedcode/superheroProject/main/superheroes_nlp_dataset.csv")

llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=api_key, streaming=True
    )

pandas_df_agent = create_pandas_dataframe_agent(
llm,
data,
verbose=True,
agent_type=AgentType.OPENAI_FUNCTIONS,
handle_parsing_errors=True,
    )

response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])