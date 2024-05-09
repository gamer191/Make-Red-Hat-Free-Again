Name:       rig
Summary:    Monitor a system for events and trigger specific actions
Version:    1.1
Release:    6%{?dist}
Url:        https://github.com/TurboTurtle/rig
Source0:    %{url}/archive/%{name}-%{version}.tar.gz
License:    GPLv2
BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(psutil)

Patch1: rig-fix-rig-list.patch
Patch2: rig-full-random-temp.patch

%description
Rig is a utility designed to watch or monitor specific system resources (e.g.
log files, journals, system activity, etc...) and then take specific action
when the trigger condition is met. Its primary aim is to assist in
troubleshooting and data collection for randomly occurring events.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%py3_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/rig.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%py3_install

%files
%{_bindir}/rig
%{_mandir}/man1/*

%{python3_sitelib}/rig-*.egg-info/
%{python3_sitelib}/rigging/

%license LICENSE
%doc README.md

%changelog
* Tue Jun 14 2022 Jake Hunsaker <jhunsake@redhat.com> - 1.1-6
- Backport change to temp dir creation to ignore rig ID

* Thu Jun 02 2022 Jake Hunsaker <jhunsake@redhat.com> - 1.1-4
- Backport fix for rig list race condition

* Fri May 04 2022 Jake Hunsaker <jhunsake@redhat.com> - 1.1-2
- Rebase to version 1.1
  Related: RHBZ#2077096

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jake Hunsaker <jhunsake@redhat.com> - 1.0-1
- Version 1.0 release
