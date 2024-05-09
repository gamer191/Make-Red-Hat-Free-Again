# RHEL 8 compatibility
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

Name:    nvme-stas
Summary: NVMe STorage Appliance Services
Version: 2.2.1
Release: 2%{?dist}
License: ASL 2.0
URL:     https://github.com/linux-nvme/nvme-stas
Source0: %{url}/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildArch:     noarch

BuildRequires: meson >= 0.57.0
BuildRequires: glib2-devel
BuildRequires: libnvme-devel >= 1.4
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: systemd-devel

BuildRequires: python3-devel
#BuildRequires: python3-pyflakes
#BuildRequires: python3-pylint
#BuildRequires: pylint

BuildRequires: python3-libnvme
BuildRequires: python3-dasbus
BuildRequires: python3-pyudev
BuildRequires: python3-systemd
BuildRequires: python3-gobject-devel
BuildRequires: python3-lxml

Requires:      avahi
Requires:      python3-libnvme >= 1.4
Requires:      python3-dasbus
Requires:      python3-pyudev
Requires:      python3-systemd
Requires:      python3-gobject
Requires:      python3-lxml

%description
nvme-stas is a Central Discovery Controller (CDC) client for Linux. It
handles Asynchronous Event Notifications (AEN), Automated NVMe subsystem
connection controls, Error handling and reporting, and Automatic (zeroconf)
and Manual configuration. nvme-stas is composed of two daemons:
stafd (STorage Appliance Finder) and stacd (STorage Appliance Connector).

%prep
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build
%meson -Dman=true -Dhtml=true
%meson_build

%install
%meson_install
mv %{buildroot}/%{_sysconfdir}/stas/sys.conf.doc %{buildroot}/%{_sysconfdir}/stas/sys.conf

%post
%systemd_post stacd.service
%systemd_post stafd.service

%preun
%systemd_preun stacd.service
%systemd_preun stafd.service

%postun
%systemd_postun_with_restart stacd.service
%systemd_postun_with_restart stafd.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/stas
%config(noreplace) %{_sysconfdir}/stas/stacd.conf
%config(noreplace) %{_sysconfdir}/stas/stafd.conf
%config(noreplace) %{_sysconfdir}/stas/sys.conf
%{_datadir}/dbus-1/system.d/org.nvmexpress.*.conf
%{_bindir}/stacctl
%{_bindir}/stafctl
%{_bindir}/stasadm
%{_sbindir}/stacd
%{_sbindir}/stafd
%{_unitdir}/stacd.service
%{_unitdir}/stafd.service
%{_unitdir}/stas-config.target
%{_unitdir}/stas-config@.service
%dir %{python3_sitelib}/staslib
%{python3_sitelib}/staslib/*
%doc %{_pkgdocdir}/html
%{_mandir}/man1/sta*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/nvme*.7*
%{_mandir}/man8/sta*.8*

%changelog
* Fri Apr 07 2023 Maurizio Lombardi <mlombard@redhat.com> - 2.2.1-2
- Rebuild the package for side-tag

* Thu Apr 06 2023 Maurizio Lombardi <mlombard@redhat.com> - 2.2.1-1
- Update to version v2.2.1

* Fri Jan 13 2023 John Meneghini <jmeneghi@redhat.com> - 2.1.1-1
  - Update to the v2.1.1 package

* Tue Nov 08 2022 Maurizio Lombardi <mlombard@redhat.com> - 2.0-1
- Update to the latest v2.0 package

* Thu Aug 04 2022 Maurizio Lombardi <mlombard@redhat.com> - 1.1.6-3
- Sync with the official 1.1.6 version

* Wed Jul 27 2022 Maurizio Lombardi <mlombard@redhat.com> - 1.1.6-2
- Rebuild for CentOS Stream

* Wed Jul 20 2022 Maurizio Lombardi <mlombard@redhat.com> - 1.1.6-1
- Update to version 1.1.6

* Mon Jun 27 2022 Maurizio Lombardi <mlombard@redhat.com> - 1.1.4-1
- Update to version 1.1.4

* Wed Apr 20 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0-1
- Upstream v1.0 official release

* Tue Apr 05 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc7-1
- Upstream v1.0 Release Candidate 7

* Fri Mar 25 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc5-1
- Upstream v1.0 Release Candidate 5

* Mon Mar 07 2022 Tomas Bzatek <tbzatek@redhat.com> - 1.0~rc3-1
- Upstream v1.0 Release Candidate 3
