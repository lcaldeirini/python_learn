#!/usr/bin/env python

import subprocess
from datetime import datetime

# show legacy apps on kubernetes

def get_kubernetes_legacy_apps():
    kubens = "kubectl get ns -o name | cut -d "/" -f2 | grep onyo"
    kubernetes_legacy_apps = subprocess.run(kubens,shell=True,stdout=subprocess.PIPE,check=True)
    return kubernetes_legacy_apps
print("apps on legacy at kubernetes")

# show microservices apps on kubernetes

def get_kubernetes_ms_apps():
    kubens = "kubectl get ns -o name | cut -d "/" -f2 | grep pp"
    kubernetes_legacy_apps = subprocess.run(kubens,shell=True,stdout=subprocess.PIPE,check=True)
    return kubernetes_ms_apps
print("apps on microservices at kubernetes")



get_kubernetes_legacy_apps()


