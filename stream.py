import streamlit as st
sal = st.number_input('enter your salary')
credit = st.number_input('enter your credit score')
if sal >= 50000 and credit >= 500:
      st.write("CONGRALUTATIONS ")
      st.balloons()
