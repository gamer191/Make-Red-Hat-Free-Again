
%global pkgname   dirsrv
%global srcname   389-ds-base

# Exclude i686 bit arches
ExcludeArch: i686 

# If perl-Socket-2.000 or newer is available, set 0 to use_Socket6.
%global use_Socket6 0

%global use_asan 0
%global use_rust 1
%global bundle_jemalloc 1
%if %{use_asan}
%global bundle_jemalloc 0
%endif

%if %{bundle_jemalloc}
%global jemalloc_name jemalloc
%global jemalloc_ver 5.3.0
%global __provides_exclude ^libjemalloc\\.so.*$
%endif

# Use Clang instead of GCC
%global use_clang 0

# Build cockpit plugin
%global use_cockpit 0

# fedora 15 and later uses tmpfiles.d
# otherwise, comment this out
%{!?with_tmpfiles_d: %global with_tmpfiles_d %{_sysconfdir}/tmpfiles.d}

# systemd support
%global groupname %{pkgname}.target

# set PIE flag
%global _hardened_build 1

# Filter argparse-manpage from autogenerated package Requires
%global __requires_exclude ^python.*argparse-manpage

# Force to require nss version greater or equal as the version available at the build time
# See bz1986327
%define dirsrv_requires_ge()  %(LC_ALL="C" echo '%*' | xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

Summary:          389 Directory Server (base)
Name:             389-ds-base
Version:          2.4.5
Release:          5%{?dist}
License:          GPLv3+ and (ASL 2.0 or MIT) and MIT and (Unlicense or MIT) and (0BSD or MIT or ASL 2.0) and MPLv2.0 and ASL 2.0 and (MIT or zlib or ASL 2.0) and ((MIT or ASL 2.0) and Unicode-DFS-2016) and (ASL 2.0 or Boost) and BSD
URL:              https://www.port389.org
Conflicts:        selinux-policy-base < 3.9.8
Conflicts:        freeipa-server < 4.0.3
Obsoletes:        %{name} <= 1.4.0.9
Obsoletes:        %{name}-legacy-tools < 1.4.4.6
Obsoletes:        %{name}-legacy-tools-debuginfo < 1.4.4.6
Provides:         ldif2ldbm >= 0

##### Bundled cargo crates list - START #####
Provides:  bundled(crate(addr2line)) = 0.21.0
Provides:  bundled(crate(adler)) = 1.0.2
Provides:  bundled(crate(ahash)) = 0.7.7
Provides:  bundled(crate(ansi_term)) = 0.12.1
Provides:  bundled(crate(atty)) = 0.2.14
Provides:  bundled(crate(autocfg)) = 1.1.0
Provides:  bundled(crate(backtrace)) = 0.3.69
Provides:  bundled(crate(base64)) = 0.13.1
Provides:  bundled(crate(bitflags)) = 1.3.2
Provides:  bundled(crate(bitflags)) = 2.4.1
Provides:  bundled(crate(byteorder)) = 1.5.0
Provides:  bundled(crate(cbindgen)) = 0.9.1
Provides:  bundled(crate(cc)) = 1.0.83
Provides:  bundled(crate(cfg-if)) = 1.0.0
Provides:  bundled(crate(clap)) = 2.34.0
Provides:  bundled(crate(concread)) = 0.2.21
Provides:  bundled(crate(crossbeam)) = 0.8.4
Provides:  bundled(crate(crossbeam-channel)) = 0.5.11
Provides:  bundled(crate(crossbeam-deque)) = 0.8.5
Provides:  bundled(crate(crossbeam-epoch)) = 0.9.18
Provides:  bundled(crate(crossbeam-queue)) = 0.3.11
Provides:  bundled(crate(crossbeam-utils)) = 0.8.19
Provides:  bundled(crate(entryuuid)) = 0.1.0
Provides:  bundled(crate(entryuuid_syntax)) = 0.1.0
Provides:  bundled(crate(errno)) = 0.3.8
Provides:  bundled(crate(fastrand)) = 2.0.1
Provides:  bundled(crate(fernet)) = 0.1.4
Provides:  bundled(crate(foreign-types)) = 0.3.2
Provides:  bundled(crate(foreign-types-shared)) = 0.1.1
Provides:  bundled(crate(getrandom)) = 0.2.12
Provides:  bundled(crate(gimli)) = 0.28.1
Provides:  bundled(crate(hashbrown)) = 0.12.3
Provides:  bundled(crate(hermit-abi)) = 0.1.19
Provides:  bundled(crate(instant)) = 0.1.12
Provides:  bundled(crate(itoa)) = 1.0.10
Provides:  bundled(crate(jobserver)) = 0.1.27
Provides:  bundled(crate(libc)) = 0.2.152
Provides:  bundled(crate(librnsslapd)) = 0.1.0
Provides:  bundled(crate(librslapd)) = 0.1.0
Provides:  bundled(crate(linux-raw-sys)) = 0.4.12
Provides:  bundled(crate(lock_api)) = 0.4.11
Provides:  bundled(crate(log)) = 0.4.20
Provides:  bundled(crate(lru)) = 0.7.8
Provides:  bundled(crate(memchr)) = 2.7.1
Provides:  bundled(crate(miniz_oxide)) = 0.7.1
Provides:  bundled(crate(object)) = 0.32.2
Provides:  bundled(crate(once_cell)) = 1.19.0
Provides:  bundled(crate(openssl)) = 0.10.62
Provides:  bundled(crate(openssl-macros)) = 0.1.1
Provides:  bundled(crate(openssl-sys)) = 0.9.98
Provides:  bundled(crate(parking_lot)) = 0.11.2
Provides:  bundled(crate(parking_lot_core)) = 0.8.6
Provides:  bundled(crate(paste)) = 0.1.18
Provides:  bundled(crate(paste-impl)) = 0.1.18
Provides:  bundled(crate(pin-project-lite)) = 0.2.13
Provides:  bundled(crate(pkg-config)) = 0.3.28
Provides:  bundled(crate(ppv-lite86)) = 0.2.17
Provides:  bundled(crate(proc-macro-hack)) = 0.5.20+deprecated
Provides:  bundled(crate(proc-macro2)) = 1.0.76
Provides:  bundled(crate(pwdchan)) = 0.1.0
Provides:  bundled(crate(quote)) = 1.0.35
Provides:  bundled(crate(rand)) = 0.8.5
Provides:  bundled(crate(rand_chacha)) = 0.3.1
Provides:  bundled(crate(rand_core)) = 0.6.4
Provides:  bundled(crate(redox_syscall)) = 0.2.16
Provides:  bundled(crate(redox_syscall)) = 0.4.1
Provides:  bundled(crate(rustc-demangle)) = 0.1.23
Provides:  bundled(crate(rustix)) = 0.38.28
Provides:  bundled(crate(ryu)) = 1.0.16
Provides:  bundled(crate(scopeguard)) = 1.2.0
Provides:  bundled(crate(serde)) = 1.0.195
Provides:  bundled(crate(serde_derive)) = 1.0.195
Provides:  bundled(crate(serde_json)) = 1.0.111
Provides:  bundled(crate(slapd)) = 0.1.0
Provides:  bundled(crate(slapi_r_plugin)) = 0.1.0
Provides:  bundled(crate(smallvec)) = 1.11.2
Provides:  bundled(crate(strsim)) = 0.8.0
Provides:  bundled(crate(syn)) = 1.0.109
Provides:  bundled(crate(syn)) = 2.0.48
Provides:  bundled(crate(tempfile)) = 3.9.0
Provides:  bundled(crate(textwrap)) = 0.11.0
Provides:  bundled(crate(tokio)) = 1.35.1
Provides:  bundled(crate(tokio-macros)) = 2.2.0
Provides:  bundled(crate(toml)) = 0.5.11
Provides:  bundled(crate(unicode-ident)) = 1.0.12
Provides:  bundled(crate(unicode-width)) = 0.1.11
Provides:  bundled(crate(uuid)) = 0.8.2
Provides:  bundled(crate(vcpkg)) = 0.2.15
Provides:  bundled(crate(vec_map)) = 0.8.2
Provides:  bundled(crate(version_check)) = 0.9.4
Provides:  bundled(crate(wasi)) = 0.11.0+wasi_snapshot_preview1
Provides:  bundled(crate(winapi)) = 0.3.9
Provides:  bundled(crate(winapi-i686-pc-windows-gnu)) = 0.4.0
Provides:  bundled(crate(winapi-x86_64-pc-windows-gnu)) = 0.4.0
Provides:  bundled(crate(windows-sys)) = 0.52.0
Provides:  bundled(crate(windows-targets)) = 0.52.0
Provides:  bundled(crate(windows_aarch64_gnullvm)) = 0.52.0
Provides:  bundled(crate(windows_aarch64_msvc)) = 0.52.0
Provides:  bundled(crate(windows_i686_gnu)) = 0.52.0
Provides:  bundled(crate(windows_i686_msvc)) = 0.52.0
Provides:  bundled(crate(windows_x86_64_gnu)) = 0.52.0
Provides:  bundled(crate(windows_x86_64_gnullvm)) = 0.52.0
Provides:  bundled(crate(windows_x86_64_msvc)) = 0.52.0
Provides:  bundled(crate(zeroize)) = 1.7.0
Provides:  bundled(crate(zeroize_derive)) = 1.4.2
##### Bundled cargo crates list - END #####

BuildRequires:    nspr-devel >= 4.32
BuildRequires:    nss-devel >= 3.67.0-7

BuildRequires:    openldap-devel
BuildRequires:    lmdb-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    icu
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    cracklib-devel
BuildRequires:    json-c-devel
%if %{use_clang}
BuildRequires:    libatomic
BuildRequires:    clang
%else
BuildRequires:    gcc
BuildRequires:    gcc-c++
%endif
# The following are needed to build the snmp ldap-agent
BuildRequires:    net-snmp-devel
BuildRequires:    lm_sensors-devel
BuildRequires:    bzip2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
# the following is for the pam passthru auth plug-in
BuildRequires:    pam-devel
BuildRequires:    systemd-units
BuildRequires:    systemd-devel
BuildRequires:    systemd-rpm-macros
%{?sysusers_requires_compat}
%if %{use_asan}
BuildRequires:    libasan
%endif
# If rust is enabled
%if %{use_rust}
BuildRequires: cargo
BuildRequires: rust
%endif
BuildRequires:    pkgconfig
BuildRequires:    pkgconfig(systemd)
BuildRequires:    pkgconfig(krb5)

# Needed to support regeneration of the autotool artifacts.
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
# For our documentation
BuildRequires:    doxygen
# For tests!
BuildRequires:    libcmocka-devel
BuildRequires:    libevent-devel
# For lib389 and related components
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    python%{python3_pkgversion}-setuptools
BuildRequires:    python%{python3_pkgversion}-ldap
BuildRequires:    python%{python3_pkgversion}-six
BuildRequires:    python%{python3_pkgversion}-pyasn1
BuildRequires:    python%{python3_pkgversion}-pyasn1-modules
BuildRequires:    python%{python3_pkgversion}-dateutil
BuildRequires:    python%{python3_pkgversion}-argcomplete
BuildRequires:    python%{python3_pkgversion}-argparse-manpage
BuildRequires:    python%{python3_pkgversion}-libselinux
BuildRequires:    python%{python3_pkgversion}-policycoreutils
BuildRequires:    python%{python3_pkgversion}-cryptography

# For cockpit
%if %{use_cockpit}
BuildRequires:    rsync
%endif

Requires:         %{name}-libs = %{version}-%{release}
Requires:         python%{python3_pkgversion}-lib389 = %{version}-%{release}
Requires:         lmdb-libs

# this is needed for using semanage from our setup scripts
Requires:         policycoreutils-python-utils
Requires:         /usr/sbin/semanage
Requires:         libsemanage-python%{python3_pkgversion}
Requires:         selinux-policy >= 3.14.1-29

# the following are needed for some of our scripts
Requires:         openldap-clients
Requires:         /usr/bin/c_rehash
Requires:         python%{python3_pkgversion}-ldap
Requires:         acl
Requires:         zlib
Requires:         json-c

# this is needed to setup SSL if you are not using the
# administration server package
Requires:         nspr >= 4.32
Requires:         nss >= 3.67.0-7
Requires:         nss-tools
%dirsrv_requires_ge nss

# these are not found by the auto-dependency method
# they are required to support the mandatory LDAP SASL mechs
Requires:         cyrus-sasl-gssapi
Requires:         cyrus-sasl-md5
Requires:         cyrus-sasl-plain

# this is needed for verify-db.pl
Requires:         libdb-utils

# Needed for password dictionary checks
Requires:         cracklib-dicts

# Needed by logconv.pl
Requires:         perl-DB_File
Requires:         perl-Archive-Tar
Requires:         perl-debugger
Requires:         perl-sigtrap

# Picks up our systemd deps.
%{?systemd_requires}

Obsoletes:        %{name} <= 1.3.5.4

Source0:          https://releases.pagure.org/389-ds-base/%{name}-%{version}.tar.bz2
# 389-ds-git.sh should be used to generate the source tarball from git
Source1:          %{name}-git.sh
Source2:          %{name}-devel.README
%if %{bundle_jemalloc}
Source3:          https://github.com/jemalloc/%{jemalloc_name}/releases/download/%{jemalloc_ver}/%{jemalloc_name}-%{jemalloc_ver}.tar.bz2
%endif
Source4:          389-ds-base.sysusers
Patch0:           0001-Issue-3527-Support-HAProxy-and-Instance-on-the-same-.patch


%description
389 Directory Server is an LDAPv3 compliant server.  The base package includes
the LDAP server and command line utilities for server administration.
%if %{use_asan}
WARNING! This build is linked to Address Sanitisation libraries. This probably
isn't what you want. Please contact support immediately.
Please see http://seclists.org/oss-sec/2016/q1/363 for more information.
%endif

%package          libs
Summary:          Core libraries for 389 Directory Server
BuildRequires:    nspr >= 4.32
BuildRequires:    nss >= 3.67.0-7
BuildRequires:    openldap-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    libtalloc-devel
BuildRequires:    libevent-devel
BuildRequires:    libtevent-devel
Requires:         krb5-libs
Requires:         libevent
BuildRequires:    systemd-devel
BuildRequires:    make
Provides:         svrcore = 4.1.4
Conflicts:        svrcore
Obsoletes:        svrcore <= 4.1.3

%description      libs
Core libraries for the 389 Directory Server base package.  These libraries
are used by the main package and the -devel package.  This allows the -devel
package to be installed with just the -libs package and without the main package.

%package          devel
Summary:          Development libraries for 389 Directory Server
Requires:         %{name}-libs = %{version}-%{release}
Requires:         pkgconfig
Requires:         nspr-devel
Requires:         nss-devel >= 3.34
Requires:         openldap-devel
Requires:         libtalloc
Requires:         libevent
Requires:         libtevent
Requires:         systemd-libs
Provides:         svrcore-devel = 4.1.4
Conflicts:        svrcore-devel
Obsoletes:        svrcore-devel <= 4.1.3

%description      devel
Development Libraries and headers for the 389 Directory Server base package.

%package          snmp
Summary:          SNMP Agent for 389 Directory Server
Requires:         %{name} = %{version}-%{release}

Obsoletes:        %{name} <= 1.4.0.0

%description      snmp
SNMP Agent for the 389 Directory Server base package.

%package -n python%{python3_pkgversion}-lib389
Summary:  A library for accessing, testing, and configuring the 389 Directory Server
BuildArch:        noarch
Requires: openssl
Requires: iproute
Requires: 389-ds-base
Recommends: bash-completion
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-ldap
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-pyasn1
Requires: python%{python3_pkgversion}-pyasn1-modules
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-argcomplete
Requires: python%{python3_pkgversion}-libselinux
Requires: python%{python3_pkgversion}-setuptools
Requires: python%{python3_pkgversion}-cryptography
%{?python_provide:%python_provide python%{python3_pkgversion}-lib389}

%description -n python%{python3_pkgversion}-lib389
This module contains tools and libraries for accessing, testing,
 and configuring the 389 Directory Server.

%if %{use_cockpit}
%package -n cockpit-389-ds
Summary:          Cockpit UI Plugin for configuring and administering the 389 Directory Server
BuildArch:        noarch
Requires:         cockpit
Requires:         389-ds-base
Requires:         python%{python3_pkgversion}
Requires:         python%{python3_pkgversion}-lib389

%description -n cockpit-389-ds
A cockpit UI Plugin for configuring and administering the 389 Directory Server
%endif

%prep

%autosetup -p1 -v -n %{name}-%{version}
%if %{bundle_jemalloc}
%setup -q -n %{name}-%{version} -T -D -b 3
%endif

cp %{SOURCE2} README.devel

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find vendor -name .cargo-checksum.json \
  -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'

%build

OPENLDAP_FLAG="--with-openldap"
%{?with_tmpfiles_d: TMPFILES_FLAG="--with-tmpfiles-d=%{with_tmpfiles_d}"}
# hack hack hack https://bugzilla.redhat.com/show_bug.cgi?id=833529
NSSARGS="--with-nss-lib=%{_libdir} --with-nss-inc=%{_includedir}/nss3"

%if %{use_asan}
ASAN_FLAGS="--enable-asan --enable-debug"
%endif

%if %{use_rust}
RUST_FLAGS="--enable-rust --enable-rust-offline"
%endif

%if !%{use_cockpit}
COCKPIT_FLAGS="--disable-cockpit"
%endif 

%if %{use_clang}
export CC=clang
export CXX=clang++
CLANG_FLAGS="--enable-clang"
%endif

%if %{bundle_jemalloc}
# Override page size, bz #1545539
# 4K
%ifarch %ix86 %arm x86_64 s390x
%define lg_page --with-lg-page=12
%endif

# 64K
%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Override huge page size on aarch64
# 2M instead of 512M
%ifarch aarch64
%define lg_hugepage --with-lg-hugepage=21
%endif

# Build jemalloc
pushd ../%{jemalloc_name}-%{jemalloc_ver}
%configure \
        --libdir=%{_libdir}/%{pkgname}/lib \
        --bindir=%{_libdir}/%{pkgname}/bin \
        --enable-prof
make %{?_smp_mflags}
popd
%endif

# Enforce strict linking
%define _ld_strict_symbol_defs 1

# Rebuild the autotool artifacts now.
autoreconf -fiv

%configure --enable-autobind --with-selinux $TMPFILES_FLAG \
           --with-systemd \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdsystemconfdir=%{_sysconfdir}/systemd/system \
           --with-systemdgroupname=%{groupname}  \
           --libexecdir=%{_libexecdir}/%{pkgname} \
           $NSSARGS $ASAN_FLAGS $RUST_FLAGS $CLANG_FLAGS $COCKPIT_FLAGS \
           --enable-cmocka --enable-new-dtags --with-libldap-r=no


# lib389
make src/lib389/setup.py
pushd ./src/lib389
%py3_build
popd
# argparse-manpage dynamic man pages have hardcoded man v1 in header,
# need to change it to v8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsconf.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsctl.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dsidm.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}/src/lib389/man/dscreate.8

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

#make %{?_smp_mflags}
make

%install

mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_sbindir}
%if %{use_cockpit}
mkdir -p %{buildroot}%{_datadir}/cockpit
%endif
make DESTDIR="$RPM_BUILD_ROOT" install

