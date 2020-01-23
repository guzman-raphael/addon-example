#!/bin/sh

# generate OPENSSL private and pub keys
openssl genpkey -out datajoint-dev.pem -algorithm rsa
openssl rsa -in datajoint-dev.pem -outform PEM -pubout -out datajoint-dev.pem.pub

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
GIT_HASH=$(git ls-files -s mzaddon_type_student | git hash-object --stdin)

# generate signature
echo $GIT_HASH | openssl dgst -sha256 -sign datajoint-dev.pem -out sign.sha256
openssl enc -base64 -in sign.sha256 -out sign.sha256.base64
rm sign.sha256

# verify signature
# openssl enc -base64 -d -in sign.sha256.base64 -out sign.sha256
# echo $GIT_HASH | openssl dgst -sha256 -verify datajoint-dev.pem.pub -signature sign.sha256
# rm sign.sha256