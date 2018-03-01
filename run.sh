#!/bin/bash
for i in inputs/*; do python3 solution.py $i; done
zip -r *.py{.zip,}