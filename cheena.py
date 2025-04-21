import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import io

# Page title
st.title("📝 Hi Dear Senorita😊")

st.write("Can Your answer of this Questions:")

# 1. Name
name = st.text_input("1. What is your name? well I know but fir bhi Bata do😭😭")

# 2. Age
age = st.number_input("2. How old are you? Real wala yrr ok !", min_value=0, max_value=120, step=1)

# 3. Health rating
health_rating = st.slider("3. How would you rate your current health?", 1, 10, 5)

#4. Hobby
hobby = st.text_input("1. What is your hobby? ")

# 5. Preferred exercise
exercise = st.selectbox(
    "4. What is your preferred type of exercise?",
    ["Walking", "Running", "Yoga", "Cycling", "Gym", "None"]
)

# 6. Average sleep
sleep = st.radio(
    "5. How many hours do you sleep on average?",
    ["Less than 5", "5-6", "6-7", "7-8", "More than 8"]
)

# Submit button
if st.button("Submit"):
    st.success("Thank you for your responses!")

    # Prepare text for image
    result_text = (
        f"Quick Health & Lifestyle Survey\n\n"
        f"👤 Name: {name}\n"
        f"🎂 Age: {age}\n"
        f"💪 Health Rating: {health_rating}/10\n"
        f"🏃 Preferred Exercise: {exercise}\n"
        f"😉 hobby: {hobby}"
        f"😴 Average Sleep: {sleep}"

       f"st.write(name , "Ye ab Whatsapp kar do ")"
        
        
    )

    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.text(0.01, 0.9, result_text, fontsize=12, va='top', ha='left', wrap=True)
    ax.axis('off')

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='jpeg', bbox_inches='tight')
    buf.seek(0)

    # Show image in Streamlit
    st.image(buf, caption="Your Responses", use_container_width=True)

    # Provide download button
    st.download_button(
        label="📥 Download Your Survey Summary (JPEG)",
        data=buf,
        file_name="survey_summary.jpeg",
        mime="image/jpeg"
    )

st.write(name , "Ye ab Whatsapp kar do ")

