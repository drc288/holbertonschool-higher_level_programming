#!/bin/bash
# This script  using GET method and add header
# variable
curl -H "X-HolbertonSchool-User-Id: 98" -Xs GET "$1"
