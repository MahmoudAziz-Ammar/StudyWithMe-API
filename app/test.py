from llm import ask_llm

context = """
Paris is the capital of France.
France is a country in Europe.
"""

question = "What is the capital of France?"

response = ask_llm(context, question)

print("ANSWER:")
print(response)