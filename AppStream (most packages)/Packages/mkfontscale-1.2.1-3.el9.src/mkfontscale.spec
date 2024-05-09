Name:       mkfontscale
Version:    1.2.1
Release:    3%{?dist}
Summary:    Tool to generate legacy X11 font system index files

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

Patch0:     mkfontscale-examine-all-encodings.patch

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  zlib-devel

Conflicts:  xorg-x11-font-utils <= 7.5-50

# Used to be a separate upstream repo in xorg-x11-font-utils, now it's part
# of mkfontscale. Keep the Provides alive though.
Provides:   mkfontdir = %{version}

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.1-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-1
- Split mkfontscale/mkfontdir out from xorg-x11-font-utils into its own
  package (#1932734)
