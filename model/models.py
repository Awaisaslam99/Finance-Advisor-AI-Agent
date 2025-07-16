from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

def get_web_search_agent_config():
    return {
        "name": "Web Search Agent",
        "role": "Search the web for the information",
        "model": Groq(id="llama3-groq-70b-8192-tool-use-preview"),
        "tools": [DuckDuckGo()],
        "instructions": ["Always include sources"],
        "show_tool_calls": True,
        "markdown": True,
    }

def get_finance_agent_config():
    return {
        "name": "Finance AI Agent",
        "model": Groq(id="llama3-groq-70b-8192-tool-use-preview"),
        "tools": [
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True
            )
        ],
        "instructions": ["Use tables to display the data"],
        "show_tool_calls": True,
        "markdown": True,
    }
