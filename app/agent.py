from langchain.agents import create_react_agent, AgentExecutor
from .llm import get_llm
from .tools import get_tools
from .prompts import get_prompt

def build_agent():
    llm = get_llm()
    tools = get_tools()
    prompt = get_prompt()

    agent = create_react_agent(llm, tools, prompt)

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,   # CLEAN output (important for internship look)
        handle_parsing_errors=True
    )

    return executor


def run_agent(query: str):
    agent = build_agent()

    result = agent.invoke({
        "input": query
    })

    return result["output"]