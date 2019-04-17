import subprocess

run = subprocess.check_output('john  --max-length:5 --incremental:lower  pass.lst --format:Raw-SHA1 --node:2/2',shell=True)
print('----------------')
print('status '+ run.decode())
