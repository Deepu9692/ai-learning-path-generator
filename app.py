import streamlit as st
from planner import generate_learning_plan
from search import get_learning_resources

st.set_page_config(page_title="AI Learning Path Generator", layout="centered")

st.title("🧠 AI Learning Path Generator")
st.markdown("Generate a personalized weekly learning schedule based on your goals.")

goal = st.text_input("🎯 Enter your learning goal", placeholder="e.g., Become an AI Engineer in 6 months")
time_per_week = st.slider("⏱️ Time available per week (in hours)", 1, 40, 10)
skill_level = st.selectbox("📘 Your current skill level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    if goal:
        with st.spinner("Generating your personalized learning path..."):
            plan = generate_learning_plan(goal, time_per_week, skill_level)
            resources = get_learning_resources(goal)
            st.success("Done! Here's your plan:")
            st.markdown(plan)
            st.markdown("### 📚 Recommended Resources")
            for res in resources:
                st.markdown(f"- [{res['title']}]({res['link']})")
    else:
        st.error("Please enter a goal.")