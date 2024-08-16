import tiktoken

# Define your prompt with question
prompt = "OpenAI ChatGPT is very Good."

# Load an encoding
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Turn text into tokens
text_to_token = encoding.encode(prompt)
print(str(text_to_token))

# Print Number of Tokens in text
num_tokens = len(encoding.encode(prompt))
print(str(num_tokens))

# Turn tokens into text
token_to_text = encoding.decode([5109, 15836, 13149, 38, 2898, 374, 1633, 7839, 13])
print(str(token_to_text))
