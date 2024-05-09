# https://github.com/intel/numatop/pull/53
%undefine _ld_as_needed

Name:           numatop
Version:        2.4
Release:        1%{?dist}
Summary:        Memory access locality characterization and analysis

License:        BSD
URL:            https://01.org/numatop
Source:         https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  check-devel
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel

# This only works for Intel and Power CPUs
ExclusiveArch:  x86_64 ppc64le

#Patch001: v2.2-001-Initial-support-for-SPR.patch


%description
NumaTOP is an observation tool for runtime memory locality characterization and
analysis of processes and threads running on a NUMA system. It helps the user
characterize the NUMA behavior of processes and threads and identify where the
NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors and PowerPC processors.


%prep
#%setup -q -n %{name}-v%{version}
%autosetup -p1


%build
autoreconf --force --install --symlink
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Thu Feb  1 2024 Pingfan Liu <piliu@redhat.com> - 2.4.1
- Add initial support for EMR

* Fri Dec  8 2023 Pingfan Liu <piliu@redhat.com> - 2.3.3
- Add Power10 support

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.1-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.1-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Dridi Boukelmoune <dridi@fedoraproject.org>- 2.1-1
- Update to 2.1
- Upstream moved to github
- Upstream switched to autotools
- Disable --as-needed until it's patched upstream
- Drop defunct 32bit x86 support
- Add ppc64le support
- Run the new test suite

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Dridi Boukelmoune <dridi@fedoraproject.org>- 1.0.4-8
- Build requires gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Dridi Boukelmoune <dridi@fedoraproject.org>- 1.0.4-3
- Catch up with packaging guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-1
- Update to latest version (support for BDW-EP/EX)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-3
- Replace ExcludeArch with ExclusiveArch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 25 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- New upstream release (#1076549)
- Remove upstreamed patch

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.2-3
- Backport and rebase 1.0.1 patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.2-1
- Bump version to 1.0.2
- Remove upstreamed patch

* Fri Sep 20 2013 Dan Horák <dan[at]danny.cz> - 1.0.1-5
- no numa on s390(x)

* Fri Sep 13 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-4
- Patch for the 32bit hardened build.

* Sun Aug 25 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-3
- Hardened build.
- Automatic requires.

* Fri Aug 02 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-2
- Fix the license tag.

* Thu Aug 01 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-1
- Initial spec.
