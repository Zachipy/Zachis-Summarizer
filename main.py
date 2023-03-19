import openai
openai.api_key = "YOUR API TOKEN"
userInput = input('Your text to summarize: ')
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Summarize this Text: " + userInput,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    ).choices[0].text
with open("output.txt", "w") as file:
    file.write(response)