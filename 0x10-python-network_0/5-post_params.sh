#!/bin/bash
# Post with body parameters
curl "$1" -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' 2> dev/null
