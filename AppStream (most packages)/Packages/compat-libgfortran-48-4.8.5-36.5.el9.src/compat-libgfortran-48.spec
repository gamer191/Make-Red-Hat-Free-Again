%global DATE 20150702
%global SVNREV 225304
# Note, gcc_release must be integer, if you want to add suffixes to
# %{release}, append them after %{gcc_release} on Release: line.
%global gcc_release 36
%global _unpackaged_files_terminate_build 0
%global _performance_build 1
%undefine _annotated_build
# Hardening slows the compiler way too much.
%undefine _hardened_build
# libgcc crashes left and right with LTO.
%global _lto_cflags %%{nil}
Summary: Compatibility Fortran runtime library version 4.8.5
Name: compat-libgfortran-48
%global gcc_version 4.8.5
Version: %{gcc_version}
Release: %{gcc_release}.5%{?dist}
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Languages
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-4_8-branch@%%{SVNREV} gcc-%%{version}-%%{DATE}
# tar cf - gcc-%%{version}-%%{DATE} | bzip2 -9 > gcc-%%{version}-%%{DATE}.tar.bz2
Source0: gcc-%{version}-%{DATE}.tar.bz2
URL: http://gcc.gnu.org
# Need binutils with -pie support >= 2.14.90.0.4-4
# Need binutils which can omit dot symbols and overlap .opd on ppc64 >= 2.15.91.0.2-4
# Need binutils which handle -msecure-plt on ppc >= 2.16.91.0.2-2
# Need binutils which support .weakref >= 2.16.91.0.3-1
# Need binutils which support --hash-style=gnu >= 2.17.50.0.2-7
# Need binutils which support mffgpr and mftgpr >= 2.17.50.0.2-8
# Need binutils which support --build-id >= 2.17.50.0.17-3
# Need binutils which support %gnu_unique_object >= 2.19.51.0.14
# Need binutils which support .cfi_sections >= 2.19.51.0.14-33
# Need binutils which support --no-add-needed >= 2.20.51.0.2-12
BuildRequires: binutils >= 2.20.51.0.2-12
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
BuildRequires: gcc, gcc-c++, make
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 2.2.1, libmpc-devel >= 0.8.1
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
# On ppc64, need omit dot symbols support and --non-overlapping-opd
# Need binutils that owns /usr/bin/c++filt
# Need binutils that support .weakref
# Need binutils that supports --hash-style=gnu
# Need binutils that support mffgpr/mftgpr
# Need binutils that support --build-id
# Need binutils that support %gnu_unique_object
# Need binutils that support .cfi_sections
# Need binutils that support --no-add-needed
Requires: binutils >= 2.20.51.0.2-12
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
Requires: glibc >= 2.3.90-35
%endif
%ifarch %{ix86} x86_64
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%if %{build_libquadmath}
# Use the system libquadmath.		  
BuildRequires: libquadmath >= 8.2.1
%endif

