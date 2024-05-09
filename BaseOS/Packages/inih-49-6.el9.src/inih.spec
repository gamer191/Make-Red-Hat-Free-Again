Name:     inih
Version:  49
Release:  6%{?dist}
Summary:  Simple INI file parser library

License:  BSD
URL:      https://github.com/benhoyt/inih
Source0:  %{url}/archive/r%{version}/%{name}-r%{version}.tar.gz

BuildRequires: gcc
BuildRequires: g++
BuildRequires: meson


%description
The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%package devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%prep
%autosetup -n %{name}-r%{version}


%build
%meson -Ddefault_library=shared -Ddistro_install=true
%meson_build


%install
%meson_install


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.0


%files devel
%{_includedir}/ini.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/lib%{name}.so


%changelog
* Fri Jun 10 2022 Eric Sandeen <sandeen@redhat.com> - 49-6
- Release bump, no changes

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 49-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 49-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Christian Kellner <ckellner@redhat.com> - 49-1
- New upstream release 49
- Switch to meson build system.
- Ship the pkg-config file.
- Remove ldconfig scriptlets.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jan F. Chadima <jfch@jagda.eu> - 36-5
- implement license tag

* Wed Aug 31 2016 Jan F. Chadima <jfch@jagda.eu> - 36-4
- implement next review hints

* Tue Aug 30 2016 Jan F. Chadima <jfch@jagda.eu> - 36-3
- implement another review results

* Tue Aug 30 2016 Jan F. Chadima <jfch@jagda.eu> - 36-2
- implement review results

* Mon Aug 29 2016 Jan F. Chadima <jfch@jagda.eu> - 36-1
- initial version
