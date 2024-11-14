import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()



def main():
    model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature=0.2)
    prompt = ChatPromptTemplate.from_template("Generate a readme.md file for below given code in proper format to be used in github.\n Code: \n {code}")
    pipe = prompt | model | StrOutputParser()
    st.title("Generate Readme📜 for your code🌐")
    file = st.file_uploader("Upload your code file here 📥")

    if file is not None:
        content = file.read().decode()
        response = pipe.invoke({'code':str(content)})
        print(f"Response \n ------- \n {response}")
        st.markdown("---")
        st.subheader("Readme")
        st.code(response)

if __name__ == "__main__":
    main()