Patch0: gcc48-hack.patch
Patch1: gcc48-java-nomulti.patch
Patch2: gcc48-ppc32-retaddr.patch
Patch3: gcc48-rh330771.patch
Patch4: gcc48-i386-libgomp.patch
Patch5: gcc48-sparc-config-detection.patch
Patch6: gcc48-libgomp-omp_h-multilib.patch
Patch7: gcc48-libtool-no-rpath.patch
Patch10: gcc48-pr38757.patch
Patch12: gcc48-no-add-needed.patch
Patch13: gcc48-pr56564.patch
Patch14: gcc48-color-auto.patch
Patch15: gcc48-pr28865.patch
Patch16: gcc48-libgo-p224.patch
Patch17: gcc48-pr60010.patch
Patch18: gcc48-aarch64-ada.patch
Patch19: gcc48-aarch64-async-unw-tables.patch
Patch20: gcc48-aarch64-unwind-opt.patch
Patch21: gcc48-rh1243366.patch
Patch22: gcc48-rh1180633.patch
Patch23: gcc48-rh1278872.patch
Patch24: gcc48-pr67281.patch
Patch25: gcc48-pr68680.patch
Patch26: gcc48-rh1312436.patch
Patch27: gcc48-pr53477.patch
Patch28: gcc48-rh1296211.patch
Patch29: gcc48-rh1304449.patch
Patch30: gcc48-s390-z13.patch
Patch31: gcc48-rh1312850.patch
Patch32: gcc48-pr65142.patch
Patch33: gcc48-pr52714.patch
Patch34: gcc48-rh1344807.patch
Patch35: gcc48-libgomp-20160715.patch
Patch36: gcc48-pr63293.patch
Patch37: gcc48-pr72863.patch
Patch38: gcc48-pr78064.patch
Patch39: gcc48-pr62258.patch
Patch40: gcc48-rh1369183.patch
Patch41: gcc48-pr68184.patch
Patch42: gcc48-pr79439.patch
Patch43: gcc48-pr66731.patch
Patch44: gcc48-pr69116.patch
Patch45: gcc48-pr72747.patch
Patch46: gcc48-pr78796.patch
Patch47: gcc48-pr79969.patch
Patch48: gcc48-pr78875.patch
Patch49: gcc48-rh1402585.patch
Patch50: gcc48-pr70549.patch
Patch51: gcc48-rh1457969.patch
Patch52: gcc48-pr69644.patch
Patch53: gcc48-rh1487434.patch
Patch54: gcc48-rh1468546.patch
Patch55: gcc48-rh1469384.patch
Patch56: gcc48-rh1491395.patch
Patch57: gcc48-rh1482762.patch
Patch58: gcc48-pr77375.patch
Patch59: gcc48-pr77767.patch
Patch60: gcc48-pr78378.patch
Patch61: gcc48-pr80129.patch
Patch62: gcc48-pr80362.patch
Patch63: gcc48-pr80692.patch
Patch64: gcc48-pr82274.patch
Patch65: gcc48-pr78416.patch
Patch66: gcc48-rh1546728.patch
Patch67: gcc48-rh1555397.patch
Patch68: gcc48-pr81395.patch
Patch69: gcc48-pr72717.patch
Patch70: gcc48-pr66840.patch
Patch71: gcc48-rh1546372.patch
Patch72: gcc48-libc-name.patch
Patch73: gcc48-ucontext.patch
Patch74: gcc48-tweaks.patch

Patch1301: gcc48-rh1469697-1.patch
Patch1302: gcc48-rh1469697-2.patch
Patch1303: gcc48-rh1469697-3.patch
Patch1304: gcc48-rh1469697-4.patch
Patch1305: gcc48-rh1469697-5.patch
Patch1306: gcc48-rh1469697-6.patch
Patch1307: gcc48-rh1469697-7.patch
Patch1308: gcc48-rh1469697-8.patch
Patch1309: gcc48-rh1469697-9.patch
Patch1310: gcc48-rh1469697-10.patch
Patch1311: gcc48-rh1469697-11.patch
Patch1312: gcc48-rh1469697-12.patch
Patch1313: gcc48-rh1469697-13.patch
Patch1314: gcc48-rh1469697-14.patch
Patch1315: gcc48-rh1469697-15.patch
Patch1316: gcc48-rh1469697-16.patch
Patch1317: gcc48-rh1469697-17.patch
Patch1318: gcc48-rh1469697-18.patch
Patch1319: gcc48-rh1469697-19.patch
Patch1320: gcc48-rh1469697-20.patch
Patch1321: gcc48-rh1469697-21.patch
Patch1322: gcc48-rh1469697-22.patch
Patch1323: gcc48-rh1469697-23.patch
Patch1324: gcc48-rh1537828-1.patch
Patch1325: gcc48-rh1537828-2.patch
Patch1326: gcc48-rh1537828-3.patch
Patch1327: gcc48-rh1537828-4.patch
Patch1328: gcc48-rh1537828-5.patch
Patch1329: gcc48-rh1537828-10.patch

