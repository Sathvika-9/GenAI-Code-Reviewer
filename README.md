# AI Code Reviewer with Streamlit and LangChain

This project is an AI-powered code reviewer built with Streamlit for an intuitive user interface and LangChain integrated with Google AI Studio for intelligent code analysis. It allows users to submit Python code and receive detailed feedback on potential bugs, errors, or suggestions for improvement, complete with code snippets for fixes.

## Features

- User-friendly web interface for submitting code
- AI-driven analysis powered by Google's Gemini Pro model
- Detailed feedback with explanations and suggested fixes
- Easy setup and local deployment

## Prerequisites

Before setting up the project, ensure you have the following:

- **Python 3.8 or higher** installed on your system
- A **Google AI Studio account** to obtain an API key

## Setup Instructions

Follow these steps to set up the project locally:

1. **Obtain an API Key**  
   - Sign up at [Google AI Studio](https://makersuite.google.com/) and create a project.  
   - Generate an API key for the Gemini API.

2. **Set the Environment Variable**  
   - Store your API key securely as an environment variable named `GOOGLE_API_KEY`:  
     - On Unix-based systems (Linux/macOS):  
       ```bash
       export GOOGLE_API_KEY="your_api_key_here"
       ```  
     - On Windows:  
       ```bash
       set GOOGLE_API_KEY="your_api_key_here"
       ```

3. **Install Required Packages**  
   - Install the necessary Python packages using pip:  
     ```bash
     pip install streamlit langchain-google-genai
     ```

## Running the App

Once the setup is complete, follow these steps to run the application:

1. Save the project code in a file, e.g., `app.py`.  
2. Open a terminal in the project directory and run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```  
3. Your default web browser will automatically open to the app’s interface (typically at `http://localhost:8501`).

## Usage

Here’s how to use the AI Code Reviewer:

1. **Paste Your Code**: In the app’s text area, enter the Python code you want reviewed.  
2. **Review the Code**: Click the "Review Code" button.  
3. **View Feedback**: The AI will analyze your code and display feedback in markdown format, including explanations and suggested fixes with code snippets.

### Example

**Input Code:**  
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n)
```

**Expected Output:**  
```
### Issue 1: Infinite Recursion
**Explanation:** The recursive call `factorial(n)` does not decrease the input, causing infinite recursion and a stack overflow.  
**Suggested Fix:**  
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```
```

## Customization

- Modify the prompt template in the `app.py` file to tweak the AI’s review focus (e.g., emphasizing performance or readability).

## Security

- The API key is stored as an environment variable (`GOOGLE_API_KEY`) rather than hardcoded in the script, ensuring better security.

## Troubleshooting

- **API Key Not Working**: Verify that `GOOGLE_API_KEY` is correctly set in your environment. Use `echo $GOOGLE_API_KEY` (Unix) or `echo %GOOGLE_API_KEY%` (Windows) to check.  
- **Package Errors**: Ensure all packages are installed and up-to-date with `pip install --upgrade streamlit langchain-google-genai`.  
- **Streamlit Won’t Start**: Confirm you’re running the correct command (`streamlit run app.py`) from the project directory.

## Contributing

Contributions are welcome! Feel free to submit pull requests with bug fixes, new features, or improvements.

---

**Streamlit Badge**  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<your-app-url>)  
*Note: Replace `<your-app-url>` with the deployed app URL if hosted online.*

**License**  
This project is licensed under the MIT License.
