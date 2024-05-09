%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

Name:           python%{python3_pkgversion}-cffi
%global general_version 1.15.1
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python to call C code
License:        MIT
URL:            https://cffi.readthedocs.org/
Source:         https://foss.heptapod.net/pypy/cffi/-/archive/v%{version}/cffi-v%{version}.tar.bz2

# Adjust tests for a last minute Python 3.11 change in the traceback format 
Patch0:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/113.patch

# Drop usage of the deprecated py.test package
Patch1:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/115.patch
# Drop usage of the deprecated py.code package
Patch2:          https://foss.heptapod.net/pypy/cffi/-/merge_requests/116.patch

BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gcc

BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pycparser

Requires:       python%{python3_pkgversion}-pycparser

# For tests:
BuildRequires:  gcc-c++

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%prep
%autosetup -p1 -n cffi-v%{general_version}%{?prerel}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest c/ testing/

%files -n python%{python3_pkgversion}-cffi
%doc README.md
%license LICENSE
%{python3_sitearch}/cffi/
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi-%{general_version}%{?prerel}-py%{python3_version}.egg-info/

%changelog
* Tue Nov 29 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.15.1-1
- Initial package
- Fedora contributions by:
      Charalampos Stratakis <cstratak@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Eric Smith <brouhaha@fedoraproject.org>
      Gwyn Ciesla <limburgher@gmail.com>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Joel Capitao <jcapitao@redhat.com>
      John Dulaney <jdulaney@fedoraproject.org>
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Nathaniel McCallum <nathaniel@themccallums.org>
      Orion Poplawski <orion@cora.nwra.com>
      Parag Nemade <pnemade@redhat.com>
      Peter Robinson <pbrobinson@fedoraproject.org>
      Petr Viktorin <pviktori@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Slavek Kabrda <bkabrda@redhat.com>
      Tomáš Hrnčiar <thrnciar@redhat.com>
      Tom Stellard <tstellar@redhat.com>
      Troy Dawson <tdawson@redhat.com>
