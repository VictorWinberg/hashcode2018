#!/bin/bash
for i in inputs/*; do python3 victor.py $i; done
zip -r *.py{.zip,}