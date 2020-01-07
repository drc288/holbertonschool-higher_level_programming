#!/bin/bash
# This script  using GET method and add header
# variable
curl -H 'X-HolbertonSchool-User-Id: 98' -X GET "$1"
