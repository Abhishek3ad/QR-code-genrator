import qrcode

# Prompt the user for a link
link = input("Enter the link to be encoded in the QR code: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code grid
    border=4,  # thickness of the border (number of boxes)
)

# Add data to the QR code
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
filename = "qrcode.png"
img.save(filename)

print(f"QR code generated and saved as {filename}")
