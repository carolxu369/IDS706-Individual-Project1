import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lib import calculate, plot_histogram, plot_kde

def analyze_grades(FILE_PATH):
    df = pd.read_excel(FILE_PATH)

    mean, median, std_dev = calculate(df)
    plot_histogram(df)
    plot_kde(df)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")

    # for test_script
    return [mean, median, std_dev]

if __name__ == "__main__":
    FILE_PATH = 'grade.xlsx'
    analyze_grades(FILE_PATH)