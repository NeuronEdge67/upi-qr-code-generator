import qrcode

upi_id = input("Enter your UPI ID: ")
amount = float(input("Enter Amount: "))
upi_url = f"upi://pay?pa={upi_id}&am={amount}&cu=INR&tn=Tea"

img = qrcode.make(upi_url)

img.save(f"qr_{upi_id}_amount_{amount}.png")