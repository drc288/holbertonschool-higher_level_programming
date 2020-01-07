#!/bin/bash
# This script  using GET method and add header
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
