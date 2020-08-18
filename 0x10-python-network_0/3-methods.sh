#!/bin/bash
# methods
curl -sI $1 | grep "Allow" | awk -F " " '{$1="";print $0}' | tail -c +2
