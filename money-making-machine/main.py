import streamlit as st
import random
import time 
import requests

st.title("Money Making Machine")
def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You made ${amount}")

def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api-zeta.vercel.app/side_hustles?apiKey=playing321")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return "Freelancing"
        
    except:
        return "Something went wrong!"

st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)

def fetch_money_quote():
    try:
        response = requests.get("https://fastapi-api-zeta.vercel.app/money_quotes?apiKey=playing321")
        if response.status_code == 200 :
            quotes = response.json()
            return quotes["money_quotes"]

        else:
            return "Money is the root of all evil"

    except: 
        return "Something went wrong!"

st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(quote)