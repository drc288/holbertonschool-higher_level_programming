#!/bin/bash
# This script get the size of a header and printing, using curl
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
