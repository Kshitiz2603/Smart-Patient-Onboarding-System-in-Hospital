#importing necessary libraries/modules
import subprocess

#Running two python script at a time
subprocess.run("python3 real_time_video.py & python3 clock.py", shell=True)