%global srcname dbus-signature-pyparsing

Name:           python-%{srcname}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Parser for a D-Bus Signature

License:        Apache-2.0
URL:            https://github.com/stratis-storage/dbus-signature-pyparsing
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyparsing

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/dbus_signature_pyparsing/
%{python3_sitelib}/dbus_signature_pyparsing-*.egg-info/

%changelog
* Tue May 09 2023 Bryan Gurney <bgurney@redhat.com> - 0.4.1-1
- Update to 0.4.1
- Resolves: rhbz#2196269

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.04-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 28 2021 Bryan Gurney <bgurney@redhat.com> - 0.04-4
- Remove check test
- Remove Requires and BuildRequires for python3-pyparsing
- Resolves: rhbz#1986574

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.04-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 mulhern <amulhern@redhat.com> - 0.04-1
  Update to 0.04

* Tue Aug 04 2020 mulhern <amulhern@redhat.com> - 0.03-14
  Run check with deterministic tests only

* Tue Aug 04 2020 mulhern <amulhern@redhat.com> - 0.03-13
  Rebuild to pass non-deterministic tests on very slow machine

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.03-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.03-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.03-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.03-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.03-1
- Initial package
