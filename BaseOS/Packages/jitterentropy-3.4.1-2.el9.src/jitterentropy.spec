Name:	jitterentropy
Version:	3.4.1
Release:	2%{?dist}
Summary:	Library implementing the jitter entropy source

License:	BSD or GPLv2
URL:		https://github.com/smuellerDD/jitterentropy-library
Source0:	%{url}/archive/v%{version}/%{name}-library-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# Disable Upstream Makefiles debuginfo strip on install
Patch0: jitterentropy-rh-makefile.patch

%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for jitterentropy

%prep
%autosetup -p0 -n %{name}-library-%{version}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/usr/include/
%make_install PREFIX=/usr LIBDIR=%{_lib}

%files
%doc README.md CHANGES.md
%license LICENSE LICENSE.bsd LICENSE.gplv2
%{_libdir}/libjitterentropy.so.3*

%files devel
%{_includedir}/*
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
* Tue Dec 27 2022 Vladis Dronov <vdronov@redhat.com> - 3.4.1-2
- Update to the upstream v3.4.1 @ 7bf9f85d (bz 2140043)
- Fix a stack corruption on s390x

* Tue Oct 04 2022 Vladis Dronov <vdronov@redhat.com> - 3.4.1-1
- Update to the upstream v3.4.1 @ 4544e113 (bz 2124596)

* Tue Apr 26 2022 Vladis Dronov <vdronov@redhat.com> - 3.4.0-1
- Update to the upstream v3.4.0 @ 2e5019cf (bz 2075978)

* Tue Nov 23 2021 Vladis Dronov <vdronov@redhat.com> - 3.3.1-2
- Update to the upstream v3.3.1 @ 887c9871 (bz 2015560)
- Fix a security issue found by a covscan in jitterentropy library

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.0.2-3.git.409828cf
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jul 13 2021 Vladis Dronov <vdronov@redhat.com> - 3.0.2-2.git.409828cf
- Update to the latest upstream commits upto 409828cf (bz 1973157)
- Add clock_gettime() software time source
- Add a code for choosing between software and hardware time sources
  https://github.com/smuellerDD/jitterentropy-library/pull/57
  https://bugzilla.redhat.com/show_bug.cgi?id=1974132

* Tue Jul 06 2021 Vladis Dronov <vdronov@redhat.com> - 3.0.2.git.d18d5863-1
- Update to the upstream v3.0.2 + tip of origin/master
  with fixes for an important issue:
  https://github.com/nhorman/rng-tools/pull/123
  https://github.com/smuellerDD/jitterentropy-library/issues/37
- Add important upstream fixes for the one CPU case (bz 1974132)

* Fri Jun 18 2021 Vladis Dronov <vdronov@redhat.com> - 3.0.2-1
- Update to the upstream v3.0.2 (bz 1973157)
- Remove ldconfig_scriptlets

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.2.0-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Neil Horman <nhorman@redhat.com> - 2.2.0-1
- Update to latest upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-3
- Drop static library
- Fix up naming
- Add gcc buildrequires
- Fix files glob

* Thu Sep 13 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-2
- Fixed license
- Fixed up some macro usage in spec file
- Documented patches
- Modified makefile to use $(INSTALL) macro

* Thu Sep 06 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-1
- Initial import
