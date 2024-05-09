%global sdkver 1.3.268.0

Name:           glslang
Version:        13.1.1
Release:        1%{?dist}
Summary:        OpenGL and OpenGL ES shader front end and validator

License:        BSD and GPLv3+ and ASL 2.0
URL:            https://github.com/KhronosGroup/%{name}
Source0:        %url/archive/vulkan-sdk-%{sdkver}.tar.gz#/%{name}-sdk-%{sdkver}.tar.gz
# Patch to build against system spirv-tools (rebased locally)
#Patch3:         https://patch-diff.githubusercontent.com/raw/KhronosGroup/glslang/pull/1722.patch#/0001-pkg-config-compatibility.patch
Patch3:         0001-pkg-config-compatibility.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  spirv-tools-devel

%description
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%prep
%autosetup -p1 -n %{name}-vulkan-sdk-%{sdkver}
# Fix rpmlint warning on debuginfo
find . -name '*.h' -or -name '*.cpp' -or -name '*.hpp'| xargs chmod a-x

%build
%cmake3 -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%{cmake_install}

# we don't want them in here
rm -rf %{buildroot}%{_includedir}/SPIRV

%ifnarch s390x ppc64
%check
pushd Test
./runtests localResults ../%{_vpath_builddir}/StandAlone/glslangValidator ../%{_vpath_builddir}/StandAlone/spirv-remap
popd
%endif

%files
%doc README.md README-spirv-remap.txt
%{_bindir}/glslang
%{_bindir}/glslangValidator
%{_bindir}/spirv-remap

%files devel
%{_includedir}/glslang/
%{_libdir}/libHLSL.a
%{_libdir}/libOGLCompiler.a
%{_libdir}/libOSDependent.a
%{_libdir}/libSPIRV.a
%{_libdir}/libSPVRemapper.a
%{_libdir}/libglslang.a
%{_libdir}/libGenericCodeGen.a
%{_libdir}/libMachineIndependent.a
%{_libdir}/libglslang-default-resource-limits.a
%{_libdir}/pkgconfig/glslang.pc
%{_libdir}/pkgconfig/spirv.pc
%{_libdir}/cmake/*

%changelog
* Wed Jan 17 2024 José Expósito <jexposit@redhat.com> - 13.1.1-1
- Update to 1.3.268.0 SDK

* Fri Jul 07 2023 Dave Airlie <airlied@redhat.com> - 11.9.0-5
- Latest snapshot used in 1.3.250.1 sdk

* Wed Feb 15 2023 Dave Airlie <airlied@redhat.com> - 11.9.0-4
- Latest snapshot used in 1.3.239 sdk

* Fri Aug 26 2022 Dave Airlie <airlied@redhat.com> - 11.9.0-3
- Latest snapshot used in 1.3.224 sdk

* Wed Jun 22 2022 Dave Airlie <airlied@redhat.com> - 11.9.0-2
- Latest snapshot used in 1.3.216 sdk

* Fri Feb 25 2022 Dave Airlie <airlied@redhat.com> - 11.9.0-1.20220202.git2742e95
- Latest snapshot used in 1.3.204 sdk

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 11.5.0-2.20210623.gitae2a562
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jul 30 2021 Dave Airlie <airlied@redhat.com> - 11.5.0-1
- Latest snapshot used in 1.2.182 sdk

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 11.0.0-5.20201208.gitc594de2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Jan 28 2021 Dave Airlie <airlied@redhat.com> - 11.0.0-4.20201208.gitc594de2
- Latest snapshot used in 1.2.162 sdk

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-3.20201104.gitd550beb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Dave Airlie <airlied@redhat.com> - 11.0.0-2
- Latest upstream snapshot

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 11.0.0-1
- Latest upstream snapshot

* Tue Aug 04 2020 Dave Airlie <airlied@redhat.com> - 8.13.3559-5
- Use cmake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.13.3559-4.2020421.gitc9b28b9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.13.3559-3.2020421.gitc9b28b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Dave Airlie <airlied@redhat.com> - 8.13.3559-2
- Update to latest git snapshot

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 8.13.3559-1
- Update to latest git snapshot

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.13.3496-3.20191102.git7f77b2e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Leigh Scott <leigh123linux@googlemail.com> - 7.13.3496-2.20191102.git7f77b2e
- Add patch for 'Fix a couple relative header paths in header'

* Wed Nov 13 2019 Dave Airlie <airlied@redhat.com> - 7.13.3496-1
- Latest upstream snapshot for validation layers build

* Sat Aug 03 2019 Dave Airlie <airlied@redhat.com> - 7.11.3214-3
- Latest upstream snapshot for validation layers build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11.3214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 01:27:27 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 7.11.3214-1
- Release 7.11.3214
- Add patch to build against system spirv-tools

* Fri Mar 29 2019 Dave Airlie <airlied@redhat.com> - 3.1-0.13.20190329.gite0d59bb
- Update for vulkan 1.1.101.0

* Tue Feb 12 2019 Dave Airlie <airlied@redhat.com> - 3.1-0.12.20190212.git05d12a9
- Update for vulkan 1.1.92.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.11.20180727.gite99a268
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.10.20180727.gite99a268
- Update for vulkan 1.1.82.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.9.20180416.git3bb4c48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.8.20180416.git3bb4c48
- Update for vulkan 1.1.73.0

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 3.1-0.7.20180205.git2651cca
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.6.20180205.git2651cca
- Update for vulkan 1.0.68.0

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.5.20171028.git715c353
- Use ninja to build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.4.20171028.git715c353
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.3.20171028.git715c353
- Exclude s390x and ppc64 from check section

* Wed Jan 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.2.20171028.git715c353
- Add check section to run tests
- Split binaries into main package

* Thu Jul 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.1-0.1.20171028.git715c353
- First build
