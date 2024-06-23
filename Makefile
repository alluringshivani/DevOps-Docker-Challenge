# build the code
build:
	sudo ansible-playbook orchestrate.yml --ask-become-pass

server:
	uvicorn main:app --host 0.0.0.0 --port 8000

verify:
	curl http://localhost:8000/hello

