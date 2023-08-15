import streamlit as st

def main():
    st.title("Home WiFi QR Code Display")

    # Display QR Code image
    qr_code_image = "path_to_your_qr_code_image.png"  # Replace with the actual image path
    st.image(qr_code_image, caption="WiFi QR Code", use_container_width=True)

if __name__ == "__main__":
    main()
