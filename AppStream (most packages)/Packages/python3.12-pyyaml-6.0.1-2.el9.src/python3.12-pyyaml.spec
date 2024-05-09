%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

Name:           python%{python3_pkgversion}-pyyaml
Version:        6.0.1
Release:        2%{?dist}
Summary:        YAML parser and emitter for Python

# SPDX
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source:         https://github.com/yaml/pyyaml/archive/%{version}.tar.gz

# Fix build with Cython 3
# Proposed upstream but refused (upstream does not want Cython 3)
Patch:          https://github.com/yaml/pyyaml/pull/731.patch

BuildRequires:  gcc
BuildRequires:  libyaml-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython

%py_provides    python%{python3_pkgversion}-yaml
%py_provides    python%{python3_pkgversion}-PyYAML

%global _description\
YAML is a data serialization format designed for human readability and\
interaction with scripting languages.  PyYAML is a YAML parser and\
emitter for Python.\
\
PyYAML features a complete YAML 1.1 parser, Unicode support, pickle\
support, capable extension API, and sensible error messages.  PyYAML\
supports standard YAML tags and provides Python-specific tags that\
allow to represent an arbitrary Python object.\
\
PyYAML is applicable for a broad range of tasks from complex\
configuration files to object serialization and persistence.

%description %_description


%prep
%autosetup -p1 -n pyyaml-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c

# we have a patch for Cython 3
sed -i 's/Cython<3.0/Cython/' pyproject.toml


%build
%py3_build


%install
%py3_install


%check
%{py3_test_envvars} %{python3} tests/lib/test_all.py


%files -n python%{python3_pkgversion}-pyyaml
%license LICENSE
%doc CHANGES README.md examples
%{python3_sitearch}/yaml/
%{python3_sitearch}/_yaml/
%{python3_sitearch}/PyYAML-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue Jan 23 2024 Miro Hrončok <mhroncok@redhat.com> - 6.0.1-2
- Rebuilt for timestamp .pyc invalidation mode

* Thu Oct 19 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 6.0.1-1
- Initial package
- Fedora contributions by:
      Bill Nottingham <notting@fedoraproject.org>
      Charalampos Stratakis <cstratak@redhat.com>
      Dan Horák <dan@danny.cz>
      David Malcolm <dmalcolm@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Ignacio Vazquez-Abrams <ivazquez@fedoraproject.org>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Jakub Čajka <jcajka@redhat.com>
      Jesse Keating <jkeating@fedoraproject.org>
      John Eckersberg <jeckersb@fedoraproject.org>
      Kalev Lember <klember@redhat.com>
      Karolina Surma <ksurma@redhat.com>
      Lumir Balhar <lbalhar@redhat.com>
      Mamoru Tasaka <mtasaka@fedoraproject.org>
      Miro Hrončok <miro@hroncok.cz>
      Peter Robinson <pbrobinson@fedoraproject.org>
      Petr Viktorin <pviktori@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Slavek Kabrda <bkabrda@redhat.com>
      Tom Callaway <spot@fedoraproject.org>
      Troy Dawson <tdawson@redhat.com>
      Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
