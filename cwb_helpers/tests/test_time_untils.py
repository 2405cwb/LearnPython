# author: cwb
# date: 2025/1/21

from datetime import datetime,timedelta
from cwb_helpers.time_untils import * 

def test_time_untils():
    assert time_now() == datetime.now()
    assert time_now_str() == datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert time_now_str_ms() == datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    assert time_now_str_ms_no_ms() == datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # assert format_time(datetime.now(),"%Y-%m-%d %H:%M:%S") == datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert time_diff(datetime.now(),datetime.now()) == timedelta(0)
    assert time_add(datetime.now(),days=1) == datetime.now() + timedelta(days=1)
    assert time_sub(datetime.now(),days=1) == datetime.now() - timedelta(days=1)
    assert time_to_str(datetime.now(),"%Y-%m-%d %H:%M:%S") == datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    test_time_untils()

