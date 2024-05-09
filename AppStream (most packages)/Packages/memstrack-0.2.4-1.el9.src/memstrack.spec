# vim: syntax=spec

Name:           memstrack
Version:        0.2.4
Release:        1%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPLv3
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/refs/tags/v%{version}.tar.gz

Patch1: 0001-Skip-memcg-info-in-__process_stacktrace-for-page_own.patch
Patch2: 0002-Fix-data-type-error-in-perf_handle_mm_page_alloc.patch

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%setup -q -n memstrack-%{version}
%patch1 -p1
%patch2 -p1

%build
%{set_build_flags}
%{make_build}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
* Fri Jul 15 2022 Tao Liu <ltao@redhat.com> - 0.2.4-1
- Rebase to latest upstream(813c2feaa2f)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.3-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jul 09 2021 Kairui Song <kasong@redhat.com> - 0.2.3-1
- Update to upstream latest release

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.2-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 08 2021 Kairui Song <kasong@redhat.com> - 0.2.2-1
- Update to upstream latest release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Timm Bäder <tbaeder@redhat.com> - 0.1.12-2
- Use %%make_build macro
  https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make

* Sun Aug 30 2020 Kairui Song <kasong@redhat.com> - 0.1.12-1
- Update to upstream latest release

* Thu Jul 30 2020 Kairui Song <kasong@redhat.com> - 0.1.9-1
- Update to upstream latest release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Kairui Song <kasong@redhat.com> - 0.1.8-1
- Update to upstream latest release

* Sat May 30 2020 Kairui Song <ryncsn@gmail.com> - 0.1.5-1
- Update to upstream latest release

* Tue Apr 21 2020 Kairui Song <ryncsn@gmail.com> - 0.1.2-1
- Update to upstream latest release

* Sun Mar 15 2020 Kairui Song <ryncsn@gmail.com> - 0-1.20200310gitee02de2
- First release
