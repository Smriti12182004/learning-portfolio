#!/bin/bash

# Check if the file name is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <filename> [count]"
    exit 1
fi

FILE=$1
COUNT=${2:-10}

tr -cs '[:alpha:]' '\n' < "$FILE" \
| tr '[:upper:]' '[:lower:]' \
| sort \
| uniq -c \
| sort -nr \
| head -n "$COUNT"