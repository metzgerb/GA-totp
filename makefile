all: qr

qr: submission.py
	pip3 install --user qrcode[pil]
	dos2unix $^
	chmod +x $^
	
clean: 
	pip3 uninstall qrcode[pil]
	chmod -x ./submission.py