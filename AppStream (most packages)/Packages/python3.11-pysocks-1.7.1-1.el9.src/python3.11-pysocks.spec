%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%if 0%{?fedora}
%global with_python3_tests 1
%endif

%global pypi_name   PySocks
%global modname     pysocks
%global sum         A Python SOCKS client module

Name:               python%{python3_pkgversion}-%{modname}
Version:            1.7.1
Release:            1%{?dist}
Summary:            %{sum}

License:            BSD
URL:                https://github.com/Anorov/%{pypi_name}
Source0:            %pypi_source
BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-rpm-macros
BuildRequires:      python%{python3_pkgversion}-setuptools
# for tests
%if 0%{?with_python3_tests}
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-psutil
BuildRequires:      python%{python3_pkgversion}-test_server
%endif

%global _description \
A fork of SocksiPy with bug fixes and extra features.\
\
Acts as a drop-in replacement to the socket module. Featuring:\
\
- SOCKS proxy client for Python 2.6 - 3.x\
- TCP and UDP both supported\
- HTTP proxy client included but not supported or recommended (you should use\
  urllib2's or requests' own HTTP proxy interface)\
- urllib2 handler included.

%description
%_description


%prep
%autosetup -n %{pypi_name}-%{version}
# drop useless 3rdparty code
rm -rfv test/bin

%build
%py3_build

%install
%py3_install

%check
# https://github.com/Anorov/PySocks/issues/37
# FIXME python module named test_server is needed but not packaged
%if 0%{?with_python3_tests}
%{__python3} setup.py test
%endif



%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/socks.py*
%{python3_sitelib}/sockshandler.py*
%{python3_sitelib}/__pycache__/*socks*
%{python3_sitelib}/%{pypi_name}-%{version}-*


%changelog
* Mon Nov 14 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.7.1-1
- Initial package
- Fedora contributions by:
      Carl George <carl@george.computer>
      Charalampos Stratakis <cstratak@redhat.com>
      Kevin Fenzi <kevin@scrye.com>
      Miro Hrončok <miro@hroncok.cz>
      Petr Viktorin <pviktori@redhat.com>
      Ralph Bean <rbean@redhat.com>
      Raphael Groner <raphgro@fedoraproject.org>
      Tim Orling <timothy.t.orling@linux.intel.com>
