import os
from datetime import datetime, date , timedelta
import time




class Log_Clean():
    def __init__(self):
        self.START_TIME = 1619280000.0
        self.PATH = "/home/xyz/log"
        self.dir_list = os.listdir(self.PATH)

        today = date.today()
        yesterday = date.today()+timedelta(days=-1)
        self.yesterday_time = self.get_time_float(yesterday)
        self.today_time = self.get_time_float(today)
        now = datetime.now()
        self.now_time = self.get_time_float(now)

    def get_create_time(self, path):
        create_time = os.path.getctime(path)
        print(create_time)
        if create_time>self.START_TIME and create_time<self.yesterday_time:
            print("file true",create_time)
            return True

    def get_time_float(self, time_date):
        time_tuple = time_date.timetuple()
        return time.mktime(time_tuple)





    def run(self):
        for dir_name in self.dir_list:
            dir_path = os.path.join(self.PATH,dir_name)
            print("dir_path",dir_path)
            if os.path.isdir(dir_path):
                if self.get_create_time(dir_path):
                    if os.path.isdir(dir_path):
                        file_list = os.listdir(dir_path)
                        for file_name in file_list:
                            file_name_path = os.path.join(dir_path,file_name)
                            a = os.remove(file_name_path)
                            print("aaaa{}".format(a))
                        os.rmdir(dir_path)
                    else:
                            os.remove(dir_path)


