# author: cwb
# date: 2025/1/21

def read_file(file_path:str,encoding:str="utf-8") -> str:
    """
    读取文件
    """
    with open(file_path, 'r',encoding=encoding) as file:
        return file.read()

def write_file(file_path:str, content:str,encoding:str="utf-8"):
    """
    写入文件
    """
    with open(file_path, 'w',encoding=encoding) as file:
        file.write(content)

