import time
class Clock:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.prompt = "未开始计时"
    def start(self):
        self.start_time = time.localtime()
        self.prompt = "请调用stop方法"
        print("开始计时")
    def stop(self):
        self.stop_time = time.localtime()
        if not self.start():
            print("请调用start方法")
        else:
            self.get_time()
            print("计时结束")
    def get_time(self):
        for each in range(6):
            self.lasted = []
            self.lasted.append(self.stop_time[each]-self.start_time[eacha])
t1 = Clock()
t1.start()
t1.stop()