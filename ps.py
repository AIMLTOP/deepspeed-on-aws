import subprocess as sb

proc_list = sb.Popen("ps -ef | awk '{print $2} ' ", stdout=sb.PIPE).communicate()[0].splitlines()

for pid in proc_list:
    print(pid)