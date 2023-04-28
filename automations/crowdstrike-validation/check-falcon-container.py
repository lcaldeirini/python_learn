#!/usr/bin/env python


import subprocess
from datetime import datetime


def get_falconcontainer_status():
    command = "kubectl get falconcontainer falcon-container -o json | jq -r '.status.phase'"
    falconcontainer_status = subprocess.run(command,shell=True,stdout=subprocess.PIPE,check=True).stdout.decode("utf-8").strip().split()[0]
    return falconcontainer_status


def show_falconcontainer_status():
    falconcontainer_status = get_falconcontainer_status()
    date_now = datetime.now()
    if falconcontainer_status == "DONE":
        print(f"{date_now} - INFO - status: [pass]")
    else:
        print(f"{date_now} - ERROR - status: [fail]")


# ---

show_falconcontainer_status()