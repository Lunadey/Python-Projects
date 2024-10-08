import google.generativeai as genai
import os

# Set API Key (from environmental variable) and model
genai.configure(api_key=os.environ['GeminiAPI Key'])
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_blog(topic):
    # Generate a blog post about given topic with 400 tokens
    response = model.generate_content(
        topic,
        generation_config = genai.GenerationConfig(
            max_output_tokens=400,
            temperature=0.3,
        )
    )
    # Get blog text
    return response.text

# Output generated blog post
print(generate_blog(str(input("Enter a blog topic: "))))
