#!/bin/bash
python mapper-tf-2.py < wiki-test.txt 2> map-tf.err | (unset LC_ALL; LC_CTYPE=en_US.UTF-8 LC_COLLATE=C sort -t$'\t' -k1,2) | python reducer-tf-2.py > tf.out

