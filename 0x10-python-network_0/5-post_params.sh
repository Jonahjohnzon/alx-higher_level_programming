#!/bin/bash
# Bash script send a POST request given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
