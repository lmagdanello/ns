#!/usr/bin/env python3.6

import argparse
from nodestatus import NodesStatus, Color
import sys
import textwrap

def main():

    parser = argparse.ArgumentParser(prog='ns', description='ns (nodes status) is a CLI created to translate the status of Slurm nodes (and a few other things)!' + Color.GREEN + ' ヽ(´▽`)/' + Color.END, formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''The "status", "json", "yaml" and "down" arguments require the nodes to be analyzed. \n\
To do this, use the argument "-n, --nodes". \n\
e.g.: \n\
        ns -s -n n00,n01 \n\
        ns -s -n n[00-01] \n\
        ns -s -n n00 n01 \n\
        ns -s -n n00,n01,n[02-03] \n\n\
The same is true for "-j", "-y" and "-d"'''))

    parser.add_argument('-r', '--res', action='store_true', help='Maps the reservations and their respective nodes in a JSON')
    parser.add_argument('-s', '--status', action='store_true', help='Shows the status of the Nodes')
    parser.add_argument('-d', '--down', action='store_true', help='Shows the node set nodes that are down')
    parser.add_argument('-j', '--json', action='store_true', help='Shows the status of the Nodes in JSON format')
    parser.add_argument('-y', '--yaml', action='store_true', help='Shows the status of the Nodes in YAML format')

    opts, rem_args = parser.parse_known_args()
    if opts.status or opts.down or opts.json or opts.yaml:
        parser.add_argument('-n', '--nodes', required=True, nargs='*')

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if args.status:
        nodes = NodesStatus(args.nodes)
        if len(nodes.status()) <= 0:
            print('Out of range!\n')
        else:
            print(nodes.status())
    elif args.down:
        nodes = NodesStatus(args.nodes)
        nodes.nodesDown()
    elif args.json:
        nodes = NodesStatus(args.nodes)
        nodes.showJson()
    elif args.yaml:
        nodes = NodesStatus(args.nodes)
        nodes.showYaml()
    elif args.res:
        NodesStatus.nodesRes()
    else:
        print('\nCommand not found...\n')
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()



