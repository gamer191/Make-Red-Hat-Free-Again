Name:       setxkbmap
Version:    1.3.2
Release:    5%{?dist}
Summary:    X11 keymap client

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/setxkbmap-%{version}.tar.bz2

BuildRequires:  make gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-xkb-utils < 7.8

%description
setxkbmap is an X11 client to change the keymaps in the X server for a
specified keyboard to use the layout determined by the options listed
on the command line.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.2-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.2-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.3.2-2
- Split setxkbmap out from xorg-x11-xkb-utils into its own package
  (#1895795)
