# author: cwb
# date: 2025/1/21

from datetime import datetime,timedelta
def time_now():
    """
    获取当前时间
    """
    return datetime.now()

def time_now_str():
    """
    获取当前时间字符串
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def time_now_str_ms():
    """
    获取当前时间字符串，精确到毫秒
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def time_now_str_ms_no_ms():
    """
    获取当前时间字符串，精确到毫秒，不显示毫秒
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_time(time_str:str,format_str:str="%Y-%m-%d %H:%M:%S") -> datetime:
    """
    格式化时间字符串
    """
    return datetime.strptime(time_str,format_str)

def time_diff(start_time:datetime,end_time:datetime) -> timedelta:
    """
    计算时间差
    """
    return end_time - start_time    

def time_add(time:datetime,days:int=0,hours:int=0,minutes:int=0,seconds:int=0) -> datetime:
    """
    添加时间
    """
    return time + timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)

def time_sub(base_time, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    """
    从给定的时间中减去指定的时间量。
    """
    return base_time - timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                 milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)

def time_to_str(time:datetime,format_str:str="%Y-%m-%d %H:%M:%S") -> str:
    """
    将时间转换为字符串
    """
    return time.strftime(format_str)


