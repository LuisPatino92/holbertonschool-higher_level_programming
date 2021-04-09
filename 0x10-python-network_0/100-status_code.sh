#!/bin/bash
# Post with body parameters
curl -o /dev/null -s -w "%{http_code}" "$1"
