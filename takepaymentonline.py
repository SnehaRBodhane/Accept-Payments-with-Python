import qrcode

#Taking UP ID As a input
upid_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#you can modify these URLs based on the payment apps you want to support


phonepe_url = f'upi://pay?pa={upid_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upid_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upid_id}&pn=Recipient%20Name&mc=1234'

#Create OR codes for each payment appp
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the OR code to image file 
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# display the QR code (you may need to install pillow library )
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
