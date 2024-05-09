Summary: X.Org X11 libXfont2 runtime library
Name: libXfont2
Version: 2.0.3
Release: 12%{?dist}
License: MIT
URL: http://www.x.org

Source0: http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(fontsproto)
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel

%description
X.Org X11 libXfont2 runtime library

%package devel
Summary: X.Org X11 libXfont2 development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}

%description devel
X.Org X11 libXfont development package

%prep
%autosetup

%build
autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static
make %{?_smp_mflags}  

%install
%make_install

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/libXfont2.so.2*

%files devel
%{_includedir}/X11/fonts/libxfont2.h
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.3-12
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.3-11
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 11:25:30 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 2.0.3-9
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 2.0.3-5
- Rebuild for xtrans 1.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 2.0.3-2
- Use ldconfig scriptlet macros

* Mon Feb 26 2018 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.0.3-1
- libXfont 2.0.3 (CVE-2017-16611)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Adam Jackson <ajax@redhat.com> - 2.0.2-1
- libXfont 2.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Hans de Goede <hdegoede@redhat.com> - 2.0.1-2
- Add some fixes from upstream git master

* Wed Jun 08 2016 Adam Jackson <ajax@redhat.com> - 2.0.2-1
- Initial packaging forked from libXfont

