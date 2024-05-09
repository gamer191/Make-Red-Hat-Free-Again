%global buildflags -buildmode pie -compiler gc -a -v -x
%global goldflags %{expand:-linkmode=external -compressdwarf=false -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'}

%global yggdrasil_ver   0.2.4
%global ygg_pkg_mgr_ver 0.1.3

Name:    rhc
Version: 0.2.4
Release: 5%{?dist}
Epoch:   1
Summary: rhc connects the system to Red Hat hosted services
License: GPLv3
URL:     https://github.com/redhatinsights/rhc

Source0: https://github.com/RedHatInsights/rhc/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: config.toml
Source2: https://github.com/RedHatInsights/yggdrasil/releases/download/%{yggdrasil_ver}/yggdrasil-%{yggdrasil_ver}.tar.gz
Source3: https://github.com/RedHatInsights/yggdrasil-worker-package-manager/releases/download/%{ygg_pkg_mgr_ver}/yggdrasil-worker-package-manager-%{ygg_pkg_mgr_ver}.tar.xz
Source4: rhc-package-manager.toml

ExclusiveArch: %{go_arches}

Recommends:    insights-client

Requires:      subscription-manager
Requires(post):      policycoreutils-python-utils

BuildRequires: git
BuildRequires: golang
BuildRequires: go-rpm-macros
BuildRequires: dbus-devel
BuildRequires: systemd-devel


%define _description %{expand:%{name} is a client tool and daemon that connects the system to Red Hat hosted
services enabling system and subscription management.}

%description
%{_description}


%package devel
Summary: Development files for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}


%description devel
%{_description}

This package includes files necessary for building rhc workers.


%global makeflags %{expand:PREFIX=%{_prefix} \\
     SYSCONFDIR=%{_sysconfdir} \\
     LOCALSTATEDIR=%{_localstatedir} \\
     SHORTNAME=%{name} \\
     LONGNAME=%{name} \\
     PKGNAME=%{name} \\
     'BRANDNAME=Remote Host Configuration' \\
     TOPICPREFIX=redhat/insights \\
     VERSION=%{version} \\
     DATAHOST=cert.cloud.redhat.com \\
     'PROVIDER=Red Hat'}


%prep
%setup -T -D -c -n %{name} -a 0
%setup -T -D -c -n %{name} -a 2
%setup -T -D -c -n %{name} -a 3
sed -i -e "s/LDFLAGS :=/LDFLAGS ?=/" %{_builddir}/%{name}/yggdrasil-%{yggdrasil_ver}/Makefile
sed -i -e "s/LDFLAGS :=/LDFLAGS ?=/" %{_builddir}/%{name}/%{name}-%{version}/Makefile


%build
%set_build_flags
export BUILDFLAGS="%{buildflags}"
export LDFLAGS="%{goldflags}"
cd %{_builddir}/%{name}/yggdrasil-%{yggdrasil_ver}
make %{makeflags}

cd %{_builddir}/%{name}/yggdrasil-worker-package-manager-%{ygg_pkg_mgr_ver}
go build %{buildflags} -ldflags="%{goldflags} -X 'github.com/redhatinsights/yggdrasil.SysconfDir=%{_sysconfdir}' -X 'github.com/redhatinsights/yggdrasil.LongName=%{name}'" -o rhc-package-manager-worker -mod vendor .

cd %{_builddir}/%{name}/%{name}-%{version}
make %{makeflags}


%install
%set_build_flags
export BUILDFLAGS="%{buildflags}"
export LDFLAGS="%{goldflags}"
cd %{_builddir}/%{name}/yggdrasil-%{yggdrasil_ver}
make %{makeflags} \
     DESTDIR=%{buildroot} \
     install

%{__install} -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/

cd %{_builddir}/%{name}/yggdrasil-worker-package-manager-%{ygg_pkg_mgr_ver}
%{__install} -D -m 755 rhc-package-manager-worker %{buildroot}%{_libexecdir}/%{name}/
%{__install} -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/workers/rhc-package-manager.toml

cd %{_builddir}/%{name}/%{name}-%{version}
make %{makeflags} \
     DESTDIR=%{buildroot} \
     install


%post
/usr/sbin/semanage permissive --add rhcd_t || true


%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/semanage permissive --delete rhcd_t || true
fi


