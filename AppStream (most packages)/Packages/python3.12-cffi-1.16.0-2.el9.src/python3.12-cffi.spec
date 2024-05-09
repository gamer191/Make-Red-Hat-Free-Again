%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

Name:           python%{python3_pkgversion}-cffi
Version:        1.16.0
Release:        2%{?dist}
Summary:        Foreign Function Interface for Python to call C code
# cffi is MIT
# cffi/_imp_emulation.py has bits copied from CPython (Python)
License:        MIT and Python
URL:            https://github.com/python-cffi/cffi
Source:         %{url}/archive/v%{version}/cffi-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gcc

BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pycparser

# For tests:
BuildRequires:  gcc-c++

Requires:       python%{python3_pkgversion}-pycparser

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.


%prep
%autosetup -p1 -n cffi-%{version}


%build
%py3_build


%install
%py3_install


%check
%pytest


%files -n python%{python3_pkgversion}-cffi
%doc README.md
%license LICENSE
%{python3_sitearch}/cffi/
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi-*.egg-info/


%changelog
* Tue Jan 23 2024 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-2
- Rebuilt for timestamp .pyc invalidation mode

* Tue Oct 17 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.16.0-1
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

