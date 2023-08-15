import streamlit as st

def main():
    st.title("Home WiFi QR Code Display")

    # Display QR Code image
    qr_code_image = r"C:\Users\UNIHU\Desktop\CODE DIRECTORY\Home_Pod\HUSAM-s-Home-Pod\Wifi.jpg"  # Replace with the actual image path
    st.image(qr_code_image, caption="WiFi QR Code", use_container_width=True)

if __name__ == "__main__":
    main()
