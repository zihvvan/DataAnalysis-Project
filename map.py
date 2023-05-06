import folium
import joblib
import streamlit as st

def main():
    # Load map in Streamlit
    st.set_page_config(page_title="Map Viewer")
    st.markdown("<h1 style='text-align: center;'>Seoul EV Charger Locations</h1>", unsafe_allow_html=True)
    map_html = joblib.load("map.pkl")
    st.markdown(map_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
