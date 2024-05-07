# Required for xdp_impl_background_emit_running_applications_changed
%global xdg_desktop_portal_version 1.5.4

Name:           xdg-desktop-portal-gtk
Version:        1.12.0
Release:        3%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using GTK+

License:        LGPLv2+
URL:            https://github.com/flatpak/%{name}
Source0:        https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
BuildRequires:  systemd-rpm-macros
Requires:       dbus
Requires:       gsettings-desktop-schemas
Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}

# This portal is recommended if you have installed any app that uses GTK. (It's
# also recommended if you have any such app installed via flatpak or snap, but
# that is impossible to detect here.)
Supplements:    gtk3
Supplements:    gtk4

%description
A backend implementation for xdg-desktop-portal that is using GTK+.


%prep
%autosetup -p1


%build
# All backends that are disabled are instead provided by
# xdg-desktop-portal-gnome, to keep this package free of GNOME dependencies.
# The appchooser and settings backends are enabled for non-GNOME GTK
# applications.
%configure \
    --disable-silent-rules \
    --enable-appchooser \
    --enable-settings \
    --disable-background \
    --disable-lockdown \
    --disable-screencast \
    --disable-screenshot \
    --disable-wallpaper
%make_build


%install
%make_install
%find_lang %{name}


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%{_datadir}/xdg-desktop-portal/portals/gtk.portal
%{_userunitdir}/%{name}.service



%changelog
* Thu May 05 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.12.0-2
- Play well with the GNOME portals
Resolves: #2051495

* Tue Feb 08 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.12.0-1
- Recommend this portal backend for all GTK3 and GTK4 users
Resolves: #2078624

* Tue Feb 08 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.12.0-1
- Rebase to 1.12.0
Resolves: #2051493

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.8.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.8.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Kalev Lember <klember@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Sat Mar 14 2020 David King <amigadave@amigadave.com> - 1.7.0-1
- Update to 1.7.0 (#1813533)

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 1.6.0-4
- Backport support for mutter screencast API version 3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 1.6.0-2
- Rebuilt for libgnome-desktop soname bump

* Fri Dec 20 2019 David King <amigadave@amigadave.com> - 1.6.0-1
- Update to 1.6.0 (#1785644)

* Thu Dec 12 2019 David King <amigadave@amigadave.com> - 1.5.2-1
- Update to 1.5.2

* Thu Nov 28 2019 David King <amigadave@amigadave.com> - 1.5.1-1
- Update to 1.5.1 (#1714705)

* Fri Oct 04 2019 David King <amigadave@amigadave.com> - 1.5.0-1
- Update to 1.5.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Jonas Ådahl <jadahl@redhat.com> - 1.2.0-3
- Backport GNOME 3.32 API compatibility bump patch (#1686053)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 David King <amigadave@amigadave.com> - 1.2.0-1
- Update to 1.2.0

* Wed Jan 16 2019 Kalev Lember <klember@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Sep 03 2018 David King <amigadave@amigadave.com> - 1.0.2-1
- Update to 1.0.2

* Mon Aug 20 2018 David King <amigadave@amigadave.com> - 1.0-1
- Update to 1.0

* Tue Jul 24 2018 David King <amigadave@amigadave.com> - 0.99-1
- Update to 0.99

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Neal Gompa <ngompa13@gmail.com> - 0.11-2
- Update Supplements to also install when snapd is installed

* Wed Apr 25 2018 David King <amigadave@amigadave.com> - 0.11-1
- Update to 0.11 (#1545226)

* Wed Feb 14 2018 David King <amigadave@amigadave.com> - 0.10-1
- Update to 0.10 (#1545226)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 David King <amigadave@amigadave.com> - 0.9-1
- Update to 0.9 (#1514775)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 David King <amigadave@amigadave.com> - 0.7-1
- Update to 0.7

* Fri Mar 31 2017 David King <amigadave@amigadave.com> - 0.6-1
- Update to 0.6

* Fri Feb 17 2017 Kalev Lember <klember@redhat.com> - 0.5-3
- Use rich deps to pull in this package when flatpak and gtk3 are both installed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 David King <amigadave@amigadave.com> - 0.5-1
- Update to 0.5

* Fri Sep 02 2016 David King <amigadave@amigadave.com> - 0.3-1
- Update to 0.3

* Fri Jul 29 2016 David King <amigadave@amigadave.com> - 0.2-1
- Update to 0.2 (#1361576)

* Wed Jul 13 2016 David King <amigadave@amigadave.com> - 0.1-1
- Initial Fedora packaging
