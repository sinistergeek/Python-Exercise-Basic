import time
class container:
    def get_current_time():
        return time.strftime('%H:%M:%S',time.localtime())
    get_current_time = staticmethod(get_current_time)

print(container.get_current_time())
