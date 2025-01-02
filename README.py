import time

# 定义工作时间和休息时间（单位：秒）
WORK_TIME = 25 * 60  # 25分钟
BREAK_TIME = 5 * 60  # 5分钟

def countdown(seconds):
    """简单的倒计时函数"""
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(time_format, end='\r')  # 在同一行显示时间
        time.sleep(1)
        seconds -= 1
    print("时间到！")

def focus_timer():
    """开始专注计时"""
    print("开始工作！")
    countdown(WORK_TIME)
    
    print("休息一下！")
    countdown(BREAK_TIME)
    
    print("专注时钟完成，重新开始！")

if __name__ == "__main__":
    focus_timer()
# King.py
