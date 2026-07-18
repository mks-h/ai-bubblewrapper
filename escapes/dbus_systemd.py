import subprocess
import sys


target = sys.argv[1]

_ = subprocess.run(
    ["systemd-run", "--user", "--wait", "--collect", "--quiet",
     "/usr/bin/sh", "-c", 'printf escaped > "$1"', "sh", target],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
