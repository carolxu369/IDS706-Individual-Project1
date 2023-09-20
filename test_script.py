from main_script import analyze_grades
import pandas as pd
import pytest

def test_script():
    FILE_PATH = 'grade.xlsx'
    mean, median, std_dev = analyze_grades(FILE_PATH)

    assert mean == pytest.approx(76.94444444444444, abs=1e-2)
    assert median == pytest.approx(85.0, abs=1e-2)
    assert std_dev == pytest.approx(18.36641711869187, abs=1e-2)
