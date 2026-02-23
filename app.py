import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Hair Care Recommendation System")

st.title("AI Hair Care Recommendation System")
st.write("Fill out the questionnaire below to receive personalized hair care recommendations.")

# Questionnaire
hair_type = st.selectbox(
    "Hair Texture",
    ["Straight", "Wavy", "Curly", "Coily"]
)

scalp_condition = st.selectbox(
    "Scalp Condition",
    ["Dry", "Oily", "Normal", "Dandruff"]
)

damage_level = st.selectbox(
    "Damage Level",
    ["Low", "Moderate", "High"]
)

goal = st.selectbox(
    "Main Goal",
    ["Moisture", "Growth", "Repair Damage", "Reduce Frizz", "Volume"]
)

description = st.text_area("Describe your main hair concerns")

if st.button("Get Recommendation"):

    if description.strip() == "":
        st.warning("Please describe your hair concerns before submitting.")
    else:
        prompt = f"""
        You are a professional hair care consultant.

        Based on the following user profile, provide:
        1. Recommended shampoo type
        2. Recommended conditioner type
        3. Recommended treatment
        4. Suggested weekly routine
        5. Explanation for recommendations

        User Profile:
        Hair Type: {hair_type}
        Scalp Condition: {scalp_condition}
        Damage Level: {damage_level}
        Goal: {goal}
        Description: {description}
        """

        with st.spinner("Generating your personalized recommendation..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional hair consultant."},
                    {"role": "user", "content": prompt}
                ]
            )

        recommendation = response.choices[0].message.content

        st.subheader("Your Personalized Recommendation")
        st.write(recommendation)