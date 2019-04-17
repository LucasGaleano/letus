import subprocess

run = subprocess.check_output('john  --max-length:6 --incremental:lower pass.lst',shell=True)
print('----------------')
print('status '+ run.decode())
