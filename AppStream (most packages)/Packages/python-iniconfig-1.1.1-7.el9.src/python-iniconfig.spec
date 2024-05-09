Name:               python-iniconfig
Version:            1.1.1
Release:            7%{?dist}
Summary:            Brain-dead simple parsing of ini files
License:            MIT
URL:                http://github.com/RonnyPfannschmidt/iniconfig
BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      pyproject-rpm-macros

Source0:            %{pypi_source iniconfig}

# Tests are disabled to remove the test dependencies
# Specify --with tests to run the tests on e.g. EPEL
%bcond_with tests

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%package -n python3-iniconfig
Summary:            %{summary}
%description -n python3-iniconfig %_description


%prep
%autosetup -n iniconfig-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files iniconfig


%if %{with tests}
%check
%tox
%endif


%files -n python3-iniconfig -f %{pyproject_files}
%doc README.txt
%license LICENSE


%changelog
* Tue Feb 22 2022 Tomas Orsava <torsava@redhat.com> - 1.1.1-7
- Add gating configuration and a simple smoke test
- Related: rhbz#1950291

* Tue Feb 08 2022 Tomas Orsava <torsava@redhat.com> - 1.1.1-6
- Add automatically generated Obsoletes tag with the python39- prefix
  for smoother upgrade from RHEL8
- Related: rhbz#1990421

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.1-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.1-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 08 2021 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-3
- Disable tests on RHEL9 to remove tox dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1888157)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Initial package (#1856421)
