import streamlit as st
from PIL import Image

def main():
    st.title("Home WiFi QR Code Display")

    # Display QR Code image

    image = Image.open('Wifi.jpg')

    st.image(image, caption='Scan for Wifi')

if __name__ == "__main__":
    main()
