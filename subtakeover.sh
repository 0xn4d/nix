#!/bin/bash

echo ""
echo "Testing subdomains..."
echo ""
echo "Results:"
echo ""

for word in $(cat $2);do
host -t cname $word.$1 | grep "alias for"
done

echo ""
