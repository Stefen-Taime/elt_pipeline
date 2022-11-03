up:
	docker stack deploy streaming-stack --compose-file docker-compose.yml

build: requirements.txt
	@echo "--INSTALLING dependencies--";
	@pip install -r requirements.txt;




