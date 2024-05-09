Name:           libhandy
Version:        1.2.3
Release:        1%{?dist}
Summary:        Building blocks for modern adaptive GNOME apps
License:        LGPLv2+

URL:            https://gitlab.gnome.org/GNOME/libhandy
%global majmin %(echo %{version} | cut -d . -f -2)
Source0:        https://download.gnome.org/sources/libhandy/%{majmin}/libhandy-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1

# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb

# Retired in F34
Obsoletes:      libhandy1 < 1.1.90-2
Conflicts:      libhandy1 < 1.1.90-2
Provides:       libhandy1 = %{version}-%{release}
Provides:       libhandy1%{?_isa} = %{version}-%{release}

%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Retired in F34
Obsoletes:      libhandy1-devel < 1.1.90-2
Conflicts:      libhandy1-devel < 1.1.90-2
Provides:       libhandy1-devel = %{version}-%{release}
Provides:       libhandy1-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n libhandy-%{version} -p1


%build
%meson -Dgtk_doc=true -Dexamples=false -Dtests=true
%meson_build


%install
%meson_install

%find_lang libhandy


%check
%{shrink:xvfb-run -a %meson_test}


%files -f libhandy.lang
%license COPYING
%doc AUTHORS
%doc HACKING.md
%doc NEWS
%doc README.md

%{_libdir}/girepository-1.0/
%{_libdir}/libhandy-1.so.0

%files devel
%{_includedir}/libhandy-1/

%{_libdir}/glade/
%{_libdir}/libhandy-1.so
%{_libdir}/pkgconfig/libhandy-1.pc

%{_datadir}/gir-1.0/
%{_datadir}/glade/
%{_datadir}/gtk-doc/
%{_datadir}/vala/


%changelog
* Tue Aug 24 2021 Kalev Lember <klember@redhat.com> - 1.2.3-1
- Update to 1.2.3

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Mar 19 2021 Kalev Lember <klember@redhat.com> - 1.2.0-2
- Add conflicts with libhandy1 packages to help with the upgrade path

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 03 2021 Kalev Lember <klember@redhat.com> - 1.1.90-2
- Update to 1.1.90 and libhandy 1 ABI, based on earlier libhandy1 packaging
- Obsolete separate libhandy1 and libhandy1-devel packages

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 0.0.13-6
- Disable glade catalog for F33+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 0.0.13-3
- Rebuilt for libgladeui soname bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 0.0.13-1
- Update to 0.0.13

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 0.0.11-1
- Update to 0.0.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 0.0.10-2
- Add patch to fix installation of glade resources for flatpak builds

* Thu Jun 13 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.10-1
- Update to 0.0.10

* Thu Mar 07 2019 Kalev Lember <klember@redhat.com> - 0.0.9-1
- Update to 0.0.9

* Fri Mar 1 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.8-2
- Pull an upstream fix to prevent broken translations in
  libhandy using apps

* Sat Feb 16 2019 Kalev Lember <klember@redhat.com> - 0.0.8-1
- Update to 0.0.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Kalev Lember <klember@redhat.com> - 0.0.7-1
- Update to 0.0.7

* Fri Jan 11 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.6-2
- Swap some runtime vs devel bits

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 0.0.6-1
- Initial Fedora packaging
