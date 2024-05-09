%global pesign_vre 0.106-1
%global gnuefi_vre 1:3.0.5-6
%global openssl_vre 1.0.2j

%global debug_package %{nil}
%global __debug_package 1
%global _binaries_in_noarch_packages_terminate_build 0
%global __debug_install_post %{SOURCE100} aa64
%undefine _debuginfo_subpackages

%global efidir %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))
%global shimrootdir %{_datadir}/shim/
%global shimversiondir %{shimrootdir}/%{version}-%{release}
%global efiarch aa64
%global shimdir %{shimversiondir}/%{efiarch}

Name:		shim-unsigned-aarch64
Version:	15
Release:	6%{?dist}
Summary:	First-stage UEFI bootloader
ExclusiveArch:	aarch64
License:	BSD
URL:		https://github.com/rhboot/shim
Source0:	https://github.com/rhboot/shim/releases/download/%{version}/shim-%{version}.tar.bz2
Source1:	securebootca.cer
# currently here's what's in our dbx:
# nothing.
Source2:	dbx.esl

Source100:	shim-find-debuginfo.sh

Patch0001:	0001-Make-sure-that-MOK-variables-always-get-mirrored.patch
Patch0002:	0002-mok-fix-the-mirroring-of-RT-variables.patch
Patch0003:	0003-mok-consolidate-mirroring-code-in-a-helper-instead-o.patch
Patch0004:	0004-Make-VLogError-behave-as-expected.patch
Patch0005:	0005-Make-EFI-variable-copying-fatal-only-on-secureboot-e.patch
Patch0006:	0006-Make-some-things-dprint-instead-of-console_print.patch
Patch0007:	0007-shim-Properly-generate-absolute-paths-from-relative-.patch
Patch0008:	0008-shim-Prevent-shim-to-set-itself-as-a-second-stage-lo.patch
Patch0009:	0009-Fix-a-use-of-strlen-instead-of-Strlen.patch
Patch0010:	0010-translate_slashes-don-t-write-to-string-literals.patch
Patch0011:	0011-RHEL-9-disable-Wpointer-sign-for-now.patch

BuildRequires:	gcc make
BuildRequires:	elfutils-libelf-devel
BuildRequires:	git openssl-devel openssl
BuildRequires:	pesign >= %{pesign_vre}
BuildRequires:	gnu-efi >= %{gnuefi_vre}
BuildRequires:	gnu-efi-devel >= %{gnuefi_vre}

# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI is not
# compatible with SysV (there's no red zone under UEFI) and there isn't a
# POSIX-style C library.
# BuildRequires:	OpenSSL
Provides:	bundled(openssl) = %{openssl_vre}

%global desc \
Initial UEFI bootloader that handles chaining to a trusted full \
bootloader under secure boot environments.
%global debug_desc \
This package provides debug information for package %{expand:%%{name}} \
Debug information is useful when developing applications that \
use this package or when debugging this package.

%description
%desc

%package debuginfo
Summary:	Debug information for shim-unsigned-aarch64
Requires:	%{name}-debugsource = %{version}-%{release}
Group:		Development/Debug
AutoReqProv:	0
BuildArch:	noarch

%description debuginfo
%debug_desc

%package debugsource
Summary:	Debug Source for shim-unsigned
Group:		Development/Debug
AutoReqProv:	0
BuildArch:	noarch

%description debugsource
%debug_desc

%prep
%autosetup -S git -n shim-%{version}
git config --unset user.email
git config --unset user.name
mkdir build-%{efiarch}

%build
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
MAKEFLAGS+="%{_smp_mflags}"
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} DEFAULT_LOADER='\\\\grub%{efiarch}.efi' all
cd ..

%install
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} \
	DEFAULT_LOADER='\\\\grub%{efiarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
cd ..

%files
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimdir}
%{shimdir}/*.efi
%{shimdir}/*.hash

%files debuginfo -f build-%{efiarch}/debugfiles.list

%files debugsource -f build-%{efiarch}/debugsource.list

%changelog
* Tue May 26 2020 Javier Martinez Canillas <javierm@redhat.com> - 15-6
- Fix a shim crash when attempting to netboot
  Resolves: rhbz#1840036

* Mon May 04 2020 Javier Martinez Canillas <javierm@redhat.com> - 15-5
- Fix firmware update bug in aarch64 caused by shim ignoring arguments
  Resolves: rhbz#1817882

* Fri Jun 07 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-4
- Add a gating.yaml file so the package can be properly gated
  Related: rhbz#1682749

* Wed Jun 05 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-3
- Make EFI variable copying fatal only on secureboot enabled systems
  Resolves: rhbz#1704854
- Fix booting shim from an EFI shell using a relative path
  Resolves: rhbz#1717063

* Tue Feb 12 2019 Peter Jones <pjones@redhat.com> - 15-2
- Fix MoK mirroring issue which breaks kdump without intervention
  Related: rhbz#1668966

* Thu Apr 05 2018 Peter Jones <pjones@redhat.com> - 15-1
- Update to shim 15
- better checking for bad linker output
- flicker-free console if there's no error output
- improved http boot support
- better protocol re-installation
- dhcp proxy support
- tpm measurement even when verification is disabled
- REQUIRE_TPM build flag
- more reproducable builds
- measurement of everything verified through shim_verify()
- coverity and scan-build checker make targets
- misc cleanups

* Tue Sep 19 2017 Peter Jones <pjones@redhat.com> - 13-3
- Actually update to the *real* 13 final.
  Related: rhbz#1489604

* Thu Aug 31 2017 Peter Jones <pjones@redhat.com> - 13-2
- Actually update to 13 final.

* Mon Aug 21 2017 Peter Jones <pjones@redhat.com> - 13-0.1
- Update to shim-13 test release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Peter Jones <pjones@redhat.com> - - 0.9-1
- Initial split up of -aarch64
