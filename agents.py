from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGroq(
        model="llama3-70b-8192",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )


def create_content_agent():
    return Agent(
        role="Content Generator",
        goal="Generate high-quality blog content based on user inputs",
        backstory="Expert content writer specialized in AI and business topics",
        llm=get_llm(),
        verbose=True
    )