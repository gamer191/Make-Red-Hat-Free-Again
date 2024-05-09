#!/bin/sh

DIRNAME=libxkbcommon-$( date +%Y%m%d )

rm -rf $DIRNAME
git clone https://github.com/xkbcommon/libxkbcommon $DIRNAME
cd $DIRNAME
if [ -z "$1" ]; then
    git log | head -1
else
    git checkout $1
fi
git log | head -1 | awk '{ print $2 }' > ../commitid
git repack -a -d
cd ..
tar Jcf $DIRNAME.tar.xz $DIRNAME
rm -rf $DIRNAME
