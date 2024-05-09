Name:           sevctl
Version:        0.4.2
Release:        1%{?dist}
Summary:        Administrative utilities for AMD SEV

License:        ASL 2.0
URL:            https://github.com/virtee/sevctl

# sevctl sources
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz

ExclusiveArch:  x86_64
BuildRequires:  rust-toolset
BuildRequires:  openssl-devel

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}
%cargo_prep -V 1

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jul 28 2023 Tyler Fanelli <tfanelli@redhat.com> - 0.4.2-1
- Rebase to 0.4.2
- Related: rhbz2222104
- Related: rhbz2104857

* Mon Jul 17 2023 Tyler Fanelli <tfanelli@redhat.com> - 0.4.1-2
- Remove snphost and snpguest CLI tools.
- Related: rhbz2222104
- Related: rhbz2104857

* Mon Jul 10 2023 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.4.1
- Add snphost and snpguest CLI utilities along with sevctl
- Related: rhbz2222043

* Mon Nov 28 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.3.2
- Related: rhbz2135747

* Fri Jul 1 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.3.0
- Related: rhbz2085086

* Thu Jan 27 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.2.0
- Related: rhbz2037961

* Thu Aug 26 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-2
- No-change rebuild for gating.yaml

* Wed Apr 14 2021 Connor Kuehl <ckuehl@redhat.com>
- Initial package
