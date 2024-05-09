Name:           power-profiles-daemon
Version:        0.13
Release:        1%{?dist}
Summary:        Makes power profiles handling available over D-Bus

License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon
Source0:        https://gitlab.freedesktop.org/hadess/power-profiles-daemon/uploads/1f2ea40547b2af8d255875d7085211e5/power-profiles-daemon-0.13.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  systemd
BuildRequires:  umockdev
BuildRequires:  python3-dbusmock
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/power-profiles-daemon

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerun -- power-profiles-daemon < 0.1-2

# This is for upgrades from previous versions before power-profiles-daemon became part
# of the system daemons.
systemctl --no-reload preset power-profiles-daemon.service &>/dev/null || :

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_localstatedir}/lib/power-profiles-daemon

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Mon Sep 11 2023 Kate Hsuan <hpa@redhat.com> - 0.13-1
- Update date to 0.13
- Support for AMD P-State
- Resolves: rhbz#2226568

* Mon May 02 2022 Bastien Nocera <bnocera@redhat.com> - 0.11.1-1
+ power-profiles-daemon-0.11.1-1
- Update to 0.11.1
- Resolves: rhbz#2080280

* Tue Nov 02 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.1-1
+ power-profiles-daemon-0.10.1-1
- Update to 0.10.1
- Resolves: rhbz#2019372

* Wed Oct 06 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.0-1
+ power-profiles-daemon-0.10.0-1
- Update to 0.10.0
- Resolves: rhbz#2011233

* Thu Aug 19 2021 Bastien Nocera <bnocera@redhat.com> - 0.9.0-1
+ power-profiles-daemon-0.9.0-1
- Update to 0.9.0
- Resolves: rhbz#1994473

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.8.1-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.8.1-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Apr 14 2021 Bastien Nocera <bnocera@redhat.com> - 0.8.1-2
+ power-profiles-daemon-0.8.1-2
- Remove linter, as apparently unwanted in check section
- Resolves: rhbz#1947950

* Thu Apr 01 2021 Bastien Nocera <bnocera@redhat.com> - 0.8.1-1
+ power-profiles-daemon-0.8.1-1
- Update to 0.8.1

* Mon Mar 22 2021 Bastien Nocera <bnocera@redhat.com> - 0.8-1
+ power-profiles-daemon-0.8-1
- Update to 0.8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-2
+ power-profiles-daemon-0.1-2
- Reload presets when updating from an older version

* Fri Aug 07 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-1
- Initial package