%if %{use_cockpit}
find %{buildroot}%{_datadir}/cockpit/389-console -type d | sed -e "s@%{buildroot}@@" | sed -e 's/^/\%dir /' > cockpit.list
find %{buildroot}%{_datadir}/cockpit/389-console -type f | sed -e "s@%{buildroot}@@" >> cockpit.list
%endif

# Copy in our docs from doxygen.
cp -r %{_builddir}/%{name}-%{version}/man/man3 $RPM_BUILD_ROOT/%{_mandir}/man3

# lib389
pushd src/lib389
%py3_install
popd

mkdir -p $RPM_BUILD_ROOT/var/log/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lib/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lock/%{pkgname}

# for systemd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/%{groupname}.wants
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/389-ds-base.conf

# remove libtool archives and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsvrcore.la

%if %{bundle_jemalloc}
pushd ../%{jemalloc_name}-%{jemalloc_ver}
make DESTDIR="$RPM_BUILD_ROOT" install_lib install_bin
cp -pa COPYING ../%{name}-%{version}/COPYING.jemalloc
cp -pa README ../%{name}-%{version}/README.jemalloc
popd
%endif

%check
# This checks the code, if it fails it prints why, then re-raises the fail to shortcircuit the rpm build.
if ! make DESTDIR="$RPM_BUILD_ROOT" check; then cat ./test-suite.log && false; fi

