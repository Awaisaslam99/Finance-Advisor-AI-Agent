from phi.agent import Agent
from model.models import get_web_search_agent_config, get_finance_agent_config

def initialize_agents():
    web_search_agent = Agent(**get_web_search_agent_config())
    finance_agent = Agent(**get_finance_agent_config())

    multi_ai_agent = Agent(
        team=[web_search_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display the data"],
        show_tool_calls=True,
        markdown=True,
    )

    return multi_ai_agent
