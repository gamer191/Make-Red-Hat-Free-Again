%global pkg_name pyqt5-sip
%global pypi_name PyQt5_sip
%global _sip_api_major 12
%global _sip_api_minor 11
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-%{pkg_name}
Version:        12.11.1
Release:        1%{?dist}
Summary:        The sip module support for PyQt5

License:        GPLv2 or GPLv3
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools} >= 30.3
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
The sip extension module provides support for the PyQt5 package.
}

%description %_description

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Provides: python3-pyqt5-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt5-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-%{pkg_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README
%{python3_sitearch}/PyQt5_sip*
%{python3_sitearch}/PyQt5/

%changelog
* Fri Apr 21 2023 Jan Grulich <jgrulich@redhat.com> - 12.11.1-1
- 12.11.1
  Resolves: bz#2188589

* Thu May 26 2022 Jan Grulich <jgrulich@redhat.com> - 12.9.1-1
- Initial package
  Resolves: bz#2090327
