Name:           libell
Version:        0.41
Release:        4%{?dist}
Summary:        Embedded Linux library
License:        LGPLv2+
URL:            https://01.org/ell
Source0:        https://www.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz

Patch0: acd-client-nodebug.patch
Patch1: 0001-examples-avoid-using-inet_ntoa.patch
Patch2: 0002-ell-avoid-using-inet_ntoa.patch

BuildRequires:  gcc
BuildRequires:  make

%description
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.


%package devel
Summary:        Embedded Linux library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Headers for developing against libell.


%prep
%autosetup -p1 -n ell-%{version}


%build
%configure
%make_build V=1


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/libell.so.*


%files devel
%{_includedir}/ell
%{_libdir}/libell.so
%{_libdir}/pkgconfig/ell.pc


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.41-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jun 24 2021 Davide Caratti <dcaratti@redhat.com> - 0.41-3
- bump NVR to trigger CI

* Thu Jun 24 2021 Davide Caratti <dcaratti@redhat.com> - 0.41-2
- add gating test that uses acd-client.c. Related: rhbz#1973511
- drop tests dependency on libell-devel. Related: rhbz#1973511

* Mon Jun 21 2021 Davide Caratti <dcaratti@redhat.com> - 0.41-1
- Avoid use of inet_ntoa(). Related: rhbz#1967524 
- Update to 0.41. Related: rhbz#1967524

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.39-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 30 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.39-1
- Update to 0.39

* Thu Feb 18 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.38-1
- Update to 0.38

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.36-1
- Update to 0.36

* Tue Dec  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.35-1
- Update to 0.35

* Sun Sep 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.33-1
- Update to 0.33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.32-1
- Update to 0.32

* Wed Mar 25 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.30-1
- Update to 0.30 release

* Sun Feb  9 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.28-1
- Update to 0.28 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.27-1
- Update to 0.27 release

* Wed Oct 30 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.26-1
- Update to 0.26 release

* Fri Oct 25 2019 Peter Robinson <pbrobinson@gmail.com> - 0.25-1
- Update to 0.25 release

* Fri Oct 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.24-1
- Update to 0.24 release

* Fri Sep 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.23-1
- Update to 0.23 release

* Thu Aug 29 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.22-1
- Update to 0.22 release

* Mon Aug 05 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.21-1
- Update to 0.21 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.20-1
- Update to 0.20 release

* Mon Apr 15 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.19-1
- Update to 0.19 release

* Thu Apr  4 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.18-1
- Update to 0.18 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17-1
- Update to 0.17 release

* Wed Dec 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-1
- Update to 0.16 release

* Fri Nov 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-1
- Update to 0.15 release

* Sat Nov 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.14-1
- Update to 0.14 release

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.11-1
- Update to 0.11 release

* Mon Sep 24 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.9-1
- Update to 0.9 release

* Sat Aug 11 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.8-1
- Update to 0.8 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.5-1
- Update to 0.5 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2-2
- Renamed to libell to fix a naming conflict
- Addressed review issues (Igor Gnatenko, #1505237):
- Added BR gcc
- Made build verbose
- Moved pkgconfig file to devel subpackage
- Fixed license tag
- Dropped Group tag
- Packaged changelog

* Sun Oct 22 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1
- Initial packaging
