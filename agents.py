from google.adk import Agent
from sub_agents.flight_agent import flight_agent
from sub_agents.hotel import hotel_agent
from datetime import datetime, timedelta

coordinator_agent = Aent(
    name = "travel_coordinator",
    model = "gemini-2.0-flash-exp",
    description = "main coordinator agent gathers travel preferences and query sub-agents"
     
)