# Created by pyp2rpm-3.3.8
%global pypi_name pefile
%global pypi_version 2023.2.7

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        Python PE parsing module

License:        MIT
URL:            https://github.com/erocarrera/pefile
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
Source1:        pefile-tests.sh
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pefile is a multi-platform Python module to parse and work with Portable
Executable (PE) files. Most of the information contained in the PE file
headers is accessible, as well as all the sections' details and data.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pefile is a multi-platform Python module to parse and work with Portable
Executable (PE) files. Most of the information contained in the PE file
headers is accessible, as well as all the sections' details and data.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp %{SOURCE1} %{buildroot}%{_datadir}/%{name}

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/pefile.py
%{python3_sitelib}/peutils.py
%{python3_sitelib}/ordlookup
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info
%{_datadir}/%{name}

%changelog
* Thu May 25 2023 Gerd Hoffmann <kraxel@redhat.com> - 2023.2.7-3
- Add gating configuration.

* Thu May 25 2023 Gerd Hoffmann <kraxel@redhat.com> - 2023.2.7-2
- Added test script and configuration.

* Tue May 23 2023 Gerd Hoffmann <kraxel@redhat.com> - 2023.2.7-1
- Initial package.
