# author: cwb
# date: 2025/1/21

from cwb_helpers.file_utils import read_file

def test_file_utils():
    assert read_file("test.txt") == "test"

if __name__ == "__main__":
    test_file_utils()
    