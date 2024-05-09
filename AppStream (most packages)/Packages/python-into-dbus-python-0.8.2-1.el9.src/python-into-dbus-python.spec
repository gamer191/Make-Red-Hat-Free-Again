%global srcname into-dbus-python

Name:           python-%{srcname}
Version:        0.8.2
Release:        1%{?dist}
Summary:        Transformer to dbus-python types

License:        Apache-2.0
URL:            https://github.com/stratis-storage/into-dbus-python
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Facilities for converting an object that inhabits core Python types, e.g.,\
lists, ints, dicts, to an object that inhabits dbus-python types, e.g.,\
dbus.Array, dbus.UInt32, dbus.Dictionary based on a specified dbus signature.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Required due to a setuptools bug that was fixed in setuptools 61.0.
# Previous to that version, setuptools loads the __init__.py module to
# obtain the value of the __version__ attribute.
BuildRequires:  python3-dbus-signature-pyparsing
BuildRequires:  python3-dbus

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
%{python3_sitelib}/into_dbus_python/
%{python3_sitelib}/into_dbus_python-*.egg-info/

%changelog
* Fri May 05 2023 Bryan Gurney <bgurney@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Resolves: rhbz#2193199

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.08-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 29 2021 Bryan Gurney <bgurney@redhat.com> - 0.08-4
- Remove check test
- Remove BuildRequires for python3-dbus-signature-pyparsing and python3-dbus
- Resolves: rhbz#1986609

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.08-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 7 2020 mulhern<amulhern@redhat.com> - 0.08-1
- New version: 0.08

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.07-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 6 2019 mulhern <amulhern@redhat.com> - 0.07-2
- Use tracing profile for tests

* Fri Sep 6 2019 mulhenr <amulhern@redhat.com> - 0.07-1
- New version: 0.07

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.06-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.06-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.06-1
- Initial package
