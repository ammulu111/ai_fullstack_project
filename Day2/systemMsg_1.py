import ollama
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role": "system",
            "content": "Give answer for 3rd class student in 2 lines"
        },
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)
print(response["message"]["content"])