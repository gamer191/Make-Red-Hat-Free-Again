%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# tests are enabled by default
%bcond_without tests

%global python_wheelname six-%{version}-py2.py3-none-any.whl

Name:           python%{python3_pkgversion}-six
Version:        1.16.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        %{pypi_source six}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-tkinter
%endif

%global _description %{expand:
Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal
of writing Python code that is compatible on both Python versions.}

%description %{_description}


%prep
%autosetup -p1 -n six-%{version}


%build
%py3_build_wheel


%install
%py3_install_wheel %{python_wheelname}


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-six
%license LICENSE
%doc README.rst documentation/index.rst
%{python3_sitelib}/six-*.dist-info/
%pycached %{python3_sitelib}/six.py


%changelog
* Fri Nov 11 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.16.0-1
- Initial package
- Fedora contributions by:
      Bohuslav Kabrda <bkabrda@redhat.com>
      Charalampos Stratakis <cstratak@redhat.com>
      David Malcolm <dmalcolm@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Haikel Guemar <hguemar@fedoraproject.org>
      Igor Gnatenko <ignatenko@redhat.com>
      Karolina Surma <ksurma@redhat.com>
      Lumir Balhar <lbalhar@redhat.com>
      Matthias Runge <mrunge@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Orion Poplawski <orion@nwra.com>
      Pádraig Brady <P@draigBrady.com>
      Petr Viktorin <pviktori@redhat.com>
      Ralph Bean <rbean@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Slavek Kabrda <bkabrda@redhat.com>
      Tomas Hrnciar <thrnciar@redhat.com>
      Tomas Orsava <torsava@redhat.com>
      Tom Callaway <spot@fedoraproject.org>
      yatin <ykarel@redhat.com>
