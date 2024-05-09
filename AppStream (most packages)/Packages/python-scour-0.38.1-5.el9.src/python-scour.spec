%global modname scour
%global sum     An SVG scrubber

Name:               python-scour
Version:            0.38.1
%global	gitversion  038.1
Release:            5%{?dist}
Summary:            %{sum}

License:            ASL 2.0
URL:                https://github.com/scour-project/scour
Source0:            %{url}/archive/v%{gitversion}.tar.gz#/%{modname}-%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
# Tests
%if !0%{?rhel}
%if !0%{?centos}
BuildRequires:      python3-six
BuildRequires:      python3-flake8
%endif
%endif

BuildArch:          noarch

%description
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}


%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{gitversion}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%build
%py3_build

%install
%py3_install


%check
%if !0%{?rhel}
%if !0%{?centos}
%{__python3} setup.py test
%endif
%endif

%{!?_licensedir: %global license %doc}

%files -n python3-%{modname}
%doc README.md
%license LICENSE
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.38.1-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 22 2021 Jan Horak <jhorak@redhat.com> - 0.38.1-4
- Don't run tests on the centos and rhel because of missing required packages

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.38.1-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.38.1
- 0.38.1

* Tue Aug 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.38-1
- 0.38

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.37-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.37-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.37-4
- Drop Python 2.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.37-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.37-1
- 0.37

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.35-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.35-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.35-3
- Rebuild for Python 3.6

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-2
- Fix Source0.

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-1
- Initial package.
