import streamlit as st
import qrcode

def generate_wifi_qr_code(ssid, password):
    wifi_config = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def main():
    st.title("Home Settings and WiFi QR Code")

    # Input home settings
    st.header("Home Settings")
    home_name = st.text_input("Home Name", "My Home")
    location = st.text_input("Location", "City, Country")

    # WiFi QR Code generation
    st.header("WiFi QR Code Generator")
    ssid = st.text_input("WiFi SSID", "")
    password = st.text_input("WiFi Password", "", type="password")

    if st.button("Generate WiFi QR Code"):
        if ssid and password:
            qr_img = generate_wifi_qr_code(ssid, password)
            st.image(qr_img, caption="WiFi QR Code", use_container_width=True)
        else:
            st.warning("Please enter WiFi SSID and Password.")

    # Display home settings
    st.header("Home Details")
    st.write(f"Home Name: {home_name}")
    st.write(f"Location: {location}")

if __name__ == "__main__":
    main()
