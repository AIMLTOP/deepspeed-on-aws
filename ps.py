import subprocess as sb

proc_list = sb.Popen("ps -ef", stdout=sb.PIPE).communicate()[0].splitlines()

for pid in proc_list:
    print(pid)