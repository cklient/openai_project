import openai
import streamlit as st

# Replace YOUR_OPENAI_API_KEY with your OpenAI API key
#st.write("api_key:", st.secrets["api_key"])
openai.api_key = st.secrets["api_key"]

def generate_answer(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def main():
    st.title("GPT-3 based Question Answering")
    model = "text-davinci-003"
    question = st.text_input("Ask your question")
    if st.button("Submit"):
        answer = generate_answer(model, question)
        st.write("Answer:", answer)
        if st.button("Download"):
            st.success("Answer saved to your device!")

if __name__ == '__main__':
    main()