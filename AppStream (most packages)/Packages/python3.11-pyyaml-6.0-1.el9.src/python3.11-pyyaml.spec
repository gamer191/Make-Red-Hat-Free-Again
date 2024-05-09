%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

Name:           python%{python3_pkgversion}-pyyaml
Version:        6.0
Release:        1%{?dist}
%global uversion %{version}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        https://github.com/yaml/pyyaml/archive/%{uversion}.tar.gz

BuildRequires:  gcc
BuildRequires:  libyaml-devel

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython

%py_provides    python%{python3_pkgversion}-yaml
%py_provides    python%{python3_pkgversion}-yaml%{?_isa}
%py_provides    python%{python3_pkgversion}-PyYAML
%py_provides    python%{python3_pkgversion}-PyYAML%{?_isa}

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
%setup -q -n pyyaml-%{uversion}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python%{python3_pkgversion}-pyyaml
%license LICENSE
%doc CHANGES README.md examples
%{python3_sitearch}/*


%changelog
* Mon Nov 14 2022 Charalampos Stratakis <cstratak@redhat.com> - 6.0-1
- Initial package
- Fedora contributions by:
      Bill Nottingham <notting@fedoraproject.org>
      Charalampos Stratakis <cstratak@redhat.com>
      Dan Horák <dan@danny.cz>
      David Malcolm <dmalcolm@redhat.com>
      Dennis Gilmore <ausil@fedoraproject.org>
      dmalcolm <dmalcolm@fedoraproject.org>
      Ignacio Vazquez-Abrams <ivazquez@fedoraproject.org>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Jakub Čajka <jcajka@redhat.com>
      Jesse Keating <jkeating@fedoraproject.org>
      John Eckersberg <jeckersb@fedoraproject.org>
      Kalev Lember <klember@redhat.com>
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
