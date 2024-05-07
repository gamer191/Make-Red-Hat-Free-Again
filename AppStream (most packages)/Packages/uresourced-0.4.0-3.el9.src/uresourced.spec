Name:           uresourced
Version:        0.4.0
Release:        3%{?dist}
Summary:        Dynamically allocate resources to the active user

License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/benzea/uresourced
Source0:        https://gitlab.freedesktop.org/benzea/uresourced/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  git
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)

%description
This daemon dynamically assigns a resource allocation to the active
graphical user. If the user has an active graphical session managed
using systemd (e.g. GNOME), then the memory allocation will be used
to protect the sessions core processes (session.slice).

%prep
%autosetup -S git -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_post uresourced.service
%systemd_user_post uresourced.service

%preun
%systemd_preun uresourced.service
%systemd_user_preun uresourced.service

%postun
%systemd_postun uresourced.service
%systemd_user_postun uresourced.service

%files
%license COPYING
%doc README
%doc NEWS.md
%config(noreplace) %{_sysconfdir}/uresourced.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UResourced.conf
%{_libexecdir}/uresourced
%{_libexecdir}/cgroupify
%{_unitdir}/*
%{_userunitdir}/*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 30 2021 Benjamin Berg <bberg@redhat.com> - 0.4.0-1
- New upstream release including cgroupify
  Resolves: #1931938
  Resolves: #1931934

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Benjamin Berg <bberg@redhat.com> - 0.3.0-1
- New upstream release fixing various issues

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Benjamin Berg <bberg@redhat.com> - 0.2.0-1
- New upstream release enabling CPU/IO controllers for applications

* Wed Jul 08 2020 Benjamin Berg <bberg@redhat.com> - 0.1.0-1
- Initial package (rhbz#1854898)
