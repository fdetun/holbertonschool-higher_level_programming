#!/bin/bash
# curl size

curl -sI "$1" | grep "Content-Length:" | awk -F " " '{print $2}'
