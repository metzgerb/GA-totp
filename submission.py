#!/usr/bin/env python3

"""Program Name: submission.py
Python Version: 3
Description: Generates QR codes and TOTPs for use with Google's Authenticator
API.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS370 (Fall 2019)
Created: 2019-11-25
Last Modified: 2019-11-25
"""

import sys, os, qrcode, time, urllib.parse, base64

"""
Function Name: totp
Description: generates a time-based on-time-password
Inputs: a string representing the secret key.
Outputs: string containing the password
"""
def totp(secret):
    
    #get current time
    current_time = time.time()
    
    #get time step by dividing current time since epoch by 30 seconds using floor division
    time_step = current_time//30
    
    #generate SHA-1 hash
    
    
    #truncate hash to 6 digits
    
    
    return str(time_step)

"""
Function Name: generate_qr
Description: generates an image file with a QR code to be used with Google
Authenticator. The QR code is an encoded URI.
Inputs: a string representing an account, a string representing the issuer,
a string representing the secret key.
Outputs: JPG file containing a QR code
"""
def generate_qr(account, issuer, secret):
    #build initial uri string for QR encoding
    uri_string = "//totp/"
    
    #add issuer prefix for label
    uri_string += urllib.parse.quote(issuer)
    uri_string += ":"
    
    #add account for label
    uri_string += urllib.parse.quote(account)
    
    #add base32 encoded secret key for parameters
    uri_string += "?secret="
    uri_string += base64.b32encode(secret)
    
    
    
    print(uri_string)
    #generate QR data as image
    img = qrcode.make('Some data here')
    
    #save img
    img.save("qr.jpg")


"""
Function Name: get_otp
Description: generates an OTP that matches Google Authenticator's OTP for each
30-second period. This repeats every thirty seconds until interrupted. 
Inputs: a string representing the secret key.
Outputs: outputs an OTP every 30 seconds to stdout
"""
def get_otp(secret):
    print("get_otp")


"""
Description: intial code that validates the commandline arguments used
    and calls the other functions to create the connections and save files
Inputs: takes 1 argument (submission.py --command)
Outputs: returns nothing
"""
if __name__ == "__main__":
    #set configs
    account = "example@gmail.com"
    issuer = "example co"
    secret = "this is a test"
    
    #check total argument count
    if len(sys.argv) != 2:
        print("USAGE: %s --command" % sys.argv[0])
    #check that control port number is actually a number
    elif not sys.argv[1] == "--generate-qr" and not sys.argv[1] == "--get-otp":
        print("syntax error: invalid command")
    #everything is ok, call main function
    else:
        if sys.argv[1] == "--generate-qr":
            generate_qr(account, issuer, secret)
        else:
            get_otp(secret)