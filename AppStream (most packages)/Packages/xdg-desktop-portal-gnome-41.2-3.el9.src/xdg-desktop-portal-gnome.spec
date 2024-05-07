%global tarball_version %%(echo %{version} | tr '~' '.')

# Required for xdp_impl_background_emit_running_applications_changed
%global xdg_desktop_portal_version 1.5.4

Name:           xdg-desktop-portal-gnome
Version:        41.2
Release:        3%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using GNOME

License:        LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/%{name}
Source0:        https://download.gnome.org/sources/%{name}/41/%{name}-%{tarball_version}.tar.xz

Patch0:         windows-changed-signal.patch

## Screencast: stream restoration support
# Code cleanups/shuffling
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/18
Patch11:        0001-screencast-trivial-style-cleanups.patch
Patch12:        0002-screencast-cleanup-unnecessary-forward-declaration.patch
Patch13:        0003-screencast-more-code-shuffling-and-cleanups.patch
Patch14:        0004-screencastwidget-rework-selection-api.patch
# Stream restoration support
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/14
Patch15:        0005-displaystatetracker-add-match-string.patch
Patch16:        0006-implement-screencast-stream-restoration.patch
Patch17:        0007-screencast-pass-stream-ids.patch
# Followup fixes
Patch18:        0008-screencast-fix-variant-type-check.patch
Patch19:        0009-screencast-dont-restore-windows-with-too-different-titles.patch
Patch20:        0010-screencast-dont-wrap-restore-data-in-another-variant.patch
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/49
Patch21:        0011-fix-window-screencast-stream-restore.patch
# Closely related screencast fixes
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/40
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/41
Patch22:        0012-screencast-close-screencast-dialog-when-the-session-is-closed-from-client-side.patch
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/52
Patch23:        0013-session-emit-closed-signal-when-we-are-closing-our-own-account.patch
# https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/86
Patch24:        00014-screencasts-duplicate-monitor-and-window-stream-info.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
BuildRequires:  systemd-rpm-macros
Requires:       dbus
Requires:       dbus-common
Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}
Supplements:    gnome-shell

%description
A backend implementation for xdg-desktop-portal that is using various pieces of
GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build


%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
%{_datadir}/xdg-desktop-portal/portals/gnome.portal
%{_userunitdir}/%{name}.service



%changelog
* Tue Jan 09 2024 Jan Grulich <jgrulich@redhat.com> - 41.2-3
- Add screencast stream restoration support
  Resolves: RHEL-4526

* Tue Dec 13 2022 Jonas Ådahl <jadahl@redhat.com> - 41.2-2
- Keep screen share window list up to date
  Resolves: #2148362

* Wed Jun 01 2022 Debarshi Ray <rishi@fedoraproject.org> - 41.2-1
- Update to 41.2
Resolves: #2083018

* Tue Apr 12 2022 Debarshi Ray <rishi@fedoraproject.org> - 41.1-3
- Recommend this portal backend for all GNOME users
Resolves: #2051473

* Tue Apr 05 2022 Debarshi Ray <rishi@fedoraproject.org> - 41.1-2
- Make the Supplements specific to Fedora to retain consistency with
  xdg-desktop-portal-gtk
Resolves: #2051473

* Sat Mar 05 2022 Debarshi Ray <rishi@fedoraproject.org> - 41.1-1
- Initial version
Resolves: #2051473
