import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_learning_plan(goal, hours, level):
    prompt = f"""
You are an AI mentor. Create a personalized 4-week learning path for the goal: "{goal}".
The user is at a {level} level and can spend {hours} hours per week.
Break the plan into weekly tasks with topics and estimated hours. Use markdown formatting.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message["content"]