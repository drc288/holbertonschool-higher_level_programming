#!/bin/bash
# This script get the size of a header and printing, using curl
curl -so /dev/null "$1" -w '%{size_request}\n'
