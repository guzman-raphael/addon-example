#!/bin/sh

# generate OPENSSL private and pub keys
# openssl genpkey -out datajoint-dev.pem -algorithm rsa
# openssl rsa -in datajoint-dev.pem -outform PEM -pubout -out datajoint-dev.pem.pub

# generate GPG private and pub keys
# cat >config <<EOF
#      %echo Generating a basic OpenPGP key
#      %no-protection
#      Key-Type: RSA
#      Key-Length: 2048
#      Subkey-Type: RSA
#      Subkey-Length: 2048
#      Name-Real: DataJoint Dev
#      Name-Comment: For maintainer use.
#      Name-Email: support@datajoint.io
#      Expire-Date: 0
#      # Do a commit here, so that we can later print "done" :-)
#      %commit
#      %echo done
# EOF
# gpg --batch --generate-key config
# rm config
# gpg --export -a "DataJoint Dev" > datajoint-dev.public.key
# gpg --export-secret-key -a "DataJoint Dev" > datajoint-dev.private.key

# import GPG keys
# gpg --import datajoint-dev.private.key

# generate hash of filename and contents
# GIT_HASH=$(git ls-files -s mzaddon_type_student | git hash-object --stdin)
GIT_HASH=bad1c5a7c1b5b39a8d0d87146bc80afd41bd6580

# generate signature
printf $GIT_HASH | openssl dgst -sha256 -sign datajoint-dev.pem -out sign.sha256 -sigopt rsa_padding_mode:pss
openssl enc -base64 -in sign.sha256 -out sign.sha256.base64
rm sign.sha256

# verify signature
# openssl enc -base64 -d -in sign.sha256.base64 -out sign.sha256
# printf $GIT_HASH | openssl dgst -sha256 -verify ../core/datajoint-dev.pem.pub -signature sign.sha256 -sigopt rsa_padding_mode:pss
# rm sign.sha256