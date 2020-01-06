#!/bin/bash
# This script get the size of a header and printing, using curl
# #############################################################
# #            get the content lnght of argv[0]               #
# #############################################################
# Get the url of argv
URL="$1"
# Get the curl of the URL, get the data of content length
# and print the second line
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
