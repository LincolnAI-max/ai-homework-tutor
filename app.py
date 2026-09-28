import streamlit as st
import google.generativeai as genai

# -----------------------------
# 1. Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Homework Tutor",
    page_icon="📚",
    layout="centered"
)

# -----------------------------
# 2. Gemini API configuration
# -----------------------------
API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# 3. App title
# -----------------------------
st.title("📚 AI Homework Tutor")
st.write("Ask questions and get step-by-step help with your homework.")


# -----------------------------
# 4. Subject selection
# -----------------------------
subject = st.selectbox(
    "Choose a subject:",
    ["Mathematics", "Physics", "English", "Chemistry", "Other"]
)


# -----------------------------
# 5. Question input
# -----------------------------
question = st.text_area(
    "Enter your homework question:",
    placeholder="Example: What is the velocity of an object that travels 100 m in 5 seconds?"
)


# -----------------------------
# 6. Ask button
# -----------------------------
if st.button("Ask Tutor 📖"):

    if not question.strip():
        st.warning("Please enter a question first.")

    else:
        with st.spinner("Thinking..."):

            prompt = f"""
You are an AI homework tutor helping a Grade 10 student.

Subject: {subject}

Student's question:
{question}

Instructions:
- Explain the answer clearly.
- Use simple language.
- Show steps when solving problems.
- Do not simply give the final answer.
- Help the student understand the concept.
- If the question requires a calculation, show the formula,
  substitute the values, and calculate the result.
"""

            try:
                response = model.generate_content(prompt)

                st.subheader("📖 Tutor's Answer")
                st.write(response.text)

            except Exception as e:
                st.error("Something went wrong while contacting the AI.")
                st.write(str(e))