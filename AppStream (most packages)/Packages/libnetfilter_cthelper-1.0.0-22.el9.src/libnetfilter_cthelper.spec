Name:           libnetfilter_cthelper
Version:        1.0.0
Release:        22%{?dist}
Summary:        User-space infrastructure for connection tracking helpers
License:        GPLv2
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  libmnl-devel >= 1.0.0, pkgconfig, kernel-headers
BuildRequires: make

Patch1: 0001-src-fix-use-after-free.patch
Patch2: 0002-include-Sync-with-kernel-headers.patch
Patch3: 0003-examples-fix-double-free-in-nftc-helper-add.patch
Patch4: 0004-examples-kill-the-invalid-argument-error-in-nftc-hel.patch
Patch5: 0005-src-fix-incorrect-building-and-parsing-of-the-NFCTH_.patch

%description
This library provides the infrastructure for the user-space helper
infrastructure available since the Linux kernel 3.6.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.0
Requires:       kernel-headers

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%doc examples
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cthelper
%{_includedir}/libnetfilter_cthelper/*.h
%{_libdir}/*.so

%changelog
* Wed Dec 22 2021 Phil Sutter <psutter@redhat.com> - 1.0.0-22
- src: fix incorrect building and parsing of the NFCTH_POLICY_SETX attribute
- examples: kill the "invalid argument" error in nftc-helper-add
- examples: fix double free in nftc-helper-add
- include: Sync with kernel headers
- src: fix use after free

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.0-21
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.0-20
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Paul Komkoff <i@stingr.net> - 1.0.0-3
- fix group tag on devel package

* Tue Nov 27 2012 Paul Komkoff <i@stingr.net> - 1.0.0-2
- fixes for epel5

* Mon Nov 26 2012 Paul Komkoff <i@stingr.net> - 1.0.0-1
- new package
