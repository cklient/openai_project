import sys

from revChatGPT.V2 import Chatbot
import streamlit as st

email = st.secrets["email"]
password = st.secrets["password"]

async def generate_answer(question):
    chatbot = Chatbot(email=email, password=password)
    #await chatbot.ask("Hello")
    result = ""
    async for line in chatbot.ask(question):
        #print(line["choices"][0]["text"].replace("<|im_end|>", ""), end="")
        tmp = line["choices"][0]["text"].replace("<|im_end|>", "")
        result = result+tmp
        sys.stdout.flush()
    #print()
    #print(response["choices"][0]["text"])
    print(result)
    return result
async def main():
    st.title("chatGPT 问答机器人")
    model = "text-davinci-003"
    question = st.text_area("输入你的问题")
    if st.button("提交"):
        answer = await generate_answer(question)
        st.write("Answer:", answer)
        if st.button("Download"):
            st.success("Answer saved to your device!")
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    #main()

    #tasks=[main()]
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.wait(tasks))