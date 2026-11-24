from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Ask a question
question = input("Enter your question: ")

print("\nThinking... Please wait.")

try:
    # Send question to OpenAI
    response = client.responses.create(
        model="gpt-4o-mini",
        input=question
    )

    # Print AI response
    print("\nAI Answer:")
    print(response.output_text)

except Exception as e:
    print("\nError occurred:")
    print(e)
