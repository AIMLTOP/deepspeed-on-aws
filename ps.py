import subprocess as sb

# proc_list = sb.Popen("ps -ef", shell=True)
# for pid in proc_list:
#     print(pid)

proc_list = sb.check_output('ps -ef', encoding='utf-8', shell=True)
print(proc_list)