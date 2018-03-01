#!/bin/bash
for i in inputs/*; do python3 closest.py $i; done
zip -r *.py{.zip,}