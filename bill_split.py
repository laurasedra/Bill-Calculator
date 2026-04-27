from supabase import create_client
import streamlit as st
from datetime import datetime

#setting up SUPABASE data table for users
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)


st.title("Bill Split Calculator by Laura")

name = st.text_input("Name:\n")

#setting up for the math

total_price = st.number_input("Total amount:\n")

tax_type = st.radio("Tax input type:", ["Amount", "Percent"])

if tax_type == "Amount":
    tax = st.number_input("Tax amount:")
else:
    tax_percent = st.number_input("Tax percent:")
    tax = total_price * (tax_percent / 100)
    st.write(f"{tax_percent}% tax: ${tax:.2f}")

tip = st.checkbox("Are you tipping?\n")
if tip:
    tip_type = st.radio("Tip input type:", ["Amount", "Percent"])
    if tip_type == "Amount":
        tip = st.number_input("Tip amount:")
    else:
        tip_percent = st.number_input("Tip percent:")
        tip = total_price * (tip_percent / 100)
        st.write(f"{tip_percent}% tip: ${tip:.2f}")
else:
    tip = 0
    
people = st.number_input("How many people?\n", min_value=0, step=1)

#the math

if st.button("Calculate"):

    #saves name to SUPABASE TABLE

    if name:
        supabase.table("BILL CALCULATOR USER LOG").insert({"name": name}).execute()

    if people > 0:
        grand_total = tax + tip + total_price
        total_split = grand_total / people
        
    #output
        st.write(f"Price per person: ${price_per_person:.2f}")

    else:
        st.write("You don't need this silly goose!")

