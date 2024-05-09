%global forgeurl https://github.com/skozina/kabi-dw
%global commitdate 20220110
%global commit 973fee0f575cc530347bac7f906e7967d4399735
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%forgemeta -i

Name:           kabi-dw
Version:        0
Release:        0.24%{?dist}
Summary:        Detect changes in the ABI between kernel builds
License:        GPLv3+
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         fix-ns-on-ET_DYN.patch

BuildRequires:  elfutils-devel
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  redhat-rpm-config
BuildRequires: make

%description
The aim of kabi-dw is to detect any changes in the ABI between the successive
builds of the Linux kernel. This is done by dumping the DWARF type information
(the .debug_info section) for the specific symbols into the text files and
later comparing the text files.

%prep
%forgesetup
%patch0 -p1

%build
LDFLAGS+=" -pie "
%ifarch x86_64
CFLAGS+=" -fcf-protection=full "
%endif
CFLAGS+=" -fPIE -D_GLIBCXX_ASSERTIONS -fstack-clash-protection -g"
%set_build_flags
%make_build

%install
install -dm 755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
%doc README.md
%license COPYING

%changelog
* Tue Jan 18 2022 Cestmir Kalina <ckalina@redhat.com> - 0.24
- Fix annocheck failures
- Fix osci tier0 test reference
- Fix ET_DYN vmlinux namespace support
- Resolves: rhbz#2038913
- Resolves: rhbz#2045976
- Resolves: rhbz#2038892

* Mon Jan 10 2022 Cestmir Kalina <ckalina@redhat.com> - 0.23
- Add support for ET_EXEC
- Add support for DW_TAG_restrict_type
- Resolves: rhbz#1761409

* Mon Nov 22 2021 Cestmir Kalina <ckalina@redhat.com> - 0.22
- Add support for symbol namespaces
- Resolves: rhbz#1761409

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - Forge-specific packaging variables
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - Forge-specific packaging variables
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 9 2020 Zamir SUN <zsun@fedoraproject.org> - 0-0.17.20191127gitbd56a60
- Workaround "multiple definition of `yyin'"
- Resolves https://bugzilla.redhat.com/show_bug.cgi?id=1799559

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Zamir SUN <zsun@fedoraproject.org> - 0-0.15.20191127gitbd56a60
- Update to bd56a60

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20181112git6fbd644
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20181112git6fbd644
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.12.20181112git6fbd644
- Update to 6fbd644 to fix RHBZ 1642806

* Wed Sep 19 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.11.20180906git626d942
- Fix the date in previous commit

* Wed Sep 19 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.10.20180906git626d942
- Update to upstream 626d94295bc83e01ed98f4ecb76d7d499341f738

* Sun Jul 22 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.9.20180308gitb8863d0
- Add gcc as BR.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180308gitb8863d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.7.20180308gitb8863d0
- Update to b8863d05565e91bd3fb40d9e9d562be081f09669
- Fixes RHBZ#1543803

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180130git545535a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.5-20180130git545535a
- Update to upstream 545535ab2d5ea093074f5df5723901756d22f298
- Fixes RHBZ#1538977

* Wed Jan 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.4.20171201gita6bced6
- Update do upstream a6bced6ef7b263380ac0309bdbd4a98c6f9055eb

* Wed Jan 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.3.20171018gite6af311
- Add libasan-devel per request

* Fri Oct 27 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20171018gite6af311
- Update to upstream e6af311e3182417f86742a5b1a78e488593f975a

* Mon Oct 16 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20171012git2ef3f81
- Initial package kabi-dw
