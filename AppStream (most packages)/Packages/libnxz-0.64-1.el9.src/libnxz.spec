# Keep the *.la file around
# See https://fedoraproject.org/wiki/Changes/RemoveLaFiles
%global __brp_remove_la_files %nil

Name:		libnxz
Version:	0.64
Release:	1%{?dist}
Summary:	Zlib implementation for POWER processors
License:	ASL 2.0 or GPLv2+
Url:		https://github.com/libnxz/power-gzip
BuildRequires:	zlib-devel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libnxz.so.0

ExclusiveArch:	ppc64le
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	systemd-rpm-macros

%description
libnxz is a zlib-compatible library that uses the NX GZIP Engine available on
POWER9 or newer processors in order to provide a faster zlib/gzip compression
without using the general-purpose cores.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for developing application that
use %{name}.

%package	static
Summary:	Static library for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for developing
application that use %{name}.

%prep
%autosetup -p1 -n power-gzip-%{version}

%build
%configure --enable-zlib-api
%make_build

%check
# libnxz tests only work on P9 servers or newer, with Linux >= 5.8.
# This combination is not guaranteed to have at build time.  Check if
# NX GZIP engine device is available before deciding to run the tests.
if [[ -w "/dev/crypto/nx-gzip" ]]; then
	make check
fi

%install
%make_install

%pre
%{_sbindir}/groupadd -r -f nx-gzip

%files
%{_libdir}/%{soname}
%{_libdir}/libnxz.so.0.%{version}
%license %{_docdir}/%{name}/APACHE-2.0.txt
%license %{_docdir}/%{name}/gpl-2.0.txt
%doc README.md

%files devel
%{_includedir}/libnxz.h
%{_libdir}/libnxz.so

%files static
%{_libdir}/libnxz.a
%{_libdir}/libnxz.la

%changelog
* Thu Apr 06 2023 Jakub Čajka <jcajka@redhat.com> - 0.64-1
- update to 0.64
- Resolves: RHBZ#2177335

* Mon Aug 29 2022 Jakub Čajka <jcajka@redhat.com> - 0.63-2
- bump for gating
- Related: RHBZ#2101334

* Fri Jul 29 2022 Jakub Čajka <jcajka@redhat.com> - 0.63-1
- initial package import
- Resolves: RHBZ#2101334
