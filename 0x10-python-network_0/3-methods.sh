#!/bin/bash
# This script print the methods of a page
curl -is -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
