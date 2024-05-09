%global pypi_name sip

Name:           sip6
Version:        6.6.2
Release:        2%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6

# code_generator/parser.{c.h} is GPLv2+ with exceptions (bison)
License:        (GPLv2 or GPLv3) and (GPLv2+ with exceptions)
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        %{pypi_source}
Patch0:         323d39a2d602

# Bug 2225259 - regression bug when using sub-classed C++ exceptions
Patch1:         sip6-fix-exception-handling.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist packaging ply setuptools toml}

%global _description %{expand:
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries.  It was originally developed in 1998 to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create bindings for
any C or C++ library.  For example it is also used to generate wxPython, the
Python bindings for wxWidgets.}

%description %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%build
%py3_build

%install
%py3_install

%check
%py3_check_import sipbuild sipbuild.distinfo sipbuild.module sipbuild.tools


%files
%doc README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/sip*
%{python3_sitearch}/sip-*
%{python3_sitearch}/sipbuild/

%changelog
* Tue Jul 25 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.2-2
- Fixed the handling of exceptions that sub-class C++ exceptions
  Resolves: bz#2225259

* Mon Oct 24 2022 Jan Grulich <jgrulich@redhat.com> - 6.6.2-1
- 6.6.2
  Resolves: bz#2118862

* Tue Apr 19 2022 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- Initial package
  Resolves: bz#2071748
