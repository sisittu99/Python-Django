#!/bin/sh

curl $1 | grep href | cut -d '"' -f 2
