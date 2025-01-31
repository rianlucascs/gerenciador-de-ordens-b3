
import subprocess
import config_secrets
from os.path import exists, join, dirname, abspath

bash_file_path = join(dirname(abspath(__file__)), "auto_commit.sh")

def auto_commit() -> None:
    
    if exists(bash_file_path):
        subprocess.Popen(
            [
                config_secrets.PATH_GIT_BASH_EXE, # <---!! 
                bash_file_path
                ],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    return None