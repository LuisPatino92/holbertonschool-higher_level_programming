#!/bin/bash
# This Shows the allowed verbs
curl -sI "$1" | grep Allow | cut -d " " -f 2-
