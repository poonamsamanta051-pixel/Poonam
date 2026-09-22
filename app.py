import streamlit as st
                            

a=st.number_input("enter a name")
b=st.number_input("Enter another number")
if st.button("add"):
   st.success(a+b)
elif st.button("multiply"):
     st.success(a*b)
elif st.button("division"):
     st.success(a/b)
