#!/bin/bash

curl $1 | tar -xzvf - #the dash tells tar to read from stdin instead of expecti

for i in *.tsv; do
  output="${i%.tsv}.csv" #changes the end of the file to be .csv instead 
  sed 's/'$'\t''/,/g' "$i" > "$output" #the i variable is the iterator
done
