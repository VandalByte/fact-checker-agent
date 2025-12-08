from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from .subagents.researcher_agent.agent import researcher_agent
from .subagents.secretary_agent.agent import secretary_agent

load_dotenv()

root_agent = SequentialAgent(
    name="FactCheckerAgent",
    description="A pipeline that verifies a claim or fact given by the user and saves the result.",
    sub_agents=[researcher_agent, secretary_agent],
)
