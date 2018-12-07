import subprocess
import sys
args = sys.argv
import datetime
d = datetime.date.today()
year = d.strftime('%y')
month = d.strftime('%m')
day = d.strftime('%d')
var = "" + year + "" + month + "" + day + ""
tobackupid = args[1]
backupto = "raspi0124/" + tobackupid + ":" + var + ""
print("backing up " + tobackupid + ", version " + var + " with repo of " + backupto + "")
cmdlib = "sudo docker commit " + tobackupid + " " + backupto + ""
print("executing following command.." + cmdlib + "")
subprocess.call(cmdlib.split())
print("executed!")
cmdlib = "sudo docker -o save " + backupto + " > /home/raspi0124/docker_backup/" + tobackupid + "_" + var +  ".tar"
print("executing following command.." + cmdlib + "")
subprocess.call(cmdlib.split())
print("executed!")
print("Finishing process..")
exit()
