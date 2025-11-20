# Reasoning engine
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


@tool
def tripleFloat(num:float) -> float:
    """ Triple the input float number and return the result """
    return float(num) * 3

tools = [TavilySearch(max_results=1),tripleFloat]

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0).bind_tools(tools)


