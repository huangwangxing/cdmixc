import time, os
s = '''This a Text for how to use Python3.\tLike you
With is message
You will learn some usful things.'''

print(s.endwith("s."))

log_time= time.strftime("%F %H:%M:%S")


path='/home/roger/下载'
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            print (fullpath)

with open("hello2.py", encoding="utf-8") as a_file:
    with open("python.log", mode="a", encoding="utf-8") as log_file:
        log_file.write(log_time+"\n")
        print("日志已记录到python.log\n")
     
