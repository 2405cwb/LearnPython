# author: cwb
# date: 2025/1/21

from cwb_helpers.string_untils import is_empty,is_not_empty,is_blank,reverse_string,is_palindrome

def test_string_untils():
    assert is_empty("") == True
    assert is_not_empty("test") == True
    assert is_blank(" ") == True
    assert reverse_string("test") == "tset"
    assert is_palindrome("test") == False

if __name__ == "__main__":
    test_string_untils()

