Name:           smc-tools
Version:        1.8.3
Release:        1%{?dist}
Summary:        Shared Memory Communication Tools

License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/smc-tools
Source0:        https://github.com/ibm-s390-linux/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  bash-completion

%ifarch s390 s390x
# for smc_chk
Requires:       python3
Requires:       man
%endif


%description
The Shared Memory Communication Tools (smc-tools) package enables usage of SMC
sockets in Linux.

%prep
%autosetup


%build
%ifarch ppc64le
# see arch/powerpc/include/uapi/asm/types.h
%global optflags %optflags -D__SANE_USERSPACE_TYPES__
%endif
%set_build_flags
%make_build


%install
%make_install V=1


%files
%license LICENSE
%doc README.md
%{_bindir}/smcd
%{_bindir}/smcr
%{_bindir}/smc_dbg
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcss
%{_libdir}/libsmc-preload.so*
%{_mandir}/man7/af_smc.7*
%{_mandir}/man8/smcd*.8*
%{_mandir}/man8/smcr*.8*
%{_mandir}/man8/smc_pnet.8*
%{_mandir}/man8/smc_run.8*
%{_mandir}/man8/smcss.8*
%ifarch s390 s390x
%{_bindir}/smc_chk
%{_bindir}/smc_rnics
%{_mandir}/man8/smc_chk.8*
%{_mandir}/man8/smc_rnics.8*
%endif
%{_datadir}/bash-completion/


%changelog
* Mon Oct 09 2023 Čestmír Kalina <ckalina@redhat.com> - 1.8.3-1
- Resolves: RHEL-11416 Upgrade smc-tools to latest version
- smc_stats: Fix man page name
- Bump version.

* Mon Dec 05 2022 Čestmír Kalina <ckalina@redhat.com> - 1.8.2-1
- Resolves: #2110413 Upgrade smc-tools to latest version

* Mon May 02 2022 Čestmír Kalina <ckalina@redhat.com> - 1.8.1-1
- Resolves: #2044219 Update smc-tools to latest version

* Fri Nov 26 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.1-1
- Resolves: #2017065 Update smc-tools to 1.6.1

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.6.0-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 07 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.0-1
- Resolves: #1869550 Upgrade smc-tools to latest version
- Related: #1869743
- Related: #1869747

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.5.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Mar 17 2021 Dan Horák <dan@danny.cz> - 1.5.0-1
- update to 1.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Dan Horák <dan@danny.cz> - 1.3.1-1
- update to 1.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dan Horák <dan@danny.cz> - 1.2.0-1
- update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Dan Horák <dan@danny.cz> - 1.1.0-1
- update to 1.1.0

* Mon Apr 16 2018 Dan Horák <dan@danny.cz> - 1.0.0-4
- fix LDFLAGS injection (#1567902)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Dan Horák <dan@danny.cz> - 1.0.0-2
- use make macro
- comment patches
- use distro LDFLAGS in build

* Mon Jan  8 2018 Dan Horák <dan@danny.cz> - 1.0.0-1
- initial Fedora version
