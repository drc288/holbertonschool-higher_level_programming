#!/bin/bash
# This script get the head if the code status is 200
STATUS=$(curl -o /dev/null -s -w "%{http_code}\n" "$1")
if [ "$STATUS" -eq 200 ]; then
	curl -o - "$1"
fi
