from supabase import create_client
import streamlit as st
from datetime import datetime

#setting up SUPABASE data table for users
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)


st.title("Womanhood Bill Calculator by Laura <3")

name = st.text_input("Name:\n")

#setting up for the math

total_price = st.number_input("Total amount (Include tax):\n")

tax = st.number_input("Tax amount:\n")
tip = st.checkbox("Are you tipping?\n")
if tip:
    tip_amnt = st.number_input("How much tip?\n")
else:
    tip_amnt = 0
    
people = st.number_input("How many people?\n", min_value=0, step=1)

#the math

if st.button("Calculate"):

    #saves name to SUPABASE TABLE

    if name:
        supabase.table("BILL CALCULATOR USER LOG").insert({"name": name}).execute()

    if people > 0:
        tax_split = tax / people
        total_split = (total_price - tax) / people
        if tip_amnt:
            tip_split = tip_amnt / people
            price_per_person = tax_split + tip_split + total_split
        else:
            price_per_person = tax_split + total_split
    
    #output
        st.write(f"Price per person: {price_per_person}")

    else:
        st.write("You don't need this silly goose!")


