#!/bin/bash
# This script using the method POST
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
