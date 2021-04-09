#!/bin/bash
# Post with body parameters
curl -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1" 2> dev/null
