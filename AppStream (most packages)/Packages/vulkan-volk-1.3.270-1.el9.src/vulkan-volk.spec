%global debug_package %{nil}

Name:           vulkan-volk
Version:        1.3.270
Release:        1%{?dist}
Summary:        Meta loader for Vulkan API

License:        MIT
URL:            https://github.com/zeux/volk
Source0:        %url/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  vulkan-headers

Conflicts: volk

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Requires:       vulkan-headers

%description    devel
%{summary}

%prep
%autosetup -n volk-%{version} -p1

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DVOLK_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/volk.h
%{_includedir}/volk.c
%{_libdir}/cmake/volk/*.cmake
%{_libdir}/libvolk.a

%changelog
* Thu Jan 11 2024 José Expósito <jexposit@redhat.com> - 1.3.270-1
- Version 1.3.270
