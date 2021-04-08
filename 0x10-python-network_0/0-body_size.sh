#!/bin/bash
# This scripts prints the length of the body of a HTTP response
expr $(echo $(curl 0.0.0.0:5000 2> /dev/null) | wc -c) - 1
