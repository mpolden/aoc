days = $(wildcard day*.py)

.PHONY: $(days)

all: $(days) checkfmt

$(days):
	python3 $@

fmt:
	python3 -m black --quiet *.py

checkfmt:
	python3 -m black --check --diff *.py
