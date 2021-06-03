import subprocess as sb

proc_list = sb.Popen("ps -ef", shell=True)

for pid in proc_list:
    print(pid)