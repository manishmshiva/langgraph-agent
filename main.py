import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END

from nodes import agent_reasoning_node, tool_node

AGENT_REASON = "agent_reason"
ACT="act"
LAST = -1

def should_continue(state:MessagesState) -> str:
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)
flow.set_entry_point(AGENT_REASON)
flow.add_node(AGENT_REASON, agent_reasoning_node)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASON,should_continue,{END:END,ACT:ACT})
flow.add_edge(ACT,AGENT_REASON)

app = flow.compile()
png_bytes = app.get_graph().draw_mermaid_png()

with open("flow.png", "wb") as f:
    f.write(png_bytes)

if __name__ == "__main__":
    print("Hello react langgraph with function calling...")