%post
if [ -n "$DEBUGPOSTTRANS" ] ; then
    output=$DEBUGPOSTTRANS
    output2=${DEBUGPOSTTRANS}.upgrade
else
    output=/dev/null
    output2=/dev/null
fi
# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :

# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Soft_static_allocation
# Soft static allocation for UID and GID
# sysusers.d format https://fedoraproject.org/wiki/Changes/Adopting_sysusers.d_format
%sysusers_create_compat %{SOURCE4}

# Reload our sysctl before we restart (if we can)
sysctl --system &> $output; true

# Gather the running instances so we can restart them
instbase="%{_sysconfdir}/%{pkgname}"
ninst=0
for dir in $instbase/slapd-* ; do
    echo dir = $dir >> $output 2>&1 || :
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    basename=`basename $dir`
    inst="%{pkgname}@`echo $basename | sed -e 's/slapd-//g'`"
    echo found instance $inst - getting status  >> $output 2>&1 || :
    if /bin/systemctl -q is-active $inst ; then
       echo instance $inst is running >> $output 2>&1 || :
       instances="$instances $inst"
    else
       echo instance $inst is not running >> $output 2>&1 || :
    fi
    ninst=`expr $ninst + 1`
done
if [ $ninst -eq 0 ] ; then
    echo no instances to upgrade >> $output 2>&1 || :
    exit 0 # have no instances to upgrade - just skip the rest
else
    # restart running instances
    echo shutting down all instances . . . >> $output 2>&1 || :
    for inst in $instances ; do
        echo stopping instance $inst >> $output 2>&1 || :
        /bin/systemctl stop $inst >> $output 2>&1 || :
    done
    for inst in $instances ; do
        echo starting instance $inst >> $output 2>&1 || :
        /bin/systemctl start $inst >> $output 2>&1 || :
    done
fi


%preun
if [ $1 -eq 0 ]; then # Final removal
    # remove instance specific service files/links
    rm -rf %{_sysconfdir}/systemd/system/%{groupname}.wants/* > /dev/null 2>&1 || :
fi

%postun
if [ $1 = 0 ]; then # Final removal
    rm -rf /var/run/%{pkgname}
fi

%post snmp
%systemd_post %{pkgname}-snmp.service

%preun snmp
%systemd_preun %{pkgname}-snmp.service %{groupname}

%postun snmp
%systemd_postun_with_restart %{pkgname}-snmp.service

exit 0

%files
%if %{bundle_jemalloc}
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.jemalloc
%license COPYING.jemalloc
%else
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl
%endif
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/schema
%config(noreplace)%{_sysconfdir}/%{pkgname}/schema/*.ldif
%dir %{_sysconfdir}/%{pkgname}/config
%dir %{_sysconfdir}/systemd/system/%{groupname}.wants
%{_sysusersdir}/389-ds-base.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/slapd-collations.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/certmap.conf
%{_datadir}/%{pkgname}
%{_datadir}/gdb/auto-load/*
%{_unitdir}
%{_bindir}/dbscan
%{_mandir}/man1/dbscan.1.gz
%{_bindir}/ds-replcheck
%{_mandir}/man1/ds-replcheck.1.gz
%{_bindir}/ds-logpipe.py
%{_mandir}/man1/ds-logpipe.py.1.gz
%{_bindir}/ldclt
%{_mandir}/man1/ldclt.1.gz
%{_bindir}/logconv.pl
%{_mandir}/man1/logconv.pl.1.gz
%{_bindir}/pwdhash
%{_mandir}/man1/pwdhash.1.gz
#%caps(CAP_NET_BIND_SERVICE=pe) {_sbindir}/ns-slapd
%{_sbindir}/ns-slapd
%{_mandir}/man8/ns-slapd.8.gz
%{_sbindir}/openldap_to_ds
%{_mandir}/man8/openldap_to_ds.8.gz
%{_libexecdir}/%{pkgname}/ds_systemd_ask_password_acl
%{_libexecdir}/%{pkgname}/ds_selinux_restorecon.sh
%{_mandir}/man5/99user.ldif.5.gz
%{_mandir}/man5/certmap.conf.5.gz
%{_mandir}/man5/slapd-collations.conf.5.gz
%{_mandir}/man5/dirsrv.5.gz
%{_mandir}/man5/dirsrv.systemd.5.gz
%{_libdir}/%{pkgname}/python
%dir %{_libdir}/%{pkgname}/plugins
%{_libdir}/%{pkgname}/plugins/*.so
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_localstatedir}/lib/%{pkgname}
%dir %{_localstatedir}/log/%{pkgname}
%ghost %dir %{_localstatedir}/lock/%{pkgname}
%exclude %{_sbindir}/ldap-agent*
%exclude %{_mandir}/man1/ldap-agent.1.gz
%exclude %{_unitdir}/%{pkgname}-snmp.service
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/
%{_libdir}/%{pkgname}/bin/
%exclude %{_libdir}/%{pkgname}/bin/jemalloc-config
%exclude %{_libdir}/%{pkgname}/bin/jemalloc.sh
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.a
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.so
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc_pic.a
%exclude %{_libdir}/%{pkgname}/lib/pkgconfig
%endif

%files devel
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%{_mandir}/man3/*
%{_includedir}/svrcore.h
%{_includedir}/%{pkgname}
%{_libdir}/libsvrcore.so
%{_libdir}/%{pkgname}/libslapd.so
%{_libdir}/%{pkgname}/libns-dshttpd.so
%{_libdir}/%{pkgname}/libldaputil.so
%{_libdir}/pkgconfig/svrcore.pc
%{_libdir}/pkgconfig/dirsrv.pc

%files libs
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%dir %{_libdir}/%{pkgname}
%{_libdir}/libsvrcore.so.*
%{_libdir}/%{pkgname}/libslapd.so.*
%{_libdir}/%{pkgname}/libns-dshttpd.so.*
%{_libdir}/%{pkgname}/libldaputil.so.*
%{_libdir}/%{pkgname}/librewriters.so*
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/libjemalloc.so.2
%endif

%files snmp
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1.gz
%{_unitdir}/%{pkgname}-snmp.service

%files -n python%{python3_pkgversion}-lib389
%doc LICENSE LICENSE.GPLv3+
%{python3_sitelib}/lib389*
%{_sbindir}/dsconf
%{_mandir}/man8/dsconf.8.gz
%{_sbindir}/dscreate
%{_mandir}/man8/dscreate.8.gz
%{_sbindir}/dsctl
%{_mandir}/man8/dsctl.8.gz
%{_sbindir}/dsidm
%{_mandir}/man8/dsidm.8.gz
%{_libexecdir}/%{pkgname}/dscontainer

%if %{use_cockpit}
%files -n cockpit-389-ds -f cockpit.list
%{_datarootdir}/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%doc README.md
%endif

%changelog
* Mon Mar 18 2024 Simon Pichugin <spichugi@redhat.com> - 2.4.5-5
- Bump version to 2.4.5-5
- Rebuild for exception phase

* Thu Mar 14 2024 Simon Pichugin <spichugi@redhat.com> - 2.4.5-4
- Bump version to 2.4.5-4
- Resolves: RHEL-5130  - RFE Add PROXY protocol support to 389-ds-base via confiuration item - similar to Postfix

* Fri Jan 19 2024 Viktor Ashirov <vashirov@redhat.com> - 2.4.5-3
- Bump version to 2.4.5-3
- Fix License tag

* Mon Jan 15 2024 James Chapman <jachapma@redhat.com> - 2.4.5-2
- Bump version to 2.4.5-2
- Resolves: RHEL-15907 - Rebase 389-ds-base in RHEL 9.4
- Resolves: RHEL-5142  - RFE Disable Transparent Huge Pages when using large caches
- Resolves: RHEL-5130  - RFE Add PROXY protocol support to 389-ds-base via confiuration item - similar to Postfix
- Resolves: RHEL-5133  - RFE Provide a history for 'LastLoginTime'
- Resolves: RHEL-16984 - RFE inChain Matching Rule

* Fri Jan 12 2024 James Chapman <jachapma@redhat.com> - 2.4.5-1
- Bump version to 2.4.5-1
- Resolves: RHEL-15907 - Rebase 389-ds-base in RHEL 9.4
- Resolves: RHEL-5142  - RFE Disable Transparent Huge Pages when using large caches
- Resolves: RHEL-5130  - RFE Add PROXY protocol support to 389-ds-base via confiuration item - similar to Postfix
- Resolves: RHEL-5133  - RFE Provide a history for 'LastLoginTime'
- Resolves: RHEL-16984 - RFE inChain Matching Rule

* Tue Nov 21 2023 James Chapman <jachapma@redhat.com> - 2.4.4-1
- Bump version to 2.4.4-1
- Resolves: RHEL-15907 - Rebase 389-ds-base-2.4 in RHEL 9.4
- Resolves: RHEL-16830 - ns-slapd crash in slapi_attr_basetype

* Thu Sep 7 2023 Simon Pichugin <spichugi@redhat.com> - 2.3.6-3
- Bump version to 2.3.6-3
- Resolves: rhbz#2236163 - Regression: replication can't be enabled for consumer or hub role

* Tue Aug 8 2023 Mark Reynolds <mreynolds@redhat.com> - 2.3.6-2
- Bump version to 2.3.6-2
- Resolves: rhbz#2225532 - 389-ds-base FTBFS with rust-1.71.0
- Resolves: rhbz#2218209 - useradd: invalid user ID '389:389': installing 389-ds-base in container fails to create the dirsrv user
- Resolves: rhbz#2207691 - python3-lib389: Python tarfile extraction needs change to avoid a warning
- Resolves: rhbz#2179278 - dirsrv failed to start after reboot because "dirsrv" did not have access on /run/dirsrv

* Mon Jul 24 2023 Mark Reynolds <mreynolds@redhat.com> - 2.3.4-3
- Bump version to 2.3.4-3
- Resolves: rhbz#2189954 - RFE Improve reponse time to filters containing 'nsrole'
- Resolves: rhbz#2189946 - RFE support of slapi_memberof for plugins/core server
- Resolves: rhbz#1974242 - Paged search impacts performance

* Fri May 19 2023 Mark Reynolds <mreynolds@redhat.com> - 2.3.4-2
- Bump version to 2.3.4-2
- Resolves: rhbz#2188627 - Fix license

* Thu May 18 2023 Mark Reynolds <mreynolds@redhat.com> - 2.3.4-1
- Bump version to 2.3.4-1
- Resolves: rhbz#2188627 - Rebase 389-ds-base-2.3 in RHEL 9.3

* Wed Mar 08 2023 Simon Pichugin <spichugi@redhat.com> - 2.2.4-4
- Resolves: rhbz#2095366 - [RFE] 389-ds-base systemd-sysusers

* Tue Dec 13 2022 Mark Reynolds <mreynolds@redhat.com> - 2.2.4-3
- Bump version to 2.2.4-3
- Resolves: rhbz#2142636 - pam mutex lock causing high etimes, affecting red hat internal sso
- Resolves: rhbz#2093981 - RFE - Create Security Audit Log
- Resolves: rhbz#2132697 - [RFE] 389ds: run as non-root
- Resolves: rhbz#2124660 - Retro changelog trimming uses maxage incorrectly
- Resolves: rhbz#2114039 - Current pbkdf2 hardcoded parameters are no longer secure
- Resolves: rhbz#2112998 - performance search rate: checking if an entry is a referral is expensive
- Resolves: rhbz#2112361 - Supplier should do periodic update to avoid slow replication when a new direct update happen
- Resolves: rhbz#2109891 - Migrate 389 to pcre2


* Mon Dec 12 2022 Mark Reynolds <mreynolds@redhat.com> - 2.2.4-2
- Bump version to 2.2.4-2
- Resolves: Bug 1859271 - RFE - Extend log of operations statistics in access log
- Resolves: Bug 2093981 - RFE - Create Security Audit Log
- Resolves: Bug 2109891 - Migrate 389 to pcre2
- Resolves: Bug 2112361 - Supplier should do periodic update to avoid slow replication when a new direct update happen
- Resolves: Bug 2112998 - performance search rate: checking if an entry is a referral is expensive
- Resolves: Bug 2114039 - Current pbkdf2 hardcoded parameters are no longer secure
- Resolves: Bug 2124660 - Retro changelog trimming uses maxage incorrectly
- Resolves: Bug 2132697 - RFE - run as non-root
- Resolves: Bug 2142636 - pam mutex lock causing high etimes, affecting red hat internal sso

* Fri Nov 11 2022 Mark Reynolds <mreynolds@redhat.com> - 2.2.4-1
- Bump version to 2.2.4-1
- Resolves:  Bug 1132524 - [RFE] Compression of log files

