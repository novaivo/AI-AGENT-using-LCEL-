import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder



load_dotenv()
my_apikey = os.getenv("openrouter_API_KEY")


def get_llm():
    try:
           return ChatOpenAI(
           model="meta-llama/llama-3-8b-instruct",
            base_url="https://openrouter.ai/api/v1",
           api_key=my_apikey,
           temperature=0.7
    )
    except Exception as e:
      print(f"Sorry! I'm having trouble thinking right now. Error: {str(e)}")
      return None
llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ( "system", 
     """ you are an intelligent, tool_using ai assistant .
     when user asks a question , think step by step, decide if a tool is needed , and use the best one .
     you have access to tools like calculator,wikipedia,weather,file reader.

    - For math, use the calculator.
    - For weather queries, use the weather tool.
    - For factual questions, use the Wikipedia tool.
    - For file-related queries, use the file tool.
     always explain what you are doing im simple human language in freindly way after using tool., give user a clean final answer.
     
"""   
    ),
    ("human","{input}"),
     MessagesPlaceholder(variable_name="agent_scratchpad")


])
