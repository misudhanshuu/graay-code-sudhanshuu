#Sudhanshu 
import streamlit as st
st.header('Binary to Gray Code')
st.success('Enter that Binary Number')


B3 = st.number_input('Enter the value of B3 ', max_value=1, min_value=0)
B2 = st.number_input('Enter the value of B2 ', max_value=1, min_value=0)
B1 = st.number_input('Enter the value of B1 ', max_value=1, min_value=0)
B0 = st.number_input('Enter the value of B0 ', max_value=1, min_value=0)

if (B3== B2):
    g2=0
else:
    g2=1
if (B2== B1):
    g1=0
else:
    g1=1
if (B1== B0):
    g0=0
else:
    g0=1
    
st.success('Final O/p')
st.write('Your Gray Code is ', B3, g2, g1, g0)

st.warning('\n\n\nInstagram @sudhan.shuu        ')
#@Sudhan.shuu

