# password_strength_app.py

import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐")

st.markdown("<h1 style='text-align: center; color: purple;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.markdown("### Enter a password to check its strength:")

# Input field
password = st.text_input("Enter Password", type="password")
check = st.button("Check Strength")

# Function to evaluate password and provide feedback
def password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Use at least 8 characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Include at least one number (0–9).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one uppercase letter (A–Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one lowercase letter (a–z).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("🔸 Include a special character (e.g. @, #, $, !).")

    # Determine strength level
    if score == 5:
        return "Strong 💪", "green", feedback
    elif score >= 3:
        return "Moderate ⚠️", "orange", feedback
    else:
        return "Weak ❌", "red", feedback

# Main output
if check:
    if password:
        strength, color, suggestions = password_strength(password)
        st.markdown(f"<h3 style='color:{color}'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

        # Show feedback if password is not strong
        if suggestions:
            st.subheader("🛠 Suggestions to Improve:")
            for item in suggestions:
                st.write(item)
        else:
            st.success("✅ Your password is strong. Great job!")
    else:
        st.warning("Please enter a password to check.")
