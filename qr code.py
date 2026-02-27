# refactoring:Modular Code
# refactoring: DRY Principle

# qr code generator
import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

# generating a qrcode
qr = qrcode.QRCode(box_size=10, border=4)
# pass data
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")
