%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

%global srcname idna

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.4
Release:        2%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD
URL:            https://github.com/kjd/idna
Source0:        https://pypi.io/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flit-core
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%{python3} -m flit_core.wheel

%install
%py3_install_wheel idna-%{version}-py3-none-any.whl

%check
%{python3} -m unittest


%files
%license LICENSE.md
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/idna-*.dist-info/

%changelog
* Tue Jan 23 2024 Miro Hrončok <mhroncok@redhat.com> - 3.4-2
- Rebuilt for timestamp .pyc invalidation mode

* Fri Oct 20 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.4-1
- Initial package
- Fedora contributions by:
      Charalampos Stratakis <cstratak@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Jeremy Cline <jeremy@jcline.org>
      Karolina Surma <ksurma@redhat.com>
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Orion Poplawski <orion@cora.nwra.com>
      Paul Wouters <pwouters@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Tom Prince <tom.prince@twistedmatrix.com>
