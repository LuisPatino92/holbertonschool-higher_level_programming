#!/bin/bash
# This scripts prints the length of the body of a HTTP response
curl -s "$1" | wc -c
