%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

Name:           python%{python3_pkgversion}-charset-normalizer
Version:        3.3.0
Release:        2%{?dist}
Summary:        The Real First Universal Charset Detector
# SPDX
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
* Tue Jan 23 2024 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuilt for timestamp .pyc invalidation mode

* Tue Oct 17 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.3.0-1
- Initial package
- Fedora contributions by:
      Charalampos Stratakis <cstratak@redhat.com>
      Gwyn Ciesla <limb@fedoraproject.org>
      Lumír Balhar <lbalhar@redhat.com>

