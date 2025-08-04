from langchain.agents import AgentExecutor, create_tool_calling_agent
from calculator_tool import get_calculator
from weather_tool import get_weather
from wikipedia_tool import get_wikipedia
from file_tool import get_file
from csv_tool import get_csv_stats
from sqlite_tool import get_sqlite
from whatsapp_tool import get_whatsapp_message
from llm_setup  import llm , prompt

tools = [get_calculator,get_weather,get_wikipedia,get_file,get_sqlite,get_csv_stats,get_whatsapp_message]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
   
)

agent_executor= AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose= True # by enabling verbose , you can see the thought process of agent intermediate result
    )