%files
%doc %{name}-%{version}/README.md yggdrasil-%{yggdrasil_ver}/doc/tags.toml
%{_bindir}/%{name}
%{_sbindir}/%{name}d
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%config(noreplace) %{_sysconfdir}/%{name}/workers/rhc-package-manager.toml
%{_unitdir}/%{name}d.service
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/*
%{_libexecdir}/%{name}


%files devel
%{_prefix}/share/pkgconfig/%{name}.pc


%changelog
* Mon Feb 12 2024 Link Dupont <link@redhat.com> - 0.2.4-5
- Update embedded yggdrasil-worker-package-manager to 0.1.3 (RHEL-17179)
- Update embedded yggdrasil to 0.2.4 (RHEL-17179)

* Mon Jan 8 2024 Jiri Hnidek <jhnidek@redhat.com> - 0.2.4-4
- Add dependency on subscription-manager (RHEL-18974)

* Mon Oct 23 2023 Link Dupont <link@redhat.com> - 0.2.4-3
- Update embedded yggdrasil-worker-package-manager (RHEL-14200)

* Wed Oct 18 2023 Link Dupont <link@redhat.com> - 0.2.4-2
- Update embedded yggdrasil to 0.2.3 (RHEL-14200)

* Tue Aug 01 2023 Alba Hita Catala <ahitacat@redhat.com> - 0.2.4-1
- Configure proxy for http connections (RHBZ#2227018)
- Failling to get system profile is not an error but a warning (RHBZ#2227012)
- Prevent message content being logged at any level (RHBZ#2227010)
- Added bash completion (RHBZ#2145198)

* Tue Jul 25 2023 Vit Mojzis <vmojzis@redhat.com> - 0.2.3-2
- Make rhcd_t permissive even when SELinux is disabled (RHBZ#2226701)

* Tue Jul 04 2023 Alba Hita Catala <ahitacat@redhat.com> - 0.2.3-1
- New upstream version (RHBZ#2219563)

* Tue Feb 14 2023 Alba Hita Catala <ahitacat@redhat.com> - 0.2.2-1
- New upstream version (RHBZ#2169772)
- RHC renaming (RHBZ#2167427)

* Wed Feb 01 2023 Link Dupont <link@redhat.com> - 1:0.2.1-14
- Correct syntax error in post scriptlet

* Fri Jan 27 2023 Link Dupont <link@redhat.com> - 0.2.1-13
- Build debuginfo packages

* Thu Jan 26 2023 Link Dupont <link@redhat.com> - 0.2.1-12
- Only run semanage conditionally when SELinux is enabled (RHBZ#2164602)

* Tue Nov 22 2022 Link Dupont <link@redhat.com> - 0.2.1-11
- Fix an issue scanning worker's stdout (RHBZ#2144926)

* Thu Nov 10 2022 Link Dupont <link@redhat.com> - 0.2.1-10
- Set SELinux policy to permissive for rhcd_t module (RHBZ#2141445)

* Fri Jun 03 2022 Link Dupont <link@redhat.com> - 0.2.1-9
- Correct config file installation name (RHBZ#2082689)

* Fri Jun 03 2022 Link Dupont <link@redhat.com> - 0.2.1-8
- Correct default config file name (RHBZ#2082689)

* Mon May 09 2022 Link Dupont <link@redhat.com> - 0.2.1-7
- Correct default config file path (RHBZ#2082689)

* Thu Mar 17 2022 Link Dupont <link@redhat.com> - 0.2.1-6
- Change dependency on insights-client to weak (RHBZ#2064944)

* Tue Mar 1 2022 Link Dupont <link@redhat.com> - 0.2.1-5
- Ensure worker is built with hardening compiler flags (RHBZ#2060539)

* Tue Feb 22 2022 Link Dupont <link@redhat.com> - 0.2.1-4
- Update summary and description (RHBZ#2057029)

* Tue Feb 15 2022 Link Dupont <link@redhat.com> - 0.2.1-3
- Include patch to collect and report errors during disconnect

* Fri Feb 11 2022 Link Dupont <link@redhat.com> - 0.2.1-2
- Include patch to default worker config location

* Fri Feb 11 2022 Link Dupont <link@redhat.com> - 0.2.1-1
- New upstream version

* Wed Dec 01 2021 Link Dupont <link@redhat.com> - 0.2.0-6
- Require full NEVR in devel subpackage

* Wed Dec 01 2021 Link Dupont <link@redhat.com> - 0.2.0-5
- Enable building with PIE and other build flags

* Fri Sep 24 2021 Link Dupont <link@redhat.com> - 0.2.0-4
- Fix an issue reporting workers on reconnect (Resolves: RHBZ#2007767)

* Wed Sep  1 2021 Link Dupont <link@redhat.com> - 0.2.0-3
- Split out development files into subpackage

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.2.0-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jun 28 2021 Link Dupont <link@redhat.com> - 0.2.0-1
- New upstream release

* Fri Jun 25 2021 Link Dupont <link@redhat.com> - 0.1.99-5
- Mark config file as such

* Fri Jun 25 2021 Link Dupont <link@redhat.com> - 0.1.99-4
- New upstream snapshot

* Fri Jun 11 2021 Link Dupont <link@redhat.com> - 0.1.99-3
- Build executables as PIE programs

* Thu Jun 10 2021 Link Dupont <link@redhat.com> - 0.1.99-2
- Include missing disttag

* Tue May 25 2021 Link Dupont <link@redhat.com> - 0.1.99-1
- New upstream development release

* Wed Apr 28 2021 Link Dupont <link@redhat.com> - 0.1.4-2
- Rebuild for fixed binutils on aarch64 (Resolves: RHBZ#1954449)

* Fri Apr  9 2021 Link Dupont <link@redhat.com> - 0.1.4-1
- New upstream release

* Fri Feb 19 2021 Link Dupont <link@redhat.com> - 0.1.2-2
- Update default broker URI
- Set Epoch to 1

* Thu Feb 18 2021 Link Dupont <link@redhat.com> - 0.1.2-1
- New upstream release

* Wed Feb 17 2021 Link Dupont <link@redhat.com> - 0.1.1-1
- New upstream release

* Fri Feb 12 2021 Link Dupont <link@redhat.com> - 0.1-1
- Initial release
