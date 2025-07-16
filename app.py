from dotenv import load_dotenv
import openai
import os

from controller.agent_controller import initialize_agents

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

agent = initialize_agents()
agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)

