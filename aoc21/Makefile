days = $(wildcard day*.py)

.PHONY: $(days)

all: checkfmt $(days)

$(days): mypy
	python3 $@

mypy:
	mypy --pretty *.py

fmt:
	python3 -m black --quiet *.py

checkfmt:
	python3 -m black --check --diff --quiet *.py
