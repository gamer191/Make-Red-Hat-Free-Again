%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global modname ply

%bcond_without tests

Name:           python%{python3_pkgversion}-%{modname}
Summary:        Python Lex-Yacc
Version:        3.11
Release:        1%{?dist}
License:        BSD
URL:            http://www.dabeaz.com/ply/
Source0:        http://www.dabeaz.com/ply/%{modname}-%{version}.tar.gz
# Fix build against Python 3.11
# https://github.com/dabeaz/ply/pull/262
Patch0:         262.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system. 


%prep
%setup -n %{modname}-%{version}
%patch0 -p1 -b .262
find example/ -type f -executable -exec chmod -x {} ';'
find example/ -type f -name '*.py' -exec sed -i \
  -e '1{\@^#!/usr/bin/env python@d}' -e '1{\@^#!/usr/local/bin/python@d}' \
  {} ';'
rm -rf *.egg-info
# extract license block from beginning of README.md
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
pushd test
  ./cleanup.sh
  %{__python3} testlex.py
  %{__python3} testyacc.py
popd
%endif

%files -n python%{python3_pkgversion}-%{modname}
%doc CHANGES README.md
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*.egg-info/

%changelog
* Fri Nov 11 2022 Charalampos Stratakis <cstratak@redhat.com> - 3.11-1
- Initial package
- Fedora contributions by:
      Bill Nottingham <notting@fedoraproject.org>
      Charalampos Stratakis <cstratak@redhat.com>
      Christian Heimes <cheimes@redhat.com>
      David Malcolm <dmalcolm@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Ignacio Vazquez-Abrams <ivazquez@fedoraproject.org>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Jesse Keating <jkeating@fedoraproject.org>
      Miro Hrončok <miro@hroncok.cz>
      Orion Poplawski <orion@cora.nwra.com>
      Patrik Kopkan <pkopkan@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Slavek Kabrda <bkabrda@redhat.com>
      Stephen Gallagher <sgallagh@redhat.com>
      Thomas Spura <tomspur@fedoraproject.org>
      Tom spot Callaway <spot@fedoraproject.org>
      Troy Dawson <tdawson@redhat.com>
