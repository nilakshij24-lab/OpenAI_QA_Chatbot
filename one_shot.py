from openai import OpenAI

client = OpenAI()

prompt = """
Example:
Question: What is Java?
Answer: Java is a programming language.

Now answer this question:
Question: What is Python?
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

print("One-Shot Response:")
print(response.output_text)
