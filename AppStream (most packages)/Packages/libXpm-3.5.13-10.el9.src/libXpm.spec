Summary: X.Org X11 libXpm runtime library
Name: libXpm
Version: 3.5.13
Release: 10%{?dist}
License: MIT
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: gettext
BuildRequires: pkgconfig(xext) pkgconfig(xt) pkgconfig(xau)
BuildRequires: ncompress gzip

# CVE-2022-46285
Patch0001: 0001-Fix-CVE-2022-46285-Infinite-loop-on-unclosed-comment.patch
# CVE-2022-44617
Patch0002: 0002-Fix-CVE-2022-44617-Runaway-loop-with-width-of-0-and-.patch
Patch0003: 0003-Prevent-a-double-free-in-the-error-code-path.patch
# CVE-2022-4883
Patch0004: 0004-configure-add-disable-open-zfile-instead-of-requirin.patch
Patch0005: 0005-Fix-CVE-2022-4883-compression-commands-depend-on-PAT.patch
Patch0006: 0006-Use-gzip-d-instead-of-gunzip.patch
# CVE-2023-43788
Patch0007: 0001-Fix-CVE-2023-43788-Out-of-bounds-read-in-XpmCreateXp.patch
# CVE-2023-43789
Patch0008: 0001-Fix-CVE-2023-43789-Out-of-bounds-read-on-XPM-with-co.patch

%description
X.Org X11 libXpm runtime library

%package devel
Summary: X.Org X11 libXpm development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXpm development package

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
#%dir %{_mandir}/man1x
%{_mandir}/man1/*.1*
#%{_mandir}/man1/*.1x*

%changelog
* Wed Oct 11 2023 José Expósito <jexposit@redhat.com> - 3.5.13-10
- Drop hardening patches from previous version to keep ABI compatibility

* Wed Oct 11 2023 José Expósito <jexposit@redhat.com> - 3.5.13-9
- CVE-2023-43786 libX11: stack exhaustion from infinite recursion
  in PutSubImage()
- CVE-2023-43787 libX11: integer overflow in XCreateImage() leading to
  a heap overflow
- CVE-2023-43788 libXpm: out of bounds read in XpmCreateXpmImageFromBuffer()
- CVE-2023-43789 libXpm: out of bounds read on XPM with corrupted colormap

* Mon Jan 16 2023 Peter Hutterer <peter.hutterer@redhat.com> - 3.5.13-8
- Fix CVE-2022-46285: infinite loop on unclosed comments (#2160230)
- Fix CVE-2022-44617: runaway loop with width of 0 (#2160232)
- Fix CVE-2022-4883: compression depends on $PATH (#2160242)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.5.13-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.5.13-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Peter Hutterer <peter.hutterer@redhat.com> 3.5.13-4
- Add make to BuildRequires

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Peter Hutterer <peter.hutterer@redhat.com> 3.5.13-1
- libXpm 3.5.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 3.5.12-7
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 3.5.12-6
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 3.5.12-1
- libXpm 3.5.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Adam Jackson <ajax@redhat.com> 3.5.11-1
- libXpm 3.5.11
- Drop pre-F18 changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 3.5.10-4
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Adam Jackson <ajax@redhat.com> 3.5.10-1
- libXpm 3.5.10
