#!/bin/bash
# Send a GET request to given URL  header variable.
curl -s "$1" | wc -c
