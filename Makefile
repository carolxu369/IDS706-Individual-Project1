
test:
	pytest test_script.py
	pytest test_lib.py
	pytest --nbval-lax main.ipynb  # Test the Jupyter Notebook using nbval

format:
	black *.py 
	nbqa black *.ipynb 

lint:
	ruff check *.py
	nbqa ruff *.ipynb

install:
	pip install -r requirements.txt