Patch1401: gcc48-rh1535655-1.patch
Patch1402: gcc48-rh1535655-2.patch
Patch1403: gcc48-rh1535655-3.patch
Patch1404: gcc48-rh1535655-4.patch
Patch1405: gcc48-rh1535655-5.patch
Patch1406: gcc48-rh1535655-6.patch
Patch1407: gcc48-rh1552021.patch
Patch1408: gcc48-rh1537828-6.patch
Patch1409: gcc48-rh1537828-7.patch
Patch1410: gcc48-rh1537828-8.patch
Patch1411: gcc48-rh1537828-9.patch

# On ARM EABI systems, we do want -gnueabi to be part of the
# target triple.
%ifnarch %{arm}
%global _gnu %{nil}
%endif
%ifarch sparcv9
%global gcc_target_platform sparc64-%{_vendor}-%{_target_os}
%endif
%ifarch ppc ppc64p7
%global gcc_target_platform ppc64-%{_vendor}-%{_target_os}
%endif
%ifnarch sparcv9 ppc ppc64p7
%global gcc_target_platform %{_target_platform}
%endif

%description
This package includes a Fortran 95 runtime library for compatibility
with GCC 4.8.x-RH compiled Fortran applications.

%prep
%setup -q -n gcc-%{version}-%{DATE}
%patch0 -p0 -b .hack~
%patch1 -p0 -b .java-nomulti~
%patch2 -p0 -b .ppc32-retaddr~
%patch3 -p0 -b .rh330771~
%patch4 -p0 -b .i386-libgomp~
%patch5 -p0 -b .sparc-config-detection~
%patch6 -p0 -b .libgomp-omp_h-multilib~
%patch7 -p0 -b .libtool-no-rpath~
%patch10 -p0 -b .pr38757~
%patch12 -p0 -b .no-add-needed~
%patch13 -p0 -b .pr56564~
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%patch14 -p0 -b .color-auto~
%endif
%patch15 -p0 -b .pr28865~
%patch16 -p0 -b .libgo-p224~
rm -f libgo/go/crypto/elliptic/p224{,_test}.go
%patch17 -p0 -b .pr60010~
%ifarch aarch64
%patch18 -p0 -b .aarch64-ada~
%endif
%patch19 -p0 -b .aarch64-async-unw-tables~
%patch20 -p0 -b .aarch64-unwind-opt~
%patch21 -p0 -b .rh1243366~
%patch22 -p0 -b .rh1180633~
%patch23 -p0 -b .rh1278872~
%patch24 -p0 -b .pr67281~
%patch25 -p0 -b .pr68680~
%patch26 -p0 -b .rh1312436~
%patch27 -p0 -b .pr53477~
touch -r %{PATCH27} libstdc++-v3/python/libstdcxx/v6/printers.py
%patch28 -p0 -b .rh1296211~
%patch29 -p0 -b .rh1304449~
%patch30 -p0 -b .s390-z13~
%patch31 -p0 -b .rh1312850~
%patch32 -p0 -b .pr65142~
%patch33 -p0 -b .pr52714~
%patch34 -p0 -b .rh1344807~
%patch35 -p0 -b .libgomp-20160715~
%patch36 -p0 -b .pr63293~
%patch37 -p0 -b .pr72863~
%patch38 -p0 -b .pr78064~
%patch39 -p0 -b .pr62258~
%patch40 -p0 -b .rh1369183~
%patch41 -p0 -b .pr68184~
%patch42 -p0 -b .pr79439~
%patch43 -p0 -b .pr66731~
%patch44 -p0 -b .pr69116~
%patch45 -p0 -b .pr72747~
%patch46 -p0 -b .pr78796~
%patch47 -p0 -b .pr79969~
%patch48 -p0 -b .pr78875~
%patch49 -p0 -b .rh1402585~
%patch50 -p0 -b .pr70549~
%patch51 -p0 -b .rh1457969~
%patch52 -p0 -b .pr69644~
%patch53 -p0 -b .rh1487434~
%patch54 -p0 -b .rh1468546~
%patch55 -p0 -b .rh1469384~
%patch56 -p0 -b .rh1491395~
%patch57 -p0 -b .rh1482762~
%patch58 -p0 -b .pr77375~
%patch59 -p0 -b .pr77767~
%patch60 -p0 -b .pr78378~
%patch61 -p0 -b .pr80129~
%patch62 -p0 -b .pr80362~
%patch63 -p0 -b .pr80692~
%patch64 -p0 -b .pr82274~
%patch65 -p0 -b .pr78416~
%patch66 -p0 -b .rh1546728~
%patch67 -p0 -b .rh1555397~
%patch68 -p0 -b .pr81395~
%patch69 -p0 -b .pr72717~
%patch70 -p0 -b .pr66840~
%patch71 -p0 -b .rh1546372~
%patch72 -p0 -b .libc-name~
%patch73 -p0 -b .ucontext~
%patch74 -p0 -b .tweaks~

