SHELL := /bin/bash

all: qr

qr: submission.py
	python3 -m venv ./venv
	source ./venv/bin/activate
	pip3 install qrcode[pil]
	dos2unix $^
	chmod +x $^
	
clean: 
	chmod -x ./submission.py
	rm -rf qr.jpg
	rm -rf ./venv