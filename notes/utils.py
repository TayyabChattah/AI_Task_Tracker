import google.generativeai as genai  
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model=genai.GenerativeModel("gemini-2.0-flash-exp")

def get_category(title,description):
    prompt = f"""Classify this task into one of the categories: Work, Personal, Study, Health, Shopping, Finance, Other.

Task Name: {title}
Task Description: {description}
Only return the category name as one word (e.g., Work, Study, etc.)"""

    response=model.generate_content(prompt)
    category=response.text.strip()
    return category
