### ns.py

#### ns *(nodes status)* is a CLI created to translate the status of Slurm nodes (and a few other things)! 

----
```shell
$ ns.py

Usage:

  -h, --help    show this help message and exit
  -r, --res     Maps the reservations and their respective nodes in a JSON
  -s, --status  Shows the status of the Nodes
  -d, --down    Shows the node set nodes that are down
  -j, --json    Shows the status of the Nodes in JSON format
  -y, --yaml    Shows the status of the Nodes in YAML format

The "status", "json", "yaml" and "down" arguments require the nodes to be analyzed.
To do this, use the argument "-n, --nodes".
e.g.:
        ns -s -n n00,n01
        ns -s -n n[00-01]
        ns -s -n n00 n01
        ns -s -n n00,n01,n[02-03]

The same is true for "-j", "-y" and "-d"

```
----
Examples:

*In '-n, --nodes' you can use different combinations of node sets:*

**e.g.:**
+ n00
+ n00,n01
+ n00 n01
+ n[00-01]
+ n[00,03-04]
+ n00,n[01],n[03-4]

---

```shell
$ ns.py --status --nodes n00
OUTPUT: 
    {'n00': 'idle'}
```

```shell
$ ns.py --down --nodes n[00,01]
OUTPUT:
    n01: down
```
> *Note: Only the nodes down in the set of nodes will be presented in the output.*

*The values that determine an 'inactive' node are:*
```shell
down = ['drain', 'drain*', 'down', 'down*', 'idle*']
```

```shell
$ ns.py --json --nodes n00
OUTPUT:
    {
        "n00": "idle"
    }
```

```shell
$ ns.py --yaml --nodes n00
OUTPUT:
    n00: idle
```

```shell
$ ns.py --res
OUTPUT:
{
    "maintenance": [
        "n00",
        "n01",
        "n02"
    ]
}
```
> *Note: The 'res' command will map all reservations and their respective nodes and will present them in JSON format*

----
TO-DO:
- [ ] Improve commands executed by subprocess
- [ ] Save output to file
- [ ] Receive a node set from a file
- [ ] Map the reason why the node is out of the queue (JSON)
- [ ] Add setup.py, requirements.txt and Makefile
- [ ] And a few more things...
----

Author: leonardo.araujo@atos.net

---
##### Feel free to change the script to your needs.
---

