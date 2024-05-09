Name:		ntpstat
Version:	0.6
Release:	6%{?dist}
Summary:	Utility to print NTP synchronization status

License:	MIT
URL:		https://github.com/mlichvar/ntpstat
Source0:	https://github.com/mlichvar/ntpstat/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	make
Requires:	(ntpsec or chrony)
# ntpstat was split off from the ntp package
Conflicts:	ntp < 4.2.8p10-4

%description
This package contains a script which prints a brief summary of the system
clock's synchronisation status when the ntpd or chronyd daemon is running.

%prep
%setup -q

%build

%install
make install bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.6-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.6-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 08 2021 Miroslav Lichvar <mlichvar@redhat.com> 0.6-4
- switch dependency from ntp to ntpsec

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Miroslav Lichvar <mlichvar@redhat.com> 0.6-1
- update to 0.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.5-1
- update to 0.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-3
- fix more issues found in package review (#1510565)

* Thu Nov 23 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-2
- fix issues found in package review (#1510565)

* Tue Nov 07 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.4-1
- update to 0.4
- split ntpstat off from ntp package
