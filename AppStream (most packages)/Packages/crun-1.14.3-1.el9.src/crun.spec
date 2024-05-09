Summary: OCI runtime written in C
Name: crun
Version: 1.14.3
Release: 1%{?dist}
Source0: https://github.com/containers/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
License: GPLv2+
URL: https://github.com/containers/crun
# https://fedoraproject.org/wiki/PackagingDrafts/Go#Go_Language_Architectures
ExclusiveArch: %{go_arches}
# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python3
BuildRequires: git
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: criu-devel
BuildRequires: python3-libmount
BuildRequires: libtool
BuildRequires: /usr/bin/go-md2man
BuildRequires: libgcrypt-devel
Provides: oci-runtime
Recommends: criu >= 3.17.1
Recommends: criu-libs

%description
crun is a runtime for running OCI containers

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Mon Feb 19 2024 Jindrich Novy <jnovy@redhat.com> - 1.14.3-1
- update to https://github.com/containers/crun/releases/tag/1.14.3
- Related: RHEL-2112

* Fri Feb 16 2024 Jindrich Novy <jnovy@redhat.com> - 1.14.2-1
- update to https://github.com/containers/crun/releases/tag/1.14.2
- Related: RHEL-2112

* Fri Feb 09 2024 Jindrich Novy <jnovy@redhat.com> - 1.14.1-1
- update to https://github.com/containers/crun/releases/tag/1.14.1
- Related: RHEL-2112

* Wed Jan 24 2024 Jindrich Novy <jnovy@redhat.com> - 1.14-1
- update to https://github.com/containers/crun/releases/tag/1.14
- Related: RHEL-2112

* Wed Jan 17 2024 Jindrich Novy <jnovy@redhat.com> - 1.13-1
- update to https://github.com/containers/crun/releases/tag/1.13
- Related: RHEL-2112

* Tue Jan 02 2024 Jindrich Novy <jnovy@redhat.com> - 1.12-1
- update to https://github.com/containers/crun/releases/tag/1.12
- Related: RHEL-2112

* Tue Nov 07 2023 Jindrich Novy <jnovy@redhat.com> - 1.11.2-1
- update to https://github.com/containers/crun/releases/tag/1.11.2
- Related: RHEL-2112

* Tue Oct 31 2023 Jindrich Novy <jnovy@redhat.com> - 1.11.1-1
- update to https://github.com/containers/crun/releases/tag/1.11.1
- Related: RHEL-2112

* Mon Oct 30 2023 Jindrich Novy <jnovy@redhat.com> - 1.11-1
- update to https://github.com/containers/crun/releases/tag/1.11
- Related: RHEL-2112

* Fri Oct 20 2023 Jindrich Novy <jnovy@redhat.com> - 1.10-1
- update to https://github.com/containers/crun/releases/tag/1.10
- Related: RHEL-2112

* Fri Sep 29 2023 Jindrich Novy <jnovy@redhat.com> - 1.9.2-1
- update to https://github.com/containers/crun/releases/tag/1.9.2
- Related: Jira:RHEL-2112

* Tue Sep 26 2023 Jindrich Novy <jnovy@redhat.com> - 1.9.1-1
- update to https://github.com/containers/crun/releases/tag/1.9.1
- Related: Jira:RHEL-2112

* Fri Sep 15 2023 Jindrich Novy <jnovy@redhat.com> - 1.9-1
- update to https://github.com/containers/crun/releases/tag/1.9
- Related: Jira:RHEL-2112

* Tue Aug 22 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.7-1
- update to https://github.com/containers/crun/releases/tag/1.8.7
- Related: #2176063

* Thu Jul 27 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.6-1
- update to https://github.com/containers/crun/releases/tag/1.8.6
- Related: #2176063

* Mon May 22 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.5-1
- update to https://github.com/containers/crun/releases/tag/1.8.5
- Related: #2176063

* Fri Apr 14 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.4-1
- update to https://github.com/containers/crun/releases/tag/1.8.4
- Related: #2184220

* Tue Apr 04 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.3-2
- fix could not find symbol criu_set_lsm_mount_context in libcriu.so
- Resolves: #2184220

* Sun Mar 26 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.3-1
- update to https://github.com/containers/crun/releases/tag/1.8.3
- Related: #2176063

* Wed Mar 22 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.2-1
- update to https://github.com/containers/crun/releases/tag/1.8.2
- Related: #2176063

* Tue Feb 28 2023 Jindrich Novy <jnovy@redhat.com> - 1.8.1-1
- update to https://github.com/containers/crun/releases/tag/1.8.1
- Related: #2124478

* Wed Feb 01 2023 Jindrich Novy <jnovy@redhat.com> - 1.8-1
- update to https://github.com/containers/crun/releases/tag/1.8
- Related: #2124478

* Thu Jan 05 2023 Jindrich Novy <jnovy@redhat.com> - 1.7.2-2
- require libgcrypt-devel and add criu weak dep
- Resolves: #2158083

* Wed Nov 30 2022 Jindrich Novy <jnovy@redhat.com> - 1.7.2-1
- update to https://github.com/containers/crun/releases/tag/1.7.2
- Related: #2124478

* Mon Nov 28 2022 Jindrich Novy <jnovy@redhat.com> - 1.7.1-1
- update to https://github.com/containers/crun/releases/tag/1.7.1
- Related: #2124478

* Tue Nov 08 2022 Jindrich Novy <jnovy@redhat.com> - 1.7-1
- update to https://github.com/containers/crun/releases/tag/1.7
- Related: #2124478

