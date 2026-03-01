from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a research consultant. Your goal is to help users refine their research queries "
    "to be as specific and useful as possible. Given a broad query, generate EXACTLY 3 "
    "clarifying questions that will help narrow down the scope and identify key areas of interest."
)

class RefinementQuestions(BaseModel):
    questions: list[str] = Field(description="A list of exactly 3 clarifying questions to refine the query.")

refinement_agent = Agent(
    name="RefineryAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=RefinementQuestions,
)
