import pytest
import src.utils.dataUtilities
from src.utils.dataUtilities import load_data


def test_load_data_with_invalid_file_path():
    invalid_file_path = "../hellothere.csv"
    with pytest.raises(FileNotFoundError):
        load_data(invalid_file_path, "test")