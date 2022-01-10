# Here i have used pywhatkit library to achieve auto messaging functionality
import pywhatkit

# This function sends message automatically on given number with given message and on given hours and minuts


def sendMessage(number, msg, hrs, mins):
    pywhatkit.sendwhatmsg(number, msg, hrs, mins)
    print("Message sent successfully!!")


# This part takes user input through terminal and sends value to aforementioned function
# Also it has a try catch block to prevent getting invalid inputs done by user side
try:
    mobileNumber = input("Enter Your Mobile Number")
    message = input("Enter Your Message")
    hours = int(input("Input Hour"))
    minutes = int(input("Input Minute"))
    sendMessage(mobileNumber, message, hours, minutes)
except ValueError:
    print("VALUE ERROR: one or more inputs entered are invalid")
