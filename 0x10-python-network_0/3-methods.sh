#!/bin/bash
# This scripts prints the body of a get following all the redirections
curl -I "$1" 2> dev/null | grep  "Allow: " | cut -d " " -f 2-5
