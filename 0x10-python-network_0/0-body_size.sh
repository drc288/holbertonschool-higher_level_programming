#!/bin/bash
# This script get the size of a header and printing, using curl
if [ $# == 1 ]; then
	curl -so /dev/null "$1" -w '%{size_request}\n'
fi
