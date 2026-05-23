# app.py
import streamlit as st

st.set_page_config(page_title="AI Tools Batch 1", layout="centered")
st.title("🔧 AI Tools - Batch 1")

tool = st.selectbox("Pick a tool:", [
    "EmailRewriter", "ExplainLike5", "HashtagFinder", "BugHunter", 
    "QuizSnap", "MeetingSummarizer", "ThumbnailGen", "MealPlanner", 
    "StorySeed", "CSVExplainer"
])

def run_tool(tool_name, user_input):
    prompts = {
        "EmailRewriter": f"Rewrite this email to be professional and polite: {user_input}",
        "ExplainLike5": f"Explain {user_input} like I am 5 years old, use simple words and an analogy",
        "HashtagFinder": f"Give me 15 trending low-competition hashtags for: {user_input}",
        "BugHunter": f"Find errors in this code and explain how to fix it: {user_input}",
        "QuizSnap": f"Create 5 MCQs with 4 options and answers from this text: {user_input}",
        "MeetingSummarizer": f"Summarize this into 5 bullet points: {user_input}",
        "ThumbnailGen": f"Give 5 viral YouTube thumbnail ideas for: {user_input}",
        "MealPlanner": f"Make a 3-day meal plan using only these ingredients: {user_input}",
        "StorySeed": f"Write a 100-word story using these 3 words: {user_input}",
        "CSVExplainer": f"Summarize this CSV data in 3 sentences for a non-technical person: {user_input}"
    }
    return prompts.get(tool_name, "Invalid tool")

input_box = st.text_area("Enter your input:", height=150)
if st.button("Run Tool"):
    if input_box:
        st.subheader("Prompt for AI:")
        st.code(run_tool(tool, input_box))
        st.info("Copy this prompt and paste it to ChatGPT, Claude, or me. This is how the tool works.")
    else:
        st.warning("Enter some input first")
