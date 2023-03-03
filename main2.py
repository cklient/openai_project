import openai
openai.api_key = "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"  # supply your API key however you choose

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
print(completion.choices[0].message.content)