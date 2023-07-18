import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = None,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="yellow")
    img.save("qrimg001.png")

url = input("Enter your url: ")
generate_qrcode(url) 