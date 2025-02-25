#!/bin/bash

local_file=$1
bucket_name=$2
expiration=$3

aws s3 cp $local_file s3://$bucket_name
aws s3 presign --expires-in $expiration s3://$bucket_name/$local_file
