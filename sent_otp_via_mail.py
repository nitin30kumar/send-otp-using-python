import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("nitinkumaranonymous123@gmail.com", "ljdhsfdspcvntjre")
print("--- OTP verification using GMail account ---")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
rslt =0
while(rslt != 1):
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("OTP Verified")
        rslt = 1
    else:
        print("Please Check your OTP & try again")
        rslt = 0

