import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title('Detected Solar panels in Marrakech-Safi region')
m = leafmap.Map(center=(32, -9), zoom=8)
m.add_basemap('SATELLITE')

m.to_streamlit()
