import subprocess

def suspend_computer():
    subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0', '1', '0'])
    return None