days = $(wildcard day*.py)

.PHONY: $(days)

all: checkfmt $(days)

$(days): mypy
	python3 $@

mypy:
	mypy --strict --pretty *.py

fmt:
	black --quiet *.py

checkfmt:
	black --check --diff --quiet *.py
