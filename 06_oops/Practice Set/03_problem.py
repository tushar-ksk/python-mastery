# Railway Department 

import random
import string


print("\nWelcome to Indian Railways")
print(">>> Delhi Depot <<<")

class Passenger:
    depot = "Delhi"

    def __init__(self, name, class_type, start, desitination, price, time):
        self.name = name
        self.class_type = class_type
        self.start = start
        self.desitination = desitination
        self.price = price
        self.time = time

    def book(self):

        ticket_info = f"""
           >>>Booking Details<<<

        Name           >>> {self.name}
        Depot          >>> {self.depot}
        Class          >>> {self.class_type}
        Starting Point >>> {self.start}
        Stopping Point >>> {self.desitination}
        Price          >>> {self.price}
        Time Taken     >>> {self.time}
        """
        print(ticket_info)
        with open("ticket.txt", "a") as f:
            f.write(ticket_info)



while True:
    e = input("\nPress \"enter\" if you want to fill your details \nor Press any \"other key\" and then \"enter\" if you want to exit\n")
    if e == "":
        name = input("Enter your name >>> ").capitalize() 
        start = "Delhi"
        print("\nDestinations: Panipat, Karnal, Hisar, Rewari, Udaipur, Jind")
        desitination = input("\nEnter your Desitination >>> ").lower()

        if desitination == "panipat":
            time = "2 hrs"
            print("\n>>1A (First AC): ₹1,175\n>>2A (Second AC): ₹710\n>>3A (Third AC): ₹505\n>>CC (Chair Car): ₹300\n>>SL (Sleeper): ₹145\n>>2S (Second Sitting): ₹90\n>>EC (Executive Chair Car): ₹825")
            class_type = input("\nEnter your class_type type >>> ")
            if class_type == "1A":
                price = 1175
            elif class_type == "2A":
                price = 710
            elif class_type == "3A":
                price = 505
            elif class_type == "CC":
                price = 300
            elif class_type == "SL":
                price = 145
            elif class_type == "2S":
                price = 90
            elif class_type == "EC":
                price = 825
            else:
                price = "Invalid class_type type"
                break

        elif desitination == "jind":
            time = "2 hrs 50 min"
            print(">>1A (First AC): ₹1,255\n>>2A (Second AC): ₹760\n>>3A (Third AC): ₹555\n>>SL (Sleeper): ₹175\n>>2S (Second Sitting): ₹90\n>>General (Unreserved): ₹60")
            class_type = input("Enter your class_type type >>> ")
            if class_type == "1A":
                price = 1255
            elif class_type == "2A":
                price = 760
            elif class_type == "3A":
                price = 555
            elif class_type == "SL":
                price = 175
            elif class_type == "2S":
                price = 90
            elif class_type.lower() == "general":
                price = 60
            else:
                price = "Invalid class_type type"
                break

        elif desitination == "karnal":
            time = "2 hrs 25 min"
            print(">>1A (First AC): ₹1,175\n>>2A (Second AC): ₹710\n>>3A (Third AC): ₹505\n>>CC (Chair Car): ₹315\n>>SL (Sleeper): ₹145\n>>2S (Second Sitting): ₹90\n>>EC (Executive Chair Car): ₹1,105")
            class_type = input("Enter your class_type type >>> ")
            if class_type == "1A":
                price = 1175
            elif class_type == "2A":
                price = 710
            elif class_type == "3A":
                price = 505
            elif class_type == "CC":
                price = 315
            elif class_type == "SL":
                price = 145
            elif class_type == "2S":
                price = 90
            elif class_type == "EC":
                price = 1105
            else:
                price = "Invalid class_type type"
                break

        elif desitination == "hisar":
            time = "3 hrs"
            print(">>1A (First AC): ₹1,255\n>>2A (Second AC): ₹760\n>>SL (Sleeper): ₹145\n>>2S (Second Sitting): ₹90\n>>General (Unreserved): ₹60")
            class_type = input("Enter your class_type type >>> ")
            if class_type == "1A":
                price = 1255
            elif class_type == "2A":
                price = 760
            elif class_type == "SL":
                price = 145
            elif class_type == "2S":
                price = 90
            elif class_type.lower() == "general":
                price = 60
            else:
                price = "Invalid class_type type"
                break

        elif desitination == "rewari":
            time = "4 hrs"
            print(">>1A (First AC): ₹1,255\n>>2A (Second AC): ₹760\n>>3A (Third AC): ₹555\n>>CC (Chair Car): ₹425\n>>SL (Sleeper): ₹175\n>>EC (Executive Chair Car): ₹685\n>>General (Unreserved): ₹25")
            class_type = input("Enter your class_type type >>> ")
            if class_type == "1A":
                price = 1255
            elif class_type == "2A":
                price = 760
            elif class_type == "3A":
                price = 555
            elif class_type == "CC":
                price = 425
            elif class_type == "SL":
                price = 175
            elif class_type == "EC":
                price = 685
            elif class_type.lower() == "general":
                price = 25
            else:
                price = "Invalid class_type type"
                break

        elif desitination == "udaipur":
            time = "16 hrs"
            print(">>1A (First AC): ₹2,675\n>>2A (Second AC): ₹1,595\n>>3A (Third AC): ₹1,130\n>>SL (Sleeper): ₹430")
            class_type = input("Enter your class_type type >>> ")
            if class_type == "1A":
                price = 2,675
            elif class_type == "2A":
                price = 1,595
            elif class_type == "3A":
                price = 1,130
            elif class_type == "SL":
                price = 430
            else:
                price = "Invalid class_type type"
                break

        else:
            print("Invalid desitination entered!")
            break

        print("\nTicket price is:", price)

        p = Passenger(name, class_type, start, desitination.capitalize(), price, time)
        p.book()

        b = input("\nType \'book\' if you want to book tikcet >>> ").lower()
        if b == "book":
            print("\n>>>Modes of pyment avialable:\n>>UPI\n>>Net Banking\n>>Credit Card\n>>Debit Card")
        
            c= input("\nEnter you mode of payment >>> ").lower()

            if c == "upi":
                print("\nUPI id >>> ird123@sbi.upi")

            elif c == "net banking" or c == "credit card" or c == "debit card":
                print("\nAccount Number >>> 2100025625435582")
            
            else:
                print("\nInvalid Input")
                break
            try:
                phone = int(input("\nEnter your phone number >>> "))
            except:
                print("Invalid phone number")
                break

            if len(str(phone)) == 10:
                otp = random.randrange(100000,999999)
                print(f"\nGenerated OTP: {otp}")
                OTP = int(input("\nEnter the OTP sent to your phone number >> "))
                
            else:
                print("\nInvalid Phone Number!")
                break

            if int(OTP) == int(otp):
                characters = string.ascii_letters + string.digits
                captcha = ''.join(random.choices(characters, k=6))
                print("\nGenerated CAPTCHA:", captcha)
                cap = input("\nEnter Captcha >> ")
            else:
                print("\nOTP didn't matched!")
                break

            if captcha == cap:
                print(f"\nTicket Booked with seat number >>> {random.randint(1, 72)}")
                print("Thanks....\n")
                break

            else:
                print("\nCaptcha did't match!")
                break

        else:
            print("\nYou entered invalid word >>>>>> Your ticket is cancelled!")
            print("Program exits....")
        break

    else:
        print("\nProgram exits....")
        break
