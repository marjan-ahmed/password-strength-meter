import streamlit as st
import random
import string
import re
import time 

st.set_page_config("Password strength Meter", "🛠")
st.title("🔐 Password Strength Meter & Generator")

def is_password_sharp(password: str):
    score = 0

    if len(password) >= 8:
        score += 25
        st.write("✅ Password length is good.")
    else:
        st.write("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 25
        st.write("✅ Contains both uppercase and lowercase letters.")
    else:
        st.write("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 25
        st.write("✅ Contains numbers.")
    else:
        st.write("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&/,)=+-~`.\*}|]", password):
        score += 25
        st.write("✅ Contains special characters (!@#$%^)")
    else:
        st.write("❌ Include at least one special character ((!@#$%^)")

    return score


def generate_password():
    
    numbers = random.randint(100, 900)
    char_list = [random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(8)]  
    char_string = ''.join(char_list)
    symbol_list = random.choices(string.punctuation)
    symbols = ''.join(symbol_list) 
    passd = char_string + str(numbers) + symbols  

    return passd
generate_pass = st.button("Generate Password")

if generate_pass:
    generated_password = generate_password()
    st.write(f"🔑 Generated Password: {generated_password}")

    st.subheader("Password Scoring:")
    score = is_password_sharp(generated_password)

    st.progress(score / 100)

    if score == 100:
        st.success("💪 Very Strong Password!")
    elif score >= 75:
        st.success("✅ Strong Password")
    elif score >= 50:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password. Please improve it.")

st.subheader("Check Your Own Password Strength")
input_password = st.text_input("Enter your password:", type="password")

if input_password:
    st.subheader("Your Password Scoring:")
    score = is_password_sharp(input_password)

    st.progress(score / 100)

    if score == 100:
        st.success("💪 Very Strong Password!")
    elif score >= 75:
        st.success("✅ Strong Password")
    elif score >= 50:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password. Please improve it.")

st.markdown(f"<h6 style='text-align: center; color: black;'>© {time.strftime} 2025 Mohammad Marjan Ahmed. All rights reserved.</h6>", unsafe_allow_html=True)