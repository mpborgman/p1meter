### Local usage

clean:
	rm -rf .venv

venv:
	python3 -m venv .venv
	python3 -m pip install .

deploy:
	scp src/*.py mpborgman@p1meter.borgmannen.org:/home/mpborgman/projects/p1meter/src/
	scp pyproject.toml Makefile README.md mpborgman@p1meter.borgmannen.org:/home/mpborgman/projects/p1meter/

startserver:
	python3 src/main.py
