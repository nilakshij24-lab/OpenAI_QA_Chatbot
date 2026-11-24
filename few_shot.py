from openai import OpenAI

client = OpenAI()

prompt = """
Example 1:
Question: What is HTML?
Answer: HTML is used to create web pages.

Example 2:
Question: What is CSS?
Answer: CSS is used to style web pages.

Example 3:
Question: What is JavaScript?
Answer: JavaScript adds interactivity to web pages.

Now answer:
Question: What is Python?
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

print("Few-Shot Response:")
print(response.output_text)
