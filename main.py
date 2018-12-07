import subprocess
import sys
args = sys.argv
from datetime import datetime

now = datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
var = "" + year + "" + month + "" + day + ""
tobackupid = args[1]
backupto = "raspi0124/" + tobackupid + ":" + var + ""
print("backing up " + tobackupid + ", version " + var + " with repo of " + backupto + "")
cmdlib = "sudo docker commit " + tobackupid + " " + var + ""
print("executing following command.." + cmdlib + "")
rutlib = subprocess.check_output( cmdlib.split(" ") )
print("executed!")
cmdlib = "sudo docker save " + backupto + " > /home/raspi0124/docker_backup/" + tobackupid + "_" + var +  ".tar"
print("executing following command.." + cmdlib + "")
rutlib = subprocess.check_output( cmdlib.split(" ") )
print("executed!")
print("Finishing process..")
exit()
