requirements:
	rm -rf requirements.txt
	poetry export -f requirements.txt --output requirements.txt

install: #TODO better way to install for local dev? 
	pip install -r requirements.txt
	pip install . --ignore-installed PyYAML

