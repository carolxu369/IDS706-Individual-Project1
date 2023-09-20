
test:
    pytest test_script.py
    pytest test_lib.py
    pytest --nbval-lax main.ipynb 

format:
    black .

lint:
    pylint main_script.py
    pylint lib.py

install:
    pip install -r requirements.txt