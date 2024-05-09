%global git0 https://github.com/rootless-containers/%{name}

Name: slirp4netns
Version: 1.2.3
Release: 1%{?dist}
Summary: slirp for network namespaces
License: GPLv2
URL: %{git0}
# build fails on i686 with: No matching package to install: 'go-md2man'
ExcludeArch: i686
Source0: %{git0}/archive/v%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git
BuildRequires: /usr/bin/go-md2man
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: make
BuildRequires: libslirp-devel

%description
slirp for network namespaces, without copying buffers across the namespaces.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Fri Feb 09 2024 Jindrich Novy <jnovy@redhat.com> - 1.2.3-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.3
- Related: RHEL-2112

* Fri Sep 15 2023 Jindrich Novy <jnovy@redhat.com> - 1.2.2-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.2
- Related: Jira:RHEL-2112

* Mon Aug 21 2023 Jindrich Novy <jnovy@redhat.com> - 1.2.1-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.1
- Related: #2176063

* Thu Feb 16 2023 Jindrich Novy <jnovy@redhat.com> - 1.2.0-3
- rebuild
- Resolves: #2129078

* Wed May 11 2022 Jindrich Novy <jnovy@redhat.com> - 1.2.0-2
- BuildRequires: /usr/bin/go-md2man
- Related: #2061316

* Mon May 02 2022 Jindrich Novy <jnovy@redhat.com> - 1.2.0-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.0
- Related: #2061316

* Thu Feb 17 2022 Jindrich Novy <jnovy@redhat.com> - 1.1.12-4
- update gating.yaml as we have no local tests in dist-git
- Related: #2000051

* Tue Feb 15 2022 Jindrich Novy <jnovy@redhat.com> - 1.1.12-3
- fix gating - don't use insecure functions - thanks to Marc-André Lureau
- Related: #2000051

* Tue Feb 15 2022 Jindrich Novy <jnovy@redhat.com> - 1.1.12-2
- add gating.yaml
- Related: #2000051

* Thu Nov 11 2021 Jindrich Novy <jnovy@redhat.com> - 1.1.12-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.12
- Related: #2000051

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.8-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.8-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Dec 04 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.8-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.8

* Thu Dec 03 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.7-2
- exclude i686 because of build failures
- Related: #1883490

* Thu Nov 26 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.7-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.7

* Mon Nov 09 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.6-2
- - be sure to harden the linked binary

* Thu Nov 05 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.6-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.6

* Wed Nov 04 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.5-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.5

* Thu Sep 17 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.4-2
- sync with rhel8-8.3.0
- use proper CFLAGS
- Related: #1821193

* Thu Feb 28 2019 Lokesh Mandvekar <lsm5@redhat.com> - 0.3.0-1.alpha.2.git30883b5
- bump to v0.3.0-alpha.2

* Fri Nov 16 2018 Frantisek Kluknavsky <fkluknav@redhat.com> - 0.1-2.dev.gitc4e1bc5
- changed summary

* Fri Aug 10 2018 Lokesh Mandvekar <lsm5@redhat.com> - 0.1-1.dev.gitc4e1bc5
- First package for RHEL 8
- import from Fedora rawhide
- Exclude ix86 and ppc64
