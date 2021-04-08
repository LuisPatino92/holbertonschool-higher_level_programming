#!/bin/bash
# This scripts prints the length of the body of a HTTP response
expr $(echo $(curl "$1" 2> /dev/null) | wc -c) - 1
