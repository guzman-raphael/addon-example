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

cert() {

    # generate hash of filename and contents
    git add . --all
    GIT_HASH=$(git ls-files -s $1 | git hash-object --stdin)
    # GIT_HASH=bad1c5a7c1b5b39a8d0d87146bc80afd41bd6580

    # generate signature
    # printf $GIT_HASH
    printf $GIT_HASH | openssl dgst -sha256 -sign datajoint-dev.pem -out $1.sigbin -sigopt rsa_padding_mode:pss
    openssl enc -base64 -in $1.sigbin -out $1.sig
    rm $1.sigbin

    # verify signature
    # openssl enc -base64 -d -in data_files/mzaddon_type_student.sig -out mzaddon_type_student.sigbin
    # printf $GIT_HASH | openssl dgst -sha256 -verify ../core/datajoint-dev.pem.pub -signature mzaddon_type_student.sigbin -sigopt rsa_padding_mode:pss
    # rm mzaddon_type_student.sigbin

    # Display Sig
    echo '----SIGNATURE----'
    cat $1.sig
    echo '--------'
}

upload() {
    # build package
    python setup.py sdist bdist_wheel

    # add sig to wheel
    wheel unpack dist/$1*.whl --dest dist/
    rm dist/$1*.whl
    cp $1.sig dist/$1*/$1-*/
    wheel_dir=$(ls dist | grep $1 | grep -v "tar")
    wheel pack dist/${wheel_dir} --dest-dir dist
    rm -R dist/${wheel_dir}

    # add sig to tarball
    tar -xzvf dist/$1*.tar.gz -C dist/
    tar_name=$(ls dist | grep tar.gz)
    rm dist/${tar_name}
    cp $1.sig dist/$1*/$1.*/
    tar_dir=$(ls dist | grep $1 | grep -v "whl")
    cd dist
    tar -czvf ${tar_name} ${tar_dir}
    cd ..
    rm -R dist/${tar_dir}

    # upload (with GPG)
    # python -m twine upload -s -i "DataJoint Dev" --repository-url https://test.pypi.org/legacy/ dist/*

    # upload (normal)
    python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
}

rm -R build dist ${2}.egg-info
"$1" $2