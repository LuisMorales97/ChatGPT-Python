import openai

# Setup API Key
openai.api_key = 'Insert Key'

# Define model to Use
model_engine = 'text-davinci-002'

# Promp for the model
# prompt = "What is the capital of the USA?"
prompt = input('What is your question?: \n')

# Generate response from model
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

# Get the generate response
message = response['choices'][0]['text']
print(message)