import streamlit as st

st.title ("control de acceso")

edad= st.number_input("Edad:",min_value=0, value=18)

tiene_identificacion=st.checkbox("Tiene identificacion")

if edad >=18 and tiene_identificacion:
  st.write("Puede ingresar.")
else:
  st.write("No puede ingrsar")