%patch1301 -p1 -b .stack-clash-1~
%patch1302 -p1 -b .stack-clash-2~
%patch1303 -p1 -b .stack-clash-3~
%patch1304 -p1 -b .stack-clash-4~
%patch1305 -p1 -b .stack-clash-5~
%patch1306 -p1 -b .stack-clash-6~
%patch1307 -p1 -b .stack-clash-7~
%patch1308 -p1 -b .stack-clash-8~
%patch1309 -p1 -b .stack-clash-9~
%patch1310 -p1 -b .stack-clash-10~
%patch1311 -p1 -b .stack-clash-11~
%patch1312 -p1 -b .stack-clash-12~
%patch1313 -p1 -b .stack-clash-13~
%patch1314 -p1 -b .stack-clash-14~
%patch1315 -p1 -b .stack-clash-15~
%patch1316 -p1 -b .stack-clash-16~
%patch1317 -p1 -b .stack-clash-17~
%patch1318 -p1 -b .stack-clash-18~
%patch1319 -p1 -b .stack-clash-19~
%patch1320 -p1 -b .stack-clash-20~
%patch1321 -p1 -b .stack-clash-21~
%patch1322 -p1 -b .stack-clash-22~
%patch1323 -p1 -b .stack-clash-23~
%patch1324 -p1 -b .stack-clash-24~
%patch1325 -p1 -b .stack-clash-25~
%patch1326 -p1 -b .stack-clash-26~
%patch1327 -p1 -b .stack-clash-27~
%patch1328 -p1 -b .stack-clash-28~
%patch1329 -p1 -b .stack-clash-29~

%patch1401 -p1 -b .retpolines-1~
%patch1402 -p1 -b .retpolines-2~
%patch1403 -p1 -b .retpolines-3~
%patch1404 -p1 -b .retpolines-4~
%patch1405 -p1 -b .retpolines-5~
%patch1406 -p1 -b .retpolines-6~
%patch1407 -p0 -b .retpolines-7~
%patch1408 -p0 -b .retpolines-8~
%patch1409 -p1 -b .retpolines-9~
%patch1410 -p1 -b .retpolines-10~
%patch1411 -p1 -b .retpolines-11~

%build

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

rm -fr obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
# GCC 4.8 doesn't know these options, but redhat-rpm-config supplies them.
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -fstack-clash-protection -fcf-protection/ /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=x86-64-v2/-march=x86-64/g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
%ifarch aarch64
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mbranch-protection=standard//g'`
%endif
%ifarch s390x
# Same here.
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=z14 -mtune=z15//g'`
%endif
%ifarch ppc64le
# Same here.  GCC 4.8 doesn't grok power8.
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mcpu=power9 -mtune=power9/-mcpu=power7 -mtune=power7/g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables/' \
      ../gcc/Makefile.in
    ;;
esac
CC="$CC" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Werror=format-security / -Wformat -Werror=format-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--disable-bootstrap \
	--enable-shared --enable-threads=posix --enable-checking=release \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-linker-hash-style=gnu \
	--enable-languages=c,c++,fortran,lto \
	--disable-plugin --enable-initfini-array \
	--without-isl --without-cloog \
	--enable-gnu-indirect-function \
	--disable-libitm --disable-libsanitizer --disable-libgomp \
	--disable-libatomic --disable-libstdcxx-pch --disable-libssp \
	--disable-libmpx --disable-libcc1 \
	--disable-multilib \
