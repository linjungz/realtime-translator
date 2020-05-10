#!/bin/sh

file_list=(
    css/font-awesome.css
    css/shoelace.css
    css/styles.css
    lib/jquery.js
    dist/main.js
    lib/aws-sdk-2.668.0.min.js
    lib/identity_pool.js
    index.html
)

bucket_name="realtime-translator-web"

for file in "${file_list[@]}"; do
    aws s3 cp $file s3://${bucket_name}/$file --acl public-read
done