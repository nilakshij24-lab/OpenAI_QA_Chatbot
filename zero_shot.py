from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Explain Python programming in simple words."
)

print("Zero-Shot Response:")
print(response.output_text)
