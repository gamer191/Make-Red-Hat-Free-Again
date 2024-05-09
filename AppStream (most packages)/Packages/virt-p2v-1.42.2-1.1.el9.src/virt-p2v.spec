# Verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# So far there are no ELF binaries in this package, so the list
# of files in the debuginfo package will be empty, triggering
# an RPM failure.
%global debug_package %{nil}

Summary:       Convert a physical machine to run on KVM
Name:          virt-p2v
Epoch:         1
Version:       1.42.2
Release:       1.1%{?dist}
License:       GPLv2+

# virt-p2v works only on x86_64 at the moment.  It requires porting
# to properly detect the hardware on other architectures, and furthermore
# virt-v2v requires porting too.
ExclusiveArch: x86_64

# Source and patches.
URL:           http://libguestfs.org/
Source0:       http://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz.sig
%endif

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source2:       libguestfs.keyring
%endif

# Basic build requirements.
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Man)
BuildRequires: perl(List::MoreUtils)
BuildRequires: /usr/bin/pod2text
BuildRequires: libxml2-devel
BuildRequires: pcre2-devel
BuildRequires: bash-completion
BuildRequires: xz
BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: m4
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# Test suite requirements.
BuildRequires: nbdkit

Requires:      gawk
Requires:      gzip

# virt-p2v-make-disk runs virt-builder:
Requires:      guestfs-tools

# virt-p2v-make-kickstart runs strip:
Requires:      binutils


%description
Virt-p2v converts (virtualizes) physical machines so they can be run
as virtual machines under KVM.

This package contains the tools needed to make a virt-p2v boot CD or
USB key which is booted on the physical machine to perform the
conversion.  You also need virt-v2v installed somewhere else to
complete the conversion.

To convert virtual machines from other hypervisors, see virt-v2v.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1


%build
%configure \
  --with-extra="fedora=%{fedora},release=%{release}"

%make_build


%check
if ! make check; then
    cat test-suite.log
    exit 1
fi


%install
%make_install

# Delete the development man pages.
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-building.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-hacking.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-release-notes.1*


%files
%doc README
%license COPYING
%{_bindir}/virt-p2v-make-disk
%{_bindir}/virt-p2v-make-kickstart
%{_bindir}/virt-p2v-make-kiwi
%{_datadir}/bash-completion/completions/virt-*
%{_datadir}/virt-p2v
%{_libdir}/virt-p2v
%{_mandir}/man1/virt-p2v-make-disk.1*
%{_mandir}/man1/virt-p2v-make-kickstart.1*
%{_mandir}/man1/virt-p2v-make-kiwi.1*
%{_mandir}/man1/virt-p2v.1*


%changelog
* Wed Aug 03 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.2-1.1
- New upstream release 1.42.2
- Synchronise with Fedora 37:
  * Uses PCRE2 instead of PCRE.
  * Remove Obsolete/Provides etc used for upgrades from Fedora 31.
  * libguestfs-tools-c was renamed to guestfs-tools in Fedora 34.
  * gnulib removed upstream.
  * Some specfile modernization.
- Add gating tests
  resolves: rhbz#1990052

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.42.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.42.0-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.42.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-1
- New upstream release 1.42.0.
- Use gpgverify macro instead of explicit gpgv2 command.
- Move .sig file to sources instead of dist-git.

* Tue Sep 10 2019 Pino Toscano <ptoscano@redhat.com> - 1:1.41.0-1
- Initial build, split off src:libguestfs.
