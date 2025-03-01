import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os



# Check if the GOOGLE_API_KEY environment variable is set
if "GOOGLE_API_KEY" not in os.environ:
    st.error("Please set the GOOGLE_API_KEY environment variable with your Google AI API key before running this app.")
    st.stop()

system_prompt = """
You are an expert AI code reviewer, dedicated to helping developers write better code. Your task is to thoroughly review the provided code for common mistakes, bugs, performance issues, and adherence to best practices. Identify any problems and suggest improvements with clear explanations and code snippets.

Please format your response using markdown, with code snippets enclosed in triple backticks (```). Structure your feedback with headings for each issue found, followed by a detailed explanation and the suggested fix.

For example:

### Issue 1: [Brief description]
**Explanation:** [Why is this a problem?]
**Suggested Fix:**
```[language]
[Corrected code snippet]
```

The code to review will be provided in the {code} placeholder. Aim for a balanced response that is detailed enough to be helpful but concise enough to be easily digestible.

Code to review:
```{code}```
"""

# Define the prompt template for code review
prompt = PromptTemplate(
    input_variables=["code"],
    template=system_prompt
)

# Initialize the Gemini model from Google AI Studio via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Create a chain combining the prompt and the language model
chain = prompt | llm

# Streamlit app interface
st.title("AI Code Reviewer")

# Display instructions for the user
st.write("Paste your code below and click 'Review Code' to get feedback from the AI.")

# Text area for user to input their  code
code = st.text_area(" Code:", height=300)

# Button to trigger the code review
if st.button("Review Code"):
    if code.strip() == "":
        st.warning("Please enter some code to review.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                # Send the code to the AI model and get the response
                response = chain.invoke({"code": code})
                # Display the review results
                st.subheader("Review Results")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"An error occurred while analyzing the code: {e}")