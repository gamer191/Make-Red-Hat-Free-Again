%global uname         jigawatts

# For snapshots. Currently unused.
%global uversion      a5f8e31a4a967059498f820c5728f1deb0736c69
%global dversion      %(echo %{uversion} | sed s/-/_/)
%global shortcommit %(c=%{uversion}; echo ${c:0:7})
%global commitdate 20210827

%global aarch64       aarch64 arm64 armv8

Name:    %{uname}
Version: 1.21.0.0.0
Release: 4%{?dist}
Summary: Java CRIU helper
License: GPLv2 with exceptions
URL:     https://github.com/chflood/%{uname}
Source0: https://github.com/chflood/%{uname}/archive/refs/tags/%{version}.tar.gz

BuildRequires: java-devel
BuildRequires: criu-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake

Requires:   java-headless

# criu is only available on these architectures
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x

%description
CRIU is a Linux utility that allows the checkpointing and restoring
of processes.You can read more about CRIU at criu.org. CRIU for
Java is a package which makes it more convenient to use CRIU from
Java.

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
Javadoc for %{name}

%prep
%setup -q

./autogen.sh

%build

%configure

make

%install

rm -rf $RPM_BUILD_ROOT
%make_install

%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%dir %{_defaultlicensedir}/%{name}
%license %{_defaultlicensedir}/%{name}/LICENSE.md
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{uname}.jar
%{_libdir}/libJigawatts.so

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Apr 06 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1.21.0.0.0-4
- Bump release number to make RHEL 9.1 build later than RHEL 9 Beta & RHEL 9 GA builds
- Resolves: rhbz#2071920

* Thu Sep 02 2021 Jiri Vanek <jvanek@redhat.com> - 1.21.0.0.0-2
- Added gating yaml
- Resolves: rhbz#1989529

* Tue Aug 31 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1.21.0.0.0-1
- Rebase to upstream release, 1.21.0.0.0.
- Resolves: rhbz#1972029

* Sun Aug 29 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1.0~SNAPSHOT^20210827.a5f8e31-1
- Store the upstream version (currently "1.0-SNAPSHOT") and snapshot info completely in the Version field rather than using Release.
- Resolves: rhbz#1972029

* Sat Aug 28 2021 Andrew Hughes <gnu.andrew@redhat.com> - 0.2-0.4.20210807b2d3751
- Update to latest upstream version with renamed package and consistent use of "jigawatts"
- Drop library patch which is no longer needed.
- Resolves: rhbz#1972029

* Mon Aug 02 2021 Andrew Hughes <gnu.andrew@redhat.com> - 0.2-0.3.20210802a3007aa
- Rewrite to use autotools build system, avoiding need for Maven dependencies missing in RHEL 9.
- This also ensures use of the standard build flags and installs the jar in the expected location.
- Resolves: rhbz#1972029

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-0.2.20210701c15dd4c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Jiri Vanek <jvanek@redhat.com> - 0.2-0.1.20210701c15dd4c
- criu-devel moved to BR
- now requires criu-libs
- enabled debuginfo generation
- excluded i686 build as criu is 64b only
- .so file moved out of jar. Required teo patches:
- added and applied patch0 output_loc.patch
- added and applied patch1 load_library.patch
- on aarch64 workarounded missing lib64 on /usr/LD_LIBRARY_PATH

* Wed Apr 14 2021 Jiri Vanek <jvanek@redhat.com> - 0.2-0.1.20210701c15dd4c
- initial build
- added requires of criu-devel
