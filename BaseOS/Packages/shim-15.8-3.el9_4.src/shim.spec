Name:		shim
Version:	15.8
Release:	3%{?dist}
Summary:	First-stage UEFI bootloader
License:	BSD
URL:		https://github.com/rhboot/shim/
BuildRequires:	efi-filesystem
BuildRequires:	efi-srpm-macros >= 6

ExclusiveArch:	%{efi}
# and we don't have shim-unsigned-arm builds *yet*
ExcludeArch:	%{arm} %{ix86}

Source0:	shim.rpmmacros
Source1:	redhatsecureboot501.cer
Source2:	redhatsecurebootca5.cer

# keep these two lists of sources synched up arch-wise.  That is 0 and 10
# match, 1 and 11 match, ...
Source10:	BOOTAA64.CSV
Source20:	shimaa64.efi
Source30:	mmaa64.efi
Source40:	fbaa64.efi
Source12:	BOOTX64.CSV
Source22:	shimx64.efi
Source32:	mmx64.efi
Source42:	fbx64.efi
#Source13:	BOOTARM.CSV
#Source23:	shimarm.efi
#Source33:	mmarm.efi
#Source43:	fbarm.efi

%include %{SOURCE0}

BuildRequires:	pesign >= 0.112-20.fc27
# Right now we're just including all of the parts from them as sources here
# to make the build+errata process less maddening.  We do this because
# %%{efi} won't expand before choosing where to make the src.rpm in koji,
# and we could be on a non-efi architecture, in which case we won't have a
# valid expansion here...
#%% ifarch x86_64
#BuildRequires:	%% {unsignedx64} = %% {shimverx64}
#%% endif
#%% ifarch aarch64
#BuildRequires:	%% {unsignedaa64} = %% {shimveraa64}
#%% endif
#%%ifarch arm
#BuildRequires:	%%{unsignedarm} = %%{shimverarm}
#%%endif

%description
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments. This package contains the version signed by
the UEFI signing service.

%define_pkg -a %{efi_arch} -p 1
%if %{efi_has_alt_arch}
%define_pkg -a %{efi_alt_arch}
%endif

%prep
cd %{_builddir}
rm -rf shim-%{version}
mkdir shim-%{version}

%build
export PS4='${LINENO}: '

cd shim-%{version}
%if %{efi_has_alt_arch}
%define_build -a %{efi_alt_arch} -A %{efi_alt_arch_upper} -i %{shimefialt} -b yes -c %{is_alt_signed} -d %{shimdiralt}
%endif
# Temporarily using _sourcedir to avoid build dep annoyances.
%define_build -a %{efi_arch} -A %{efi_arch_upper} -i %{shimefi} -b yes -c %{is_signed} -d %{_sourcedir}

%install
rm -rf $RPM_BUILD_ROOT
cd shim-%{version}
install -D -d -m 0755 $RPM_BUILD_ROOT/boot/
install -D -d -m 0700 $RPM_BUILD_ROOT%{efi_esp_root}/
install -D -d -m 0700 $RPM_BUILD_ROOT%{efi_esp_efi}/
install -D -d -m 0700 $RPM_BUILD_ROOT%{efi_esp_dir}/
install -D -d -m 0700 $RPM_BUILD_ROOT%{efi_esp_boot}/

%do_install -a %{efi_arch} -A %{efi_arch_upper} -b %{bootcsv}
%if %{efi_has_alt_arch}
%do_install -a %{efi_alt_arch} -A %{efi_alt_arch_upper} -b %{bootcsvalt}
%endif

%if %{provide_legacy_shim}
install -m 0700 %{shimefi} $RPM_BUILD_ROOT%{efi_esp_dir}/shim.efi
%endif

( cd $RPM_BUILD_ROOT ; find .%{efi_esp_root} -type f ) \
  | sed -e 's/\./\^/' -e 's,^\\\./,.*/,' -e 's,$,$,' > %{__brp_mangle_shebangs_exclude_from_file}

%define_files -a %{efi_arch} -A %{efi_arch_upper}
%if %{efi_has_alt_arch}
%define_files -a %{efi_alt_arch} -A %{efi_alt_arch_upper}
%endif

%if %{provide_legacy_shim}
%verify(not mtime) %{efi_esp_dir}/shim.efi
%endif

%changelog
* Wed Apr 03 2024 Peter Jones <pjones@redhat.com> - 15.8-3.el9
- Fix rpm verification due to mtime granularity on FAT.
  Related: RHEL-11262

* Thu Mar 21 2024 Peter Jones <pjones@redhat.com> - 15.8-2.el9
- Add the grub2-efi-ARCH conflict for SBAT.
  Resolves: RHEL-11262

* Thu Mar 21 2024 Peter Jones <pjones@redhat.com> - 15.8-1.el9
- Update to shim-15.8 for CVE-2023-40547
  Resolves: RHEL-11262

* Thu Apr 14 2022 Peter Jones <pjones@redhat.com> - 15.5-2.el9
- Attempt to make aarch64 build.
  Related: rhbz#1932057

* Thu Apr 14 2022 Peter Jones <pjones@redhat.com> - 15.5-1.el9
- Rebuild for rhel-9.0.0
  Resolves: rhbz#1932057

* Mon Sep 21 2020 Javier Martinez Canillas <javierm@redhat.com> - 15-16
- Fix an incorrect allocation size

* Fri Jul 31 2020 Peter Jones <pjones@redhat.com> - 15-15
- Update once again for new signed shim builds.

* Tue Jul 28 2020 Peter Jones <pjones@redhat.com> - 15-14
- Get rid of our %%dist hack for now.

* Tue Jul 28 2020 Peter Jones <pjones@redhat.com> - 15-13
- New signing keys

* Thu Jun 11 2020 Javier Martinez Canillas <javierm@redhat.com> - 15-12
- Fix firmware update bug in aarch64 caused by shim ignoring arguments
- Fix a shim crash when attempting to netboot

* Fri Jun 07 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-11
- Update the shim-unsigned-aarch64 version number

* Fri Jun 07 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-10
- Add a gating.yaml file so the package can be properly gated

* Wed Jun 05 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-9
- Bump the NVR

* Wed Jun 05 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-7
- Make EFI variable copying fatal only on secureboot enabled systems
- Fix booting shim from an EFI shell using a relative path

* Thu Mar 14 2019 Peter Jones <pjones@redhat.com> - 15-6
- Fix MoK mirroring issue which breaks kdump without intervention

* Thu Jan 24 2019 Peter Jones <pjones@redhat.com> - 15-5
- Rebuild for signing once again. If the signer actually works, then:

* Tue Oct 16 2018 Peter Jones <pjones@redhat.com> - 15-4
- Rebuild for signing

* Mon Aug 13 2018 Troy Dawson <tdawson@redhat.com>
- Release Bumped for el8 Mass Rebuild

* Sat Aug 11 2018 Troy Dawson <tdawson@redhat.com>
- Release Bumped for el8+8 Mass Rebuild

* Mon Jul 23 2018 Peter Jones <pjones@redhat.com> - 15-1
- Build for RHEL 8
