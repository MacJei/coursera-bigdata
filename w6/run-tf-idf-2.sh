#!/bin/bash

cat tf.out idf.out > tf-idf.in
python mapper-tf-idf-red-2.py < tf-idf.in 2> map-tf-idf.err | (unset LC_ALL; LC_CTYPE=en_US.UTF-8 LC_COLLATE=C sort -t$'\t' -k1,2) | python reducer-tf-idf-2.py > tf-idf.out

