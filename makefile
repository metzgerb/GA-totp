all: qr

qr: submission.py
	python3 -m venv ./venv
	./venv/bin/pip3 install qrcode[pil]
	dos2unix $^
	chmod +x $^
	
clean: 
	chmod -x ./submission.py
	rm -rf qr.jpg
	rm -rf ./venv