import sys
import openai
import streamlit as st

email = st.secrets["email"]
password = st.secrets["password"]
openai.api_key = st.secrets["api_key"]
async def generate_answer(question):

    #await chatbot.ask("Hello")
    result = ""

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": question}])
    print(completion.choices[0].message.content)
    result = completion.choices[0].message.content
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