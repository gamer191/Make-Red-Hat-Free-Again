#!/usr/bin/bash


VERSION=$1

if [ "${VERSION:="*"}" == "*" ]
then
  echo "Define a version of hplip as an argument."
  exit 1
fi

# extract the original tarball
tar -xaf hplip-$VERSION.tar.gz || exit 1

# remove unwanted files
rm hplip-$VERSION/prnt/hpcups/ErnieFilter.{cpp,h} hplip-$VERSION/prnt/hpijs/ernieplatform.h || exit 1

# compress into a new tarball
tar -cjvf hplip-$VERSION-repack.tar.gz hplip-$VERSION || exit 1

# upload a new source tarball
#fedpkg new-sources hplip-$VERSION-repack.tar.gz || exit 1
