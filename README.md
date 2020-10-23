### ns.py

ns *(nodes status)* is a CLI created to translate the status of Slurm nodes (and a few other things)! 

----
```shell
Usage:

  -h, --help    show this help message and exit
  -r, --res     Maps the reservations and their respective nodes in a JSON
  -s, --status  Shows the status of the Nodes
  -j, --json    Shows the status of the Nodes in JSON format
  -y, --yaml    Shows the status of the Nodes in YAML format

The "status", "json", "yaml" and "down" arguments require the nodes to be analyzed.
To do this, use the argument "-n, --nodes".
e.g.:
        ns -s -n n00,n01
        ns -s -n n[00-01]
        ns -s -n n00 n01
        ns -s -n n00,n01,n[02-03]

The same is true for "-j", "-y" and "-d"#### ns (node status) 
```


