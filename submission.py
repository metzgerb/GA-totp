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

import sys, os

"""
Function Name: generate_qr
Description: generates an image file with a QR code to be used with Google
Authenticator. The QR code is an encoded URI.
Inputs: nothing
Outputs: svg file containing a QR code
"""
def generate_qr():
    print("generate_qr")


"""
Function Name: get_otp
Description: generates an OTP that matches Google Authenticator's OTP for each
30-second period. This repeats every thirty seconds until interrupted. 
Inputs: nothing
Outputs: outputs an OTP every 30 seconds to stdout
"""
def get_otp():
    print("get_otp")


"""
Description: intial code that validates the commandline arguments used
    and calls the other functions to create the connections and save files
Inputs: takes 1 argument (submission.py --command)
Outputs: returns nothing
"""
if __name__ == "__main__":
    #check total argument count
    if len(sys.argv) != 2:
        print("USAGE: %s --command" % sys.argv[0])
    #check that control port number is actually a number
    elif not sys.argv[1] == "--generate-qr" and not sys.argv[1] == "--get-otp":
        print("syntax error: invalid command")
    #everything is ok, call main function
    else:
        if sys.argv[1] == "--generate-qr":
            generate_qr()
        else:
            get_otp()