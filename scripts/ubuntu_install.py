#!/usr/bin/python

# this scrip will install all the required packages that you need on
# ubuntu to compile and work with this package.

import subprocess

packs=[
	'swig', # for creating the interfaces
	'swig-examples', # for the examples
	'swig-doc', # for the documentation
	'gcc-doc', # for development
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)