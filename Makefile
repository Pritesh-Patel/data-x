requirements:
	rm -rf requirements.txt
	poetry export --without-hashes -f requirements.txt --output requirements.txt

install: #TODO better way to install for local dev? 
	pip install -r requirements.txt
	pip install . --ignore-installed PyYAML

