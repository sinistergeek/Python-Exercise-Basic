from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

wd.get("https://www.wikipedia.org/")
assert "Wikipedia" in wd.title
print(wd.page_source)

f = open('hello.txt','w')
try:
    f.write('hello,world')
finally:
    f.close()

class ManagedFile:
    def __init__(self,name):
        self.name = name 
    def __enter__(self):
        self.file = open(self.name,'w')
        return self.file 
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.file:
            self.file.close()
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name,'w')
        yeild f 
    finally:
        f.close()
    with managed_file('hello.txt') as f:
        f.write('hello world!')
        f.write('bye now')

with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')


def __init__(self):
    self.foo = 11 
    self._bar = 23 
    self.__baz = 42 
t = Test() 
dir(t)
