#! /bin/sh
v=20200406
s=texlive-$v-source.tar.xz
p=${s%.tar.xz}

# get the texlive original source
if [ ! -f $s ] ; then
  echo download $s, please wait...
  wget https://ftp.tu-chemnitz.de/pub/tug/historic/systems/texlive/2020/$s
  if [ ! -f $s ] ; then
    echo download $s failed!
    exit 1
  fi
fi
# remove old source
if [ -d $p ] ; then
  rm -fr $p
fi

echo extracting the $s...
if ( ! tar Jxf $s ) ; then
  echo $s failed, cannot be extracted
  exit 1
fi

# remove files with bad licenses, don't embeded zziplib but build with system lib
rm -rf $p/libs/zziplib
rm -rf $p/texk/ps2pk

# create clean texlive source
echo create the clean texlive source, please wait...
if ( tar Jcf $p-clean.tar.xz $p) ; then
  echo clean texlive source $p-clean.tar.xz is created.
else
  echo failed, clean texlive source $p-clean.tar.xz cannot be created.
fi
