# IDS706-Individual-Project1

This is a Python GitHub Repository of Continuous Integration using GitHub Actions of Python Data Science Project, which includes the following:
- A .devcontainer configuration for a Python environment
- A Makefile with commands for setup, testing, and linting
- GitHub Actions for CI/CD
- A requirements.txt for project dependencies
- A README.md with setup and usage instructions
- Jupyter Notebook using Pandas for descriptive statistics
- Python script using Pandas for descriptive statistics
- A lib.py file that shares the common code between the script and notebook
- A test_script.py to test script
- A test_lib.py to test library
- Data visualization for descriptive statistics analysis

## Prerequisites

- Python 3
- pandas==1.3.3
- matplotlib==3.4.3
- seaborn==0.11.2
- pytest==6.2.5
- black==21.9b0
- pylint==2.9.6
- nbval==0.9.6   
- openpyxl==3.0.7 
- click==7.1.2  
- ruff
- nbqa

## Report

For this pandas descriptive statistics script, I used pandas, matplotlib, and seaborn libraries in python to read a “grade.xlsx” and calculated the mean, median, and standard deviation.
Then, I generated two plots as following.
This is the link to my video demo for this project https://youtu.be/C3jt4oKo5Zs. 

- Mean: 76.94444444444444
- Median: 85.0
- Standard Deviation: 18.36641711869187

![Distribution Plot](data%20plot/distribution%20plot.png)
![KDE Plot](data%20plot/KDE%20plot.png)

## Steps to run the Repo

1. Use [git clone] to clone the GitHub repository to your local machine
2. Install the project dependencies listed in 'requirements.txt' using [pip install -r requirements.txt]
3. Execute main_script.py using [python3 main_script.py]
4. Start your Jupyter Notebook or Jupyter Lab and find main.ipynb and open it, then execute the cells in the notebook one by one
5. Execute test_script.py using [pytest test_script.py]
6. Execute test_lib.py using [pytest test_lib.py]
