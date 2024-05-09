%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

Name:           python%{python3_pkgversion}-charset-normalizer
Version:        2.1.0
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest


%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.


%prep
%autosetup -n charset_normalizer-%{version}
# Remove pytest-cov settings from setup.cfg
sed -i "/addopts = --cov/d" setup.cfg

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/normalizer{,-%{python3_version}}

%check
%pytest

%files -n python%{python3_pkgversion}-charset-normalizer
%license LICENSE
%doc README.md
%{_bindir}/normalizer-%{python3_pkgversion}
%{python3_sitelib}/charset_normalizer/
%{python3_sitelib}/charset_normalizer-%{version}-py%{python3_pkgversion}.egg-info/

%changelog
* Mon Oct 24 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.1.0-1
- Initial package
- Fedora contributions by:
      Gwyn Ciesla <limb@fedoraproject.org>
      Lumir Balhar <lbalhar@redhat.com>