* Tue Oct 18 2022 Jindrich Novy <jnovy@redhat.com> - 1.6-1
- update to https://github.com/containers/crun/releases/tag/1.6
- Related: #2124478

* Tue Aug 02 2022 Jindrich Novy <jnovy@redhat.com> - 1.5-1
- update to https://github.com/containers/crun/releases/tag/1.5
- Related: #2061316

* Wed May 11 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.5-2
- BuildRequires: /usr/bin/go-md2man
- Related: #2061316

* Wed Apr 27 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.5-1
- update to https://github.com/containers/crun/releases/tag/1.4.5
- Related: #2061316

* Thu Mar 24 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.4-1
- update to https://github.com/containers/crun/releases/tag/1.4.4
- Related: #2061316

* Tue Mar 08 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.3-1
- update to https://github.com/containers/crun/releases/tag/1.4.3
- Related: #2061316

* Wed Jan 26 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.2-1
- update to https://github.com/containers/crun/releases/tag/1.4.2
- Related: #2000051

* Fri Jan 14 2022 Jindrich Novy <jnovy@redhat.com> - 1.4.1-1
- update to https://github.com/containers/crun/releases/tag/1.4.1
- Related: #2000051

* Wed Dec 22 2021 Jindrich Novy <jnovy@redhat.com> - 1.4-1
- update to https://github.com/containers/crun/releases/tag/1.4
- Related: #2000051

* Fri Nov 05 2021 Jindrich Novy <jnovy@redhat.com> - 1.3-1
- update to https://github.com/containers/crun/releases/tag/1.3
- Related: #2000051

* Mon Oct 11 2021 Jindrich Novy <jnovy@redhat.com> - 1.2-1
- update to https://github.com/containers/crun/releases/tag/1.2
- Related: #2000051

* Fri Oct 01 2021 Jindrich Novy <jnovy@redhat.com> - 1.1-3
- perform only sanity/installability tests for now
- Related: #2000051

* Wed Sep 29 2021 Jindrich Novy <jnovy@redhat.com> - 1.1-2
- add gating.yaml
- Related: #2000051

* Wed Sep 29 2021 Jindrich Novy <jnovy@redhat.com> - 1.1-1
- update to https://github.com/containers/crun/releases/tag/1.1
- Related: #2000051

* Fri Sep 03 2021 Jindrich Novy <jnovy@redhat.com> - 1.0-1
- update to https://github.com/containers/crun/releases/tag/1.0
- Related: #2000051

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.21-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Aug 06 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-3
- do not use versioned provide
- Resolves: #1974951

* Fri Jul 30 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-2
- re-add versioned provide
- Related: #1970747

* Tue Jul 27 2021 Jindrich Novy <jnovy@redhat.com> - 0.21-1
- update to https://github.com/containers/crun/releases/tag/0.21
- Related: #1970747

* Tue Jun 22 2021 Lokesh Mandvekar <lsm5@redhat.com> - 0.20.1-4
- Resolves: #1974951 - Versionless oci-runtime

* Tue Jun 15 2021 Jindrich Novy <jnovy@redhat.com> - 0.20.1-3
- add BR: criu-devel
- Resolves: #1944964

* Mon Jun 14 2021 Jindrich Novy <jnovy@redhat.com> - 0.20.1-2
- update to https://github.com/containers/crun/releases/tag/0.20.1
- Related: #1970747

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 0.19-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Apr 06 2021 Jindrich Novy <jnovy@redhat.com> - 0.19-1
- update to https://github.com/containers/crun/releases/tag/0.19

* Fri Feb 19 2021 Jindrich Novy <jnovy@redhat.com> - 0.18-2
- allow to build without glibc-static (thanks to Giuseppe Scrivano)

* Fri Feb 19 2021 Jindrich Novy <jnovy@redhat.com> - 0.18-1
- update to https://github.com/containers/crun/releases/tag/0.18

* Tue Jan 26 2021 Jindrich Novy <jnovy@redhat.com> - 0.17-1
- update to https://github.com/containers/crun/releases/tag/0.17

* Thu Dec 03 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-2
- exclude i686 because of build failures
- Related: #1883490

* Wed Nov 25 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-1
- update to https://github.com/containers/crun/releases/tag/0.16

* Wed Nov 04 2020 Jindrich Novy <jnovy@redhat.com> - 0.15.1-1
- update to https://github.com/containers/crun/releases/tag/0.15.1

* Thu Oct 29 2020 Jindrich Novy <jnovy@redhat.com> - 0.15-2
- backport "exec: check read bytes from sync" (gscrivan@redhat.com)
  (https://github.com/containers/crun/issues/511)

* Wed Sep 23 2020 Jindrich Novy <jnovy@redhat.com> - 0.15-1
- update to https://github.com/containers/crun/releases/tag/0.15

* Tue Aug 11 2020 Jindrich Novy <jnovy@redhat.com> - 0.14.1-2
- use proper CFLAGS
- Related: #1821193

* Wed Jul 08 2020 Jindrich Novy <jnovy@redhat.com> - 0.14.1-1
- update to https://github.com/containers/crun/releases/tag/v0.14.1
- Related: #1821193

* Thu Jul 02 2020 Jindrich Novy <jnovy@redhat.com> - 0.14-1
- update to https://github.com/containers/crun/releases/tag/v0.14
- Related: #1821193

* Tue Jun 16 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.13-1
- initial import
