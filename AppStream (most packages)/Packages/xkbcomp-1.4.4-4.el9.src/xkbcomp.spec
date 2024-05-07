Name:       xkbcomp
Version:    1.4.4
Release:    4%{?dist}
Summary:    XKB keymap compiler

License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.bz2

BuildRequires: make gcc
BuildRequires: libxkbfile-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-xkb-utils < 7.8

%description
X.Org XKB keymap compiler

%package devel
Summary:    XKB keymap compiler development package
Requires:   pkgconfig
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org XKB keymap compiler development files

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.4-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.4-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.4.4-1
- Split xkbcomp out from xorg-x11-xkb-utils into its own package (#1895770)
