# Created by pyp2rpm-3.3.6
%global pypi_name resolvelib
%global python3_pkgversion 3
%global python39_sitelib /usr/lib/python3.9/site-packages/
%global commitId d935f9fd07246d9641436c7a8e6ae39423374e28

Name:           python-%{pypi_name}
Version:        0.5.4
Release:        5%{?dist}
Summary:        Resolve abstract dependencies into concrete ones

License:        ISC
URL:            https://github.com/sarugaku/resolvelib.git
Source0:        resolvelib-d935f9fd07246d9641436c7a8e6ae39423374e28.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
ResolveLib at the highest level provides a Resolver class that
includes dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result. Intended Usage :: import resolvelib Things I want to
resolve. requirements [...] Implement logic so the resolver understands the
requirement format. class...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

#Requires:       python3dist(black)
#Requires:       python3dist(commentjson)
#Requires:       python3dist(flake8)
#Requires:       python3dist(html5lib)
#Requires:       python3dist(packaging)
#Requires:       python3dist(packaging)
#Requires:       python3dist(pygraphviz)
#Requires:       python3dist(pytest)
#Requires:       python3dist(requests)
#Requires:       python3dist(setl)
#Requires:       python3dist(towncrier)

%description -n python%{python3_pkgversion}-%{pypi_name}
ResolveLib at the highest level provides a Resolver class that
includes dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result. Intended Usage :: import resolvelib Things I want to
resolve. requirements [...] Implement logic so the resolver understands the
requirement format. class...

%prep
%autosetup -n %{pypi_name}-%{commitId}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python39_sitelib}/%{pypi_name}
%{python39_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 14 2021 Paul Belanger <pabelanger@redhat.com> - 0.5.4-1
- Initial package.
- Forked from https://fedora.pkgs.org/rawhide/fedora-x86_64/python3-resolvelib-0.5.5-2.fc35.noarch.rpm.html however
  downgraded to 0.5.4 due to 0.5.5 being yanked from pypi.
