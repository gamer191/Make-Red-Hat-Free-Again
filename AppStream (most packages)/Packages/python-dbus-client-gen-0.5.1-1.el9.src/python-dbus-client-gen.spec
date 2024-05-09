%global srcname dbus-client-gen

Name:           python-%{srcname}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Library for Generating D-Bus Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-client-gen
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This library contains a few methods that consume an XML specification\
of a D-Bus interface and return classes or functions that may be useful\
in constructing a python D-Bus client. The XML specification has the format\
of the data returned by the Introspect() method\
of the Introspectable interface.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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
%{python3_sitelib}/dbus_client_gen/
%{python3_sitelib}/dbus_client_gen-*.egg-info/

%changelog
* Wed May 03 2023 Bryan Gurney <bgurney@redhat.com> - 0.5.1-1
- Update to 0.5.1
- Resolves: rhbz#2192384

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.5-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 28 2021 Bryan Gurney <bgurney@redhat.com> - 0.5-4
- Remove check test
- Resolves: rhbz#1986607

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.5-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 8 2020 mulhern <amulhern@redhat.com> - 0.5-1
- Update to 0.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4-1
- Update to 0.4

* Wed Aug 8 2018 Andy Grover <agrover@redhat.com> - 0.3-4
* Bump version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-2
- Rebuilt for Python 3.7

* Fri Jun 1 2018 Andy Grover <agrover@redhat.com> - 0.3-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-1
- Initial package
