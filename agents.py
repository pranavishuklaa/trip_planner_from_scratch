from crewai import Agent
from textwrap import dedent
# from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

"""
Goal: Create a 7-day tarvel itineary with detailed per-day plans, incluidng budget,
      packing suggestions, and safty tips 

    Captain/Manager/Boss:
       Expert Travel Agent

    Employees/ Experts to hire:
       City selection expert
       Local Tour guide 
"""


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. 
                            I've decades of expereince making travel itenaries """),
            goal=dedent(f""" Create a 7-day tarvel itineary with detailed per-day plans, incluidng budget,
      packing suggestions, and safty tips """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
             ],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert ata analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and traveler's interests """),
            tools=[SearchTools.search_internet,
                   CalculatorTools.calculate],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Provide the BEST insights about the selected city """),
            tools=[SearchTools.search_internet, 
               CalculatorTools.calculate],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )



