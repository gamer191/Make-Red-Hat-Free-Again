%global srcname dbus-python-client-gen

Name:           python-%{srcname}
Version:        0.8.3
Release:        1%{?dist}
Summary:        Python Library for Generating dbus-python Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-python-client-gen
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
# Required due to a setuptools bug that was fixed in setuptools 61.0.
# Previous to that version, setuptools loads the __init__.py module to
# obtain the value of the __version__ attribute.
BuildRequires:  python3-dbus
BuildRequires:  python3-into-dbus-python >= 0.08

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
%{python3_sitelib}/dbus_python_client_gen/
%{python3_sitelib}/dbus_python_client_gen-*.egg-info/

%changelog
* Fri Apr 28 2023 Bryan Gurney <bgurney@redhat.com> - 0.8.3-1
- Update to 0.8.3
- Resolves: rhbz#2189682

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.8-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 29 2021 Bryan Gurney <bgurney@redhat.com> - 0.8-4
- Remove check test
- Remove BuildRequires for python3-dbus and python3-into-dbus-python
- Resolves: rhbz#1986608

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.8-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 8 2020 mulhern <amulhern@redhat.com> - 0.8-1
- Update to 0.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7-2
- Rebuilt for Python 3.7

* Tue May 1 2018 Andy Grover <agrover@redhat.com> - 0.7-1
- Update to 0.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-1
- Update to 0.6

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5-1
- Initial import
