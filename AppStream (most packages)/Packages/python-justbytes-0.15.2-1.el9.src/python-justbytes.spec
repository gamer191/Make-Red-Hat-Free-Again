%global srcname justbytes

Name:           python-%{srcname}
Version:        0.15.2
Release:        1%{?dist}
Summary:        Library for handling computation with address ranges in bytes

License:        LGPL-2.1-or-later
URL:            http://pypi.python.org/pypi/justbytes
Source0:        https://pypi.io/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for handling computations with address ranges. The library also offers\
a configurable way to extract the representation of a value.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-justbases

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf justbytes.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/justbytes/
%{python3_sitelib}/justbytes-%{version}-*.egg-info/

%changelog
* Tue May 16 2023 Bryan Gurney <bgurney@redhat.com> - 0.15.2-1
- Update to 0.15.2
- Resolves: rhbz#2204503

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.15-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 29 2021 Bryan Gurney <bgurney@redhat.com> - 0.15-5
- Remove check test
- Remove BuildRequires and Requires for python3-justbases
- Resolves: rhbz#1986913

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.15-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 22 2021 mulhern <amulhern@redhat.com> - 0.15-3
- Use the correct tarball

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 mulhern <amulhern@redhat.com> - 0.15-1
- Update to 0.15

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 mulhern <amulhern@redhat.com> - 0.14-1
- Update to new release

* Thu Apr 23 2020 mulhern <amulhern@redhat.com> - 0.12-1
- Change license to LGPLv2+

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11-5
- Subpackage python2-justbytes has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-1
- Update to 0.11

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10-2
- Rebuild for Python 3.6

* Wed Aug 10 2016 mulhern <amulhern@redhat.com> - 0.10
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 23 2016 mulhern <amulhern@redhat.com> - 0.6
- Initial release
