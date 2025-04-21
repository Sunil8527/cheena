import streamlit as st

# Page title
st.title("📝 Quick Health & Lifestyle Survey")

st.write("Please answer the following questions:")

# 1. Name
name = st.text_input("1. What is your name?")

# 2. Age
age = st.number_input("2. How old are you?", min_value=0, max_value=120, step=1)

# 3. Health rating
health_rating = st.slider("3. How would you rate your current health?", 1, 10, 5)

# 4. Preferred exercise
exercise = st.selectbox(
    "4. What is your preferred type of exercise?",
    ["Walking", "Running", "Yoga", "Cycling", "Gym", "None"]
)

# 5. Average sleep
sleep = st.radio(
    "5. How many hours do you sleep on average?",
    ["Less than 5", "5-6", "6-7", "7-8", "More than 8"]
)

# Submit button
if st.button("Submit"):
    st.success("Thank you for your responses!")
    st.write("Here's what you shared:")
    st.write(f"👤 Name: **{name}**")
    st.write(f"🎂 Age: **{age}**")
    st.write(f"💪 Health Rating: **{health_rating}/10**")
    st.write(f"🏃 Preferred Exercise: **{exercise}**")
    st.write(f"😴 Average Sleep: **{sleep}**")
