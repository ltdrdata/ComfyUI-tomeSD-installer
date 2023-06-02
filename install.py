import os
import sys
import subprocess

comfy_path = '../..'

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))
sys.path.append('.')   # for portable version
sys.path.append(comfy_path)

tomesd_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tomesd")

subprocess.check_call([sys.executable, "setup.py", "build"], cwd=tomesd_path)
subprocess.check_call([sys.executable, "setup.py", "install"], cwd=tomesd_path)