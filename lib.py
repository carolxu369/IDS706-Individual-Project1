import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate(dataframe):
    mean = dataframe['grade'].mean()
    median = dataframe['grade'].median()
    std_dev = dataframe['grade'].std()
    return mean, median, std_dev

def plot_histogram(dataframe):
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe['grade'], bins=20, color='skyblue')
    plt.title('Distribution of Grades')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_kde(dataframe):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(dataframe['grade'], shade=True, color='skyblue')
    plt.title('Kernel Density Estimation (KDE) of Grades')
    plt.xlabel('Grade')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()