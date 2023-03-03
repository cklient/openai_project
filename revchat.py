from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "cklientt@gmail.com",
  "password": "xf168199"
})

for data in chatbot.ask(
  "prompt",
  conversation_id=chatbot.config.get("conversation"),
  parent_id=chatbot.config.get("parent_id"),
):
  print(data["message"], end="", flush = True)
print()