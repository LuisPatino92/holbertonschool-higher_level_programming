#!/bin/bash
# Sending a JSON from a file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
