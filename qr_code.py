import qrcode

upi_id = input("Enter your UPI ID: ")
amount = float(input("Enter Amount: "))
upi_url = f"upi://pay?pa={upi_id}&am={amount}&cu=INR&"

qr = qrcode.QRCode()
qr.add_data(upi_url)
qr.make(fit=True)
qr.print_ascii(invert=True)