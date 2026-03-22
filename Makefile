PYTHONPATH=src

.PHONY: check-contracts test

check-contracts:
	PYTHONPATH=$(PYTHONPATH) python3 -m skillpack.cli check-contracts

test:
	PYTHONPATH=$(PYTHONPATH) python3 -m unittest discover -s tests
