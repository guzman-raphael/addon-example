#!/bin/sh

# generate private and pub keys
# ssh-keygen -t rsa -C "datajoint-dev" -f ./datajoint-dev.pem -N ""

# generate hash of contents
git ls-files -s mzaddon_type_student | git hash-object --stdin