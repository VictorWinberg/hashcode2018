#!/bin/bash
for i in inputs/*; do python3 $1 $i; done
zip -r *.py{.zip,}