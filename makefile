all: qr

qr: submission.py
	pip3 install --user qrcode[pil]
	dos2unix $^
	chmod +x $^
	
clean: 
	pip3 uninstall -y qrcode
	pip3 uninstall -y pil
	chmod -x ./submission.py
	rm -rf qr.jpg