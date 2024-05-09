%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global srcname idna

Name:           python%{python3_pkgversion}-%{srcname}
Version:        3.4
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD and Python and Unicode
URL:            https://github.com/kjd/idna
Source0:        https://pypi.io/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
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

# setuptools currently does not support dynamic version,
# hence we set it statically in pyproject.toml
sed -i 's/dynamic.*/version=\"%{version}\"/g' pyproject.toml


%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest


%files
%license LICENSE.md
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Oct 21 2022 Charalampos Stratakis <cstratak@redhat.com> - 3.4-1
- Initial package
- Fedora contributions by:
      Charalampos Stratakis <cstratak@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Jeremy Cline <jeremy@jcline.org>
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Orion Poplawski <orion@cora.nwra.com>
      Paul Wouters <pwouters@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Tom Prince <tom.prince@ualberta.net>
