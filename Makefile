PYTHONPATH=src

.PHONY: check-contracts test playbook

check-contracts:
	PYTHONPATH=$(PYTHONPATH) python3 -m skillpack.cli check-contracts

test:
	PYTHONPATH=$(PYTHONPATH) python3 -m unittest discover -s tests

playbook:
	PYTHONPATH=$(PYTHONPATH) python3 -m skillpack.cli build-playbook
