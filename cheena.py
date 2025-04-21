import streamlit as st
from fpdf import FPDF

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

# Function to create PDF
def create_pdf(name, age, health_rating, exercise, sleep):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.cell(200, 10, txt="Quick Health & Lifestyle Survey", ln=True, align='C')

    # Add the user responses
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"👤 Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"🎂 Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"💪 Health Rating: {health_rating}/10", ln=True)
    pdf.cell(200, 10, txt=f"🏃 Preferred Exercise: {exercise}", ln=True)
    pdf.cell(200, 10, txt=f"😴 Average Sleep: {sleep}", ln=True)

    # Save PDF to a BytesIO buffer
    pdf_output = pdf.output(dest='S', format='pdf')
    return pdf_output

# Submit button
if st.button("Submit"):
    st.success("Thank you for your responses!")

    # Display responses on the webpage
    st.write("Here's what you shared:")
    st.write(f"👤 Name: **{name}**")
    st.write(f"🎂 Age: **{age}**")
    st.write(f"💪 Health Rating: **{health_rating}/10**")
    st.write(f"🏃 Preferred Exercise: **{exercise}**")
    st.write(f"😴 Average Sleep: **{sleep}**")

    # Create PDF from responses
    pdf_output = create_pdf(name, age, health_rating, exercise, sleep)

    # Allow the user to download the PDF
    st.download_button(
        label="📥 Download Your Survey Summary (PDF)",
        data=pdf_output,
        file_name="survey_summary.pdf",
        mime="application/pdf"
    )
