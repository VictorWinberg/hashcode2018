#!/bin/bash
for i in inputs/*; do python3 smart.py $i; done
zip -r *.py{.zip,}
