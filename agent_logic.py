from langchain.agents import AgentExecutor, create_tool_calling_agent
from calculator_tool import get_calculator
from weather_tool import get_weather
from wikipedia_tool import get_wikipedia
from file_tool import get_file
from llm_setup  import llm , prompt

tools = [get_calculator,get_weather,get_wikipedia,get_file]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
   
)

agent_executor= AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose= True
    )