#!/usr/bin/python3

# this script will install all the required packages that you need on
# ubuntu to compile and work with this package.

import subprocess # for check_call

packs=[
	'swig', # for creating the interfaces
	'swig-examples', # for the examples
	'swig-doc', # for the documentation
	'gcc-doc', # for development
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)
