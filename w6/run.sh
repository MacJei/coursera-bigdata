#!/bin/bash
python mapper-tf.py < wiki-test.txt 2> map.err | (unset LC_ALL; LC_CTYPE=en_US.UTF-8 LC_COLLATE=C sort -t$'\t' -k1,2) | python reducer-tf.py 

