from google import genai
import os

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Tell me a quick joke about AI.'
)
print(response.text)
