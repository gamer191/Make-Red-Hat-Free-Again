Name:          libzdnn
Version:       1.0.1
Release:       1%{?dist}
Summary:       Driver library for the IBM Z Neural Network Processing Assist Facility

License:       ASL 2.0
Url:           https://github.com/IBM/zDNN
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch: s390x
BuildRequires: gcc
BuildRequires: g++
BuildRequires: make
BuildRequires: gawk
BuildRequires: automake
BuildRequires: autoconf

# Be explicit about the soversion in order to avoid unintentional changes.
%global soversion 0

%description
The zDNN library provide a user space API for exploitation of the
Neural Network Processing Assist Facility.  All application which
intend to use that facility on IBM Z are supposed to do this via this
library.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package       static
Summary:       Static library version %{name}
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static library of %{name}.


%prep
%autosetup -p1 -n zDNN-%{version}
autoreconf -i

%build
# libzdnn needs to be built with z14 support so override the distro wide options to append -march=z14.
# cflags for the init routines in e.g. zdnn_init.c should just use the distro options.
# export CFLAGS_INIT explicitely since it is not handled by configure
CFLAGS_INIT="%{build_cflags}"; export CFLAGS_INIT; CFLAGS="%{build_cflags} -march=z14 -mtune=z14" CXXFLAGS="%{build_cxxflags} -march=z14 -mtune=z14" %configure
%make_build build

%install
%make_install
mv $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version}
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion}

rm -f $RPM_BUILD_ROOT%{_libdir}/libzdnn.so
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so


%files
%{_libdir}/libzdnn.so.%{version}
%{_libdir}/libzdnn.so.%{soversion}
%doc README.md
%license LICENSE

%files devel
%{_includedir}/zdnn.h
%{_libdir}/*.so

%files static
%{_libdir}/libzdnn.a

%changelog
* Thu May 11 2023 Jakub Čajka <jcajka@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Resolves: RHBZ#2160081

* Tue Jan 24 2023 Jakub Čajka <jcajka@redhat.com> - 0.4.0-2
- Release bump
- Resolves: RHBZ#2093292

* Fri Mar 25 2022 Jakub <jcajka@redhat.com> - 0.4.0-1
- Initial package import
- Resolves: RHBZ#2070957
