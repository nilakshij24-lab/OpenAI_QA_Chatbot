from openai import OpenAI

# Create OpenAI client
client = OpenAI()

print("Welcome to OpenAI Q&A Chatbot!")
print("Ask me anything.")
print("Type 'bye' to exit.")

# Keep chatbot running
while True:

    # Get question from user
    question = input("\nYou: ")

    # Exit condition
    if question.lower() == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    try:
        # Send question to GPT
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions="You are a helpful assistant. Answer questions in simple and clear language.",
            input=question
        )

        # Display AI response
        print("\nAI Answer:")
        print(response.output_text)

    except Exception as e:
        print("Error:", e)
