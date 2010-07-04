#!/bin/sh

# this is a small script which gets the requirements for autoconf
# on a standard linux system. If you do not have these files, and
# as a consequence this script fails, then get them off the net

# you will not need this as part of a regular install since you
# probably got them with the package and the configure script

cp /usr/share/automake/{install-sh,config.sub,config.guess} .
