#!/usr/bin/env python3.6

import subprocess
from ClusterShell.NodeSet import NodeSet
import pprint
import json
import sys
import yaml


class Color:
       PURPLE = '\033[1;35;48m'
       CYAN = '\033[1;36;48m'
       BOLD = '\033[1;37;48m'
       BLUE = '\033[1;34;48m'
       GREEN = '\033[1;32;48m'
       YELLOW = '\033[1;33;48m'
       RED = '\033[1;31;48m'
       BLACK = '\033[1;30;48m'
       UNDERLINE = '\033[4;37;48m'
       END = '\033[1;37;0m'

class NodesStatus:
    def __init__(self, nodes):
        self.nodes = NodeSet.fromlist(nodes)

    def status(self):
        nodesS = {}
        for n in self.nodes:
            nodesS[n] = subprocess.check_output(["sinfo -hn {0} --format %t".format(n)], shell=True).decode(sys.stdout.encoding).strip()
            for k, v in list(nodesS.items()):
                nodesS[k] = nodesS[k].strip()
                if len(v) <= 0:
                    del nodesS[k]
        return nodesS

    def nodesDown(self):
        down = ['drain', 'drain*', 'down', 'down*', 'idle*']
        for k, v in self.status().items():
            if v in down:
                print('\n' + k + ': ' + Color.RED + v + Color.END + '\n')

    def nodesRes():
        nodesRes = {}
        resv = [subprocess.check_output(["scontrol show reservation | grep -E 'ReservationName' | xargs | cut -d ' ' -f1 | awk -F '=' '{{print $NF}}'"], shell=True).decode(sys.stdout.encoding).strip()]
        for r in resv:
            for n in list(NodeSet(subprocess.check_output(["scontrol show reservation {0} | grep -Ew 'Nodes' | xargs | cut -d ' ' -f1 | awk -F '=' '{{print $NF}}'".format(r)], shell=True).decode(sys.stdout.encoding))):
                nodesRes.setdefault(r, []).append(n)
        print(json.dumps(nodesRes, sort_keys=True, indent=4))

    def showJson(self):
        print(json.dumps(self.status(), sort_keys=True, indent=4))

    def showYaml(self):
        print('\n' + yaml.dump(self.status()))
