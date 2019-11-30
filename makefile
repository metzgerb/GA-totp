all: qr

qr: submission.py
	python3 -m venv ./venv
	./venv/bin/activate
	pip3 install --user qrcode[pil]
	dos2unix $^
	chmod +x $^
	
clean: 
	deactivate
	chmod -x ./submission.py
	rm -rf qr.jpg
	rm -rf ./venv