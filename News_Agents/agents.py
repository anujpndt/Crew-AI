from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

# Use LangChain's Google Gemini integration directly
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

# Creating a senior researcher agent
news_researcher = Agent(
    name="Senior Researcher",
    role="Research cutting-edge technologies",
    goal="Uncover groundbreaking technologies in {topic}",
    llm=gemini_llm,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    memory=True,
    verbose=True,
    allow_delegation=True
)

# Creating a writer agent
news_writer = Agent(
    name="News Writer",
    role="Transform research into engaging blog posts",
    goal="Write a news blog about the latest technology {topic}",
    llm=gemini_llm,
    backstory=(
        "As a seasoned writer, you have a knack for transforming complex "
        "ideas into engaging narratives that captivate readers."
    ),
    tools=[tool],
    memory=True,
    verbose=True,
    allow_delegation=False
)