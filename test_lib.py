from lib import calculate
import pandas as pd

def test_lib():
    FILE_PATH = 'grade.xlsx'
    df = pd.read_excel(FILE_PATH)

    mean, median, std_dev = calculate(df)

    assert mean == pytest.approx(76.94444444444444, abs=1e-2)
    assert median == pytest.approx(85.0, abs=1e-2)
    assert std_dev == pytest.approx(18.36641711869187, abs=1e-2)