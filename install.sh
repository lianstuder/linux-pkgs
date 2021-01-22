#!/bin/bash

filename="./packages.txt"

while read line
do
    if [ "$file" != "END" ]; then
        sudo emerge "$line"
    fi
done < $filename