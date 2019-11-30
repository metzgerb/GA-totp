*******************************************************************************
*
*						CS370 Programming Project 2
*
*******************************************************************************

CREATED: 2019-11-25
LAST MODIFIED: 2019-11-30
AUTHOR: Brian Metzger (metzgerb@oregonstate.edu)



PROJECT DESCRIPTION: This program generates QR codes and Time-Based One Time
Passwords (TOTPs) for use with the Google Authenticator. The project is written
in Python 3. Testing done with Python 3.6 on Windows and Flip.



REQUIREMENTS:
	-Python 3 must be installed
	-qrcode and pillow must be installed (only if not using the makefile as 
		described below)



SETUP INSTRUCTIONS:

USING MAKEFILE:
	1. Run the attached makefile with the command `make`:
		a. make will create a python3 virtual environment
		b. make will install the qrcode and pillow libraries inside the virtual
			environment
		c. make will add the executable permission to the submission.py
	
	2. When `make` finishes, run submission.py with the appropriate commands
		(see USAGE INSTRUCTIONS below)
		
		NOTE:[POSIX] The shebang at the top of submission.py points to the created 
			virtual environment. To override, specify the path/interpreter 
			before submission.py.
			
WITHOUT USING MAKEFILE:
	1. Install Python 3.
	
	2. Create Virtual Environment:
		a. [POSIX] python3 -m venv ./venv
		   [WINDOWS] python -m venv .\venv
						OR
		   [WINDOWS] python3 -m venv .\venv
	
	3. Activate virtual environment and install dependencies:
		a. [POSIX] source ./venv/bin/activate
		   [WINDOWS] .\venv\Scripts\activate.bat
		b. pip3 install qrcode[pil]
	
	4. [POSIX ONLY] add executable permissions to submission.py:
		a. chmod +x ./submission.py
	
	5. With active virtual environment, run submission.py with the appropriate
		commands (see USAGE INSTRUCTIONS below)
		
		NOTE:[POSIX] The shebang at the top of submission.py points to the created 
			  virtual environment. To override, specify the path/interpreter 
			  before submission.py.


	
USAGE INSTRUCTIONS:

USAGE:	submission.py --command [secret] [account] [issuer]
COMMANDS:
	--generate-qr	creates a .JPG file containing a QR code using optional parameters [secret], [account], and [issuer]
	--get-otp		contiuously generates TOTP codes using optional parameter [secret]
	--help			prints this usage information
OPTIONAL:
	[secret]	A secret key for calculating codes (default: 'This is a Test!')
	[account]	The account you wish to generate qr code for (default: 'ExamplePerson@Example.com')
	[issuer]	The company issuing the account (default: 'Example Co')



CLEANUP INSTRUCTIONS:

USING MAKEFILE:
	1. If virtual environment is activated, deactivate it:
		a. deactivate
		
	2. Run the attached makefile with the command `make clean`
		a. make will remove the executable permission from submission.py
		b. make will delete 'qr.jpg' if it exists in the current directory
		c. make will delete the python3 virtual environment
	
	3. Remove the source files if desired
			
WITHOUT USING MAKEFILE:
	1. Deactivate and delete virtual environment directory:
		a. deactivate
		b. [POSIX] rm -rf ./venv
		   [WINDOWS] del .\venv ('Y' to confirm)
	
	2. Delete qr.jpg file:
		a. [POSIX] rm -rf ./qr.jpg
		   [WINDOWS] del .\qr.jpg
	
	3. [POSIX ONLY] remove executable permissions from submission.py
		a. chmod -x ./submission.py
		
	4. Remove the source files if desired