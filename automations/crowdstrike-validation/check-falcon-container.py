#!/usr/bin/env python

import json
import subprocess
import sys
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


def check_falcon_injector_pods():
    command = "kubectl get deploy injector -n falcon-system -o json"
    date_now = datetime.now()
    falconinjector_status = subprocess.run(command,shell=True,stdout=subprocess.PIPE,check=True).stdout.decode("utf-8").strip()
    status_dict = json.loads(falconinjector_status)
    desired_replica_count = status_dict["status"]["replicas"]
    ready_replica_count = status_dict["status"]["readyReplicas"]
    if ready_replica_count == desired_replica_count:
        print(f"{date_now} - falcon-injector pods are OK")
    else:
        print(f"{date_now} - falcon-injector pods are not ready")


def check_falcon_injector():
    falcon_injector_check_pod = check_falcon_injector_pods()
    date_now = datetime.now()
    if falcon_injector_check_pod == "DONE":
        print(f"{date_now} - PODS - status: [running]")
    else:
        print(f"{date_now} - PODS - status: [not working]")

# ---

# option = input("choose a option: ")
option = sys.argv[0]
if option == "falconcontainer":
    show_falconcontainer_status()
elif option == "injector":
    check_falcon_injector_pods()
else:
    show_falconcontainer_status()
    check_falcon_injector_pods()


# check deployment blocked by injector (verify status of status (parameters at json) all deployments in all namespace)
## no_pods=$([ "${fail_to_get_image}" -eq 0 ] && [ "$(kubectl get deploy "${deploy}" -n "${namespace}" -o json | jq -r ".status.conditions[].message" | grep -c "failed calling webhook")" -gt 0 ]  && [ "${deploy_pod_count}" -eq 0 ] && printf 1 || printf 0
