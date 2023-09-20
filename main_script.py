"""This module contains functions for analyzing grades."""

import pandas as pd
from lib import calculate, plot_histogram, plot_kde

def analyze_grades(file_path):
    """
    Analyze grades from an Excel file and display statistics and plots.

    Args:
        file_path (str): Path to the Excel file containing grades.
    """
    df = pd.read_excel(file_path)

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