# author: cwb
# date: 2025/1/21

def is_empty(s:str) -> bool:
    """
    判断字符串是否为空
    """
    return s == ""

def is_not_empty(s:str) -> bool:
    """
    判断字符串是否不为空
    """
    return s != ""

def is_blank(s:str) -> bool:
    """
    判断字符串是否为空或只包含空白字符
    """
    return s == "" or s.isspace()

def reverse_string(s:str) -> str:
    """
    反转字符串
    """
    return s[::-1]  

def is_palindrome(s:str) -> bool:
    """
    判断字符串是否为回文
    """
    return s == s[::-1]