%ifarch %{arm}
	--disable-sjlj-exceptions \
%endif
%ifarch ppc ppc64 ppc64le ppc64p7
	--enable-secureplt \
%endif
%ifarch sparc sparcv9 sparc64 ppc ppc64 ppc64le ppc64p7 s390 s390x alpha
	--with-long-double-128 \
%endif
%ifarch ppc64le
	--enable-targets=powerpcle-linux \
%endif
%ifarch ppc64le
       --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%ifarch ppc ppc64 ppc64p7
%if 0%{?rhel} >= 7
	--with-cpu-32=power7 --with-tune-32=power7 --with-cpu-64=power7 --with-tune-64=power7 \
%endif
%if 0%{?rhel} == 6
	--with-cpu-32=power4 --with-tune-32=power6 --with-cpu-64=power4 --with-tune-64=power6 \
%endif
%endif
%ifarch ppc
	--build=%{gcc_target_platform} --target=%{gcc_target_platform} --with-cpu=default32
%endif
%ifarch %{ix86} x86_64
	--with-tune=generic \
%endif
%if 0%{?rhel} >= 7
%ifarch %{ix86}
	--with-arch=x86-64 \
%endif
%ifarch x86_64
	--with-arch_32=x86-64 \
%endif
%else
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%endif
%ifarch s390 s390x
%if 0%{?rhel} >= 7
	--with-arch=z196 --with-tune=zEC12 --enable-decimal-float \
%else
	--with-arch=z9-109 --with-tune=z10 --enable-decimal-float \
%endif
%endif
%ifarch armv7hl
	--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a \
	--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux \
%endif
%ifnarch sparc sparcv9 ppc
	--build=%{gcc_target_platform}
%endif

make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS" LDFLAGS_FOR_TARGET=-Wl,-z,relro,-z,now MAKEINFO=missing

%install
rm -fr %{buildroot}
cd obj-%{gcc_target_platform}
mkdir -p %{buildroot}/%{_libdir}

# Do this so that the resulting .so doesn't have a bogus RPATH.
cd %{gcc_target_platform}/libgfortran/
mkdir temp
%if %{build_libquadmath}
# Link against the system libquadmath.
# ??? I don't know what I am doing.
mkdir libquadmath
echo '/* GNU ld script
   Use the system libquadmath.so.  */
INPUT ( %{_libdir}/libquadmath.so.0.0.0 )' > libquadmath/libquadmath.so
export LIBRARY_PATH=`pwd`/libquadmath
%endif
make install DESTDIR=`pwd`/temp
cp -a temp/usr/%{_lib}/libgfortran.so.3* %{buildroot}/%{_libdir}
cd ../..

%check
cd obj-%{gcc_target_platform}

# Run the Fortran tests.
make %{?_smp_mflags} -k -C gcc check-gfortran ALT_CC_UNDER_TEST=gcc ALT_CXX_UNDER_TEST=g++ || :
echo ====================TESTING=========================
( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | bzip2 -9c \
  | uuencode testlogs-%{_target_platform}.tar.bz2 || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libgfortran.so.3*

%changelog
* Wed Jan 26 2022 Marek Polacek <polacek@redhat.com> - 4.8.5-36.5
- build with -Wl,-z,relro,-z,now (#2044834)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 4.8.5-36.4.1
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Aug  9 2021 Marek Polacek <polacek@redhat.com> - 4.8.5-36.4
- bump for rebuild

* Fri May 14 2021 Marek Polacek <polacek@redhat.com> - 4.8.5-36.3
- invoke make with MAKEINFO=missing (#1951315)

* Mon Apr 19 2021 Marek Polacek <polacek@redhat.com> - 4.8.5-36.2
- use power7 cpu/tuning and filter out -march=z14 -mtune=z15 (#1951315)

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 4.8.5-36.1.1
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 20 2021 Marek Polacek <polacek@redhat.com> 4.8.5-36
- new compat library
