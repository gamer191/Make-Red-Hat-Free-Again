Name: redfish-finder 
Version: 0.4
Release: 9%{?dist}
Summary: Utility for parsing SMBIOS information and configuring canonical BMC access
BuildArch: noarch

License: GPLv2
URL: https://github.com/nhorman/redfish-finder
Source0: %url/archive/V%{version}/%{name}-%{version}.tar.gz

Patch0: redfish-finder-python3.patch
Patch1: hostconfig-dhcp-parse.patch

%{?systemd_requires}
BuildRequires: systemd

Requires: python3 NetworkManager dmidecode

%description
Scans Smbios information for type 42 management controller information, and uses
that to configure the appropriate network interface so that the BMC is
canonically accessible via the host name redfish-localhost

%prep
%autosetup


%build
#noop here

%install
install -D -p -m 0755 redfish-finder %{buildroot}/%{_bindir}/redfish-finder
install -D -p -m 0644 redfish-finder.1 %{buildroot}/%{_mandir}/man1/redfish-finder.1
install -D -p -m 0644 ./redfish-finder.service %{buildroot}/%{_unitdir}/redfish-finder.service

%post
%systemd_post redfish-finder.service

%preun
%systemd_preun redfish-finder.service

%postun
%systemd_postun_with_restart redfish-finder.service


%files
%doc README.md
%license COPYING
%{_bindir}/redfish-finder
%{_mandir}/man1/redfish-finder.1.*
%{_unitdir}/redfish-finder.service

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.4-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Apr 19 2021 Joel Savitz <jsavitz@redhat.com> - 0.4-8
- Fix missing bz number in spec file (bz1951095)

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.4-7
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Mar 26 2021 Joel Savitz <jsavitz@redhat.com> - 0.4-6
- Fix parsing HostConfig for DHCP (bz1944243)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Neil Horman <nhorman@redhat.com> - 0.4-2
-Fixup interpreter (bz 1770861)

* Thu Oct 17 2019 Neil Horman <nhorman@redhat.com> - 0.4-1
- Update to latest upstream (bz1730589)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Neil Horman <nhorman@redhat.com> - 0.3-1
- Update to latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Neil Horman <nhorman@redhat.com> - 0.2-1
- Update to new upstream release

* Thu Oct 04 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-3
- Fixed missing BuildRequires/Requires
- Fixed missing dist tag
- Fixed Source url

* Wed Oct 03 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-2
- Updated requires for python3
- Removed unneeded BuildRequires
- Globed the inclusion of man page
- Fixed license file tagging

* Mon Oct 01 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-1 
- Initial import

