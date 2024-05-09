%define debug_package %{nil}
%define product_family Red Hat Enterprise Linux
%define release_name Plow
%define base_release_version 9
%define full_release_version 9.4
%define dist_release_version 9

# When moving from Beta to GA, the beta definition needs to be removed,
# not just commented out.
# Also ensure that the appropriate SWID and productids tarball have been
# uploaded to the lookaside cache.
%define beta_part %{?beta:-%{beta}}
%define swid_regid redhat.com
%define dist .el%{dist_release_version}

Name:           redhat-release
Version:        %{full_release_version}
Release:        0.4%{?dist}
Summary:        %{product_family} release file
Group:          System Environment/Base
License:        GPLv2
Provides:       redhat-release = %{version}-%{release}
Provides:       system-release = %{version}-%{release}
Provides:       system-release(releasever) = %{base_release_version}
Provides:       base-module(platform:el%{base_release_version})
Provides:       redhat-release-server
Provides:       redhat-release-client
Provides:       redhat-release-computenode
Provides:       redhat-release-workstation
Obsoletes:      redhat-release-server
Obsoletes:      redhat-release-client
Obsoletes:      redhat-release-computenode
Obsoletes:      redhat-release-workstation
Recommends:     redhat-release-eula
Source0:        redhat-release-%{base_release_version}.0.tar.gz
Source1:        85-display-manager.preset
Source2:        90-default.preset
Source3:        99-default-disable.preset
Source4:        redhat-release-productids-9.4-dist-20240326104541.tar.gz
Source5:        RHEL-%{full_release_version}%{?beta_part}-swidtag.tar.gz
Source6:        50-redhat.conf
Source7:        90-default-user.preset

# Secure Boot Signing Certificates
Source400:      sb-certs-9-2023.8.tar.bz2


%description
%{product_family} release files


%package -n redhat-sb-certs
Summary: %{distro} public secureboot certificates
Group: System Environment/Base
Provides: system-sb-certs = %{version}-%{release}
BuildArch: noarch


%description -n redhat-sb-certs
Secure Boot certificates


%package eula
Summary:        %{product_family} EULA file
Group:          System Environment/Base
%description eula
%{product_family} EULA file

%prep
%setup -q -n redhat-release-%{base_release_version}
%setup -q -n redhat-release-%{base_release_version} -T -D -a 4
%setup -q -n redhat-release-%{base_release_version} -T -D -a 5
%setup -q -n redhat-release-%{base_release_version} -T -D -a 400


%build
echo OK


%install
rm -rf %{buildroot}

# create /etc
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/%{_prefix}/lib

# create /etc/system-release and /etc/redhat-release
echo "%{product_family} release %{full_release_version}%{?beta: %{beta}} (%{release_name})" > %{buildroot}/etc/redhat-release
ln -s redhat-release %{buildroot}/etc/system-release

# -------------------------------------------------------------------------
# Definitions for /etc/os-release and for macros in macros.dist.  These
# macros are useful for spec files where distribution-specific identifiers
# are used to customize packages.

# Name of vendor / name of distribution. Typically used to identify where
# the binary comes from in --help or --version messages of programs.
# Examples: gdb.spec, clang.spec
%global dist_vendor Red Hat, Inc.
%global dist_name   %{product_family}

# URL of the homepage of the distribution
# Example: gstreamer1-plugins-base.spec
%global dist_home_url https://www.redhat.com/

# Bugzilla / bug reporting URLs shown to users.
# Examples: gcc.spec
%global dist_bug_report_url https://bugzilla.redhat.com/

# debuginfod server, as used in elfutils.spec. Not currently available for RHEL
# %global dist_debuginfod_url %{nil}
# -------------------------------------------------------------------------

# create /usr/lib/os-release
cat << EOF >>%{buildroot}/%{_prefix}/lib/os-release
NAME="%{dist_name}"
VERSION="%{full_release_version} (%{release_name})"
ID="rhel"
ID_LIKE="fedora"
VERSION_ID="%{full_release_version}"
PLATFORM_ID="platform:el%{base_release_version}"
PRETTY_NAME="%{product_family} %{full_release_version}%{?beta: %{beta}} (%{release_name})"
ANSI_COLOR="0;31"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:redhat:enterprise_linux:%{base_release_version}::baseos"
HOME_URL="%{dist_home_url}"
DOCUMENTATION_URL="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/%{base_release_version}"
BUG_REPORT_URL="%{dist_bug_report_url}"

REDHAT_BUGZILLA_PRODUCT="%{product_family} %{base_release_version}"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{full_release_version}
REDHAT_SUPPORT_PRODUCT="%{product_family}"
REDHAT_SUPPORT_PRODUCT_VERSION="%{full_release_version}%{?beta: %{beta}}"
EOF
# create /etc/os-release symlink
ln -s ..%{_prefix}/lib/os-release %{buildroot}/%{_sysconfdir}/os-release

# write cpe to /etc/system/release-cpe
echo "cpe:/o:redhat:enterprise_linux:%{base_release_version}::baseos" | tr [A-Z] [a-z] > %{buildroot}/etc/system-release-cpe

# create /etc/issue, /etc/issue.net and /etc/issue.d
echo '\S' > %{buildroot}/etc/issue
echo 'Kernel \r on an \m' >> %{buildroot}/etc/issue
cp %{buildroot}/etc/issue %{buildroot}/etc/issue.net
echo >> %{buildroot}/etc/issue
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

mkdir -p -m 755 %{buildroot}/etc/pki/rpm-gpg
# Correct GPG keys were fixed in via rhbz#1672230
cp RPM-GPG-KEY-redhat-release %{buildroot}/etc/pki/rpm-gpg/
cp RPM-GPG-KEY-redhat-beta %{buildroot}/etc/pki/rpm-gpg/
cp ISV-Container-signing-key %{buildroot}/etc/pki/rpm-gpg/
chmod 0644 %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-*
chmod 0644 %{buildroot}/etc/pki/rpm-gpg/ISV-Container-signing-key

# Copy Productids
mkdir -p -m 755 %{buildroot}/etc/pki/product-default
if [ -d redhat-release-productids-%{full_release_version}-*/%{_arch} ]; then
    for pem in redhat-release-productids-%{full_release_version}-*/%{_arch}/*.pem; do
        install -m 644 $pem %{buildroot}/etc/pki/product-default
    done
fi

## set up the dist tag macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.dist << EOF
# dist macros.

%%rhel %{base_release_version}
%%__bootstrap         ~bootstrap
%%dist %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%{dist}%%{?distsuffix}%%{?with_bootstrap:%{__bootstrap}}
%%el%{base_release_version} 1
%%dist_vendor         %{dist_vendor}
%%dist_name           %{dist_name}
%%dist_home_url       %{dist_home_url}
%%dist_bug_report_url %{dist_bug_report_url}
EOF
### dist tag macros end

# make redhat-release a protected package
install -p -d -m 755 %{buildroot}/etc/dnf/protected.d/
touch redhat-release.conf
echo redhat-release > redhat-release.conf
install -p -c -m 0644 redhat-release.conf %{buildroot}/etc/dnf/protected.d/
rm -f redhat-release.conf

# use unbranded datadir
mkdir -p -m 755 %{buildroot}/%{_datadir}/redhat-release
install -m 644 EULA %{buildroot}/%{_datadir}/redhat-release

# use unbranded docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/redhat-release
install -m 644 GPL %{buildroot}/%{_docdir}/redhat-release
sed  -i 's:@@VERSION@@:%{full_release_version}:' GPL-source-offer
install -m 644 GPL-source-offer %{buildroot}/%{_docdir}/redhat-release

# copy systemd presets
mkdir -p %{buildroot}/%{_prefix}/lib/systemd/system-preset/
mkdir -p %{buildroot}/%{_prefix}/lib/systemd/user-preset
install -m 0644 %{SOURCE1} %{buildroot}/%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE2} %{buildroot}/%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE3} %{buildroot}/%{_prefix}/lib/systemd/system-preset/

install -m 0644 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/user-preset/
install -m 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/user-preset/

# copy sysctl presets
mkdir -p %{buildroot}/%{_prefix}/lib/sysctl.d/
install -m 0644 %{SOURCE6} %{buildroot}/%{_prefix}/lib/sysctl.d/

mkdir -p -m 755 %{buildroot}/etc/yum.repos.d

# Copy SWID tags
mkdir -p -m 755 %{buildroot}%{_prefix}/lib/swidtag/%{swid_regid}
if ! [ %{_arch} = "i386" ] ; then
    install -p -m 644 RHEL-%{full_release_version}%{?beta_part}-swidtag/com.redhat.RHEL-%{base_release_version}-%{_arch}.swidtag %{buildroot}%{_prefix}/lib/swidtag/%{swid_regid}/
    install -p -m 644 RHEL-%{full_release_version}%{?beta_part}-swidtag/com.redhat.RHEL-%{full_release_version}%{?beta_part}-%{_arch}.swidtag %{buildroot}%{_prefix}/lib/swidtag/%{swid_regid}/
fi
mkdir -p -m 755 %{buildroot}/etc/pki/swid/CA/%{swid_regid}
mkdir -p -m 755 %{buildroot}/etc/swid/swidtags.d
ln -sr %{buildroot}%{_prefix}/lib/swidtag/%{swid_regid} %{buildroot}/etc/swid/swidtags.d/%{swid_regid}
install -p -m 644 RHEL-%{full_release_version}%{?beta_part}-swidtag/redhatcodesignca.cert %{buildroot}/etc/pki/swid/CA/%{swid_regid}/


# Copy secureboot certificates
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/sb-certs/
install -d -m 0755 %{buildroot}%{_datadir}/pki/sb-certs/

# Install aarch64 certs
install -m 644 sb-certs/redhatsecurebootca5.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-aarch64.cer

install -m 644 sb-certs/redhatsecureboot501.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-aarch64.cer

install -m 644 sb-certs/redhatsecureboot502.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-aarch64.cer

install -m 644 sb-certs/redhatsecureboot503.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-fwupd-aarch64.cer

install -m 644 sb-certs/redhatsecureboot504.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer

# Install ppc64le certs
install -m 644 sb-certs/redhatsecurebootca7.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-ppc64le.cer

install -m 644 sb-certs/redhatsecureboot701.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-ppc64le.cer

install -m 644 sb-certs/redhatsecureboot701.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-ppc64le.cer

install -m 644 sb-certs/redhatsecureboot704.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer

# Install s390x certs
install -m 644 sb-certs/redhatsecurebootca3.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-s390x.cer

install -m 644 sb-certs/redhatsecureboot302.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-s390x.cer

install -m 644 sb-certs/redhatsecureboot304.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-s390x.cer

# Install x86_64 certs
install -m 644 sb-certs/redhatsecurebootca5.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-x86_64.cer

install -m 644 sb-certs/redhatsecureboot501.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-x86_64.cer

install -m 644 sb-certs/redhatsecureboot502.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-x86_64.cer

install -m 644 sb-certs/redhatsecureboot503.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-fwupd-x86_64.cer

install -m 644 sb-certs/redhatsecureboot504.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer

%clean
rm -rf %{buildroot}


%files
%defattr(0644,root,root,0755)
/etc/redhat-release
/etc/system-release
%config /etc/os-release
%config /etc/system-release-cpe
%config(noreplace) /etc/issue
%config(noreplace) /etc/issue.net
%dir %{_sysconfdir}/issue.d
/etc/dnf/protected.d/redhat-release.conf
/etc/pki/rpm-gpg/
%{_rpmmacrodir}/macros.dist
%{_docdir}/redhat-release/*
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/*
%{_prefix}/lib/sysctl.d/50-redhat.conf
%{_prefix}/lib/os-release
/etc/pki/product-default
%dir /etc/yum.repos.d
/etc/swid/swidtags.d
%{_prefix}/lib/swidtag/%{swid_regid}
/etc/pki/swid/CA/%{swid_regid}


%files eula
%defattr(0644,root,root,0755)
%{_datadir}/redhat-release/EULA


%files -n redhat-sb-certs
# Note to future packagers:
# The symlinks are not %config(noreplace) intentionally. We want them to be
# restored if this package is updated.
%dir %{_sysconfdir}/pki/sb-certs
%dir %{_datadir}/pki/sb-certs
%{_sysconfdir}/pki/sb-certs/*.cer
%{_datadir}/pki/sb-certs/*.cer


%changelog
* Fri Apr 05 2024 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.4
- Bump the version
- Resolves: RHELBLD-14813

* Fri Apr 05 2024 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.3
- Change version to 9.4-0, because of errata_automation failed
- Resolves: RHELBLD-14813
 
* Fri Apr 05 2024 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-1.2
- Add ISV container signing key
- Resolves: RHELBLD-14813

* Tue Mar 26 2024 Aviv Sabadra <asabadra@redhat.com> - 9.4-1.1
- Bump release
- Resolves: RHELBLD-14195

* Tue Mar 26 2024 Aviv Sabadra <asabadra@redhat.com> - 9.4-1.0
- Add RHEL-9.4 GA Product ID certs
- Resolves: RHELBLD-14195

* Thu Mar 05 2024 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.3
- Enable kernel-bootcfg-boot-successful.service 
- Resolves: RHEL-21816 

* Fri Jan 19 2024 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.2
- Improve virt presets
- Resolves: RHEL-14704

* Mon Aug 21 2023 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.1
- Add newly created secureboot certs
- Resolves: rhbz#2225009

* Thu Jul 20 2023 Veronika Doubkova <vdoubkov@redhat.com> - 9.4-0.0
- Add RHEL-9.4 Beta product ID certs
- Resolves: RHELBLD-13198

* Thu Apr 06 2023 Stephen Gallagher <sgallagh@redhat.com> - 9.3-0.3
- Enable obex.service
- Resolves: rhbz#2181984

* Tue Feb 21 2023 Stephen Gallagher <sgallagh@redhat.com> - 9.3-0.2
- Remove ostree-readonly-sysroot-migration service from preset
- Resolves: RHELBLD-12180

* Tue Feb 14 2023 Stephen Gallagher <sgallagh@redhat.com> - 9.3-0.1
- Enable ostree-readonly-sysroot-migration service
- Resolves: RHELPLAN-147614

* Thu Jan 19 2023 Aviv Sabadra <asabadra@redhat.com> - 9.3-0.0
- Add RHEL-9.3 Beta product ID certs
- Resolves: RHELBLD-11465

* Mon Dec 12 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.2-0.10
- Remove redundant slash in the symlink //usr/lib/os-release
- Resolves: RHELBLD-11698

* Wed Nov 09 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.2-0.9
- Remove the "License" field for the redhat-release-eula subpackage
- Resolves: RHELBLD-11423

* Thu Oct 20 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.2-0.8
- Drop debuginfod_url definition
- Related: rhbz#2112392

* Wed Oct 19 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.2-0.7
- Change documentation URL
- Resolves: RHELBLD-11161

* Tue Oct 18 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.2-0.6
- Fix debuginfo_url definition
- Related: rhbz#2112392

* Tue Sep 20 2022 Veronika Doubkov <vdoubkov@redhat.com> - 9.2-0.5
- Updated product certificate
- Resolves: RHELBLD-10819

* Mon Sep 12 2022 Amit Shah <amitshah@fedoraproject.org> - 9.2-0.4
- Add new distribution-specific macros for package configurations

* Thu Jul 28 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.2-0.3
- Include %%{?distsuffix} in %%dist definition
- Resolves: rhbz#2100579

* Thu Jul 28 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.2-0.2
- Enable greenboot-service-monitor.service in presets
- Resolves: rhbz#2108625

* Wed Jul 27 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.2-0.1
- Enable clevis-luks-askpass.path
- Resolves: RHELBLD-10332

* Wed Jul 20 2022 Aviv Sabadra <asabadra@redhat.com> - 9.2-0.0
- Add RHEL-9.2 Beta product ID certs
- Resolves: RHELBLD-10195

* Fri Jul 08 2022 bstinson@redhat.com - 9.1-1.5
- Update ppc64le secureboot certs
- Resolves: rhbz#2104308

* Mon Jun 20 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.1-1.4
- Updated productIDs
- Resolves: RHELBLD-10117

* Wed Mar 16 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.1-1.3
- Updated redhat-release-9.0.tar.gz
- Resolves: rhbz#2060785

* Mon Mar 07 2022 Veronika Doubkova <vdoubkov@redhat.com> - 9.1-1.2
- Updated redhat-release-9.0.tar.gz
- Resolves: rhbz#2060346

* Thu Mar 03 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.1-1.1
- Sign grub2 on ppc64le properly
- Related: rhbz#1873860
- Enable switcheroo-control.service
- Resolves: rhbz#2049627

* Wed Feb 02 2022 Aviv Sabadra <asabadra@redhat.com> - 9.1-1.0
- Add RHEL-9.1 Beta product ID certs
  Resolves: RHELBLD-8723

* Thu Jan 06 2022 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.12
- Add LOGO to os-release(5) data
  Resolves: rhbz#2031998

* Thu Nov 18 2021 Timothée Ravier <tim@siosm.fr> - 9.0-2.11
- Create and own /etc/issue.d directory
- Resolves: rhbz#2024610

* Fri Nov 12 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.10
- Add preset to enable WirePlumber by default
- Resolves: rhbz#2022717

* Wed Oct 13 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.9
- Enable new service presets
- Enable preset for low-memory-monitor
  Resolves: rhbz#2013299
- Enable preset for greenboot
  Resolves: rhbz#2005552
- Enable preset for power-profiles-daemon
  Resolves: rhbz#2011240

* Tue Sep 14 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-2.8
- Fix Beta string
- Resolves: RHELBLD-7362

* Fri Sep 10 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.7
- Fix incorrect symlink introduced accidentally
- Related: rhbz#2002496

* Thu Sep 09 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.6
- Add secure boot certificates
- Resolves: rhbz#2002496

* Wed Sep 01 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.5
- Drop nfs-convert.service preset
- Related: rhbz#1937811

* Tue Aug 17 2021 Veronika Doubkova - 9.0-2.4
- Add product ID certs and SWID tags back to beta 
- Resolves: RHELBLD-7109

* Tue Aug 03 2021 Aviv Sabadra <asabadra@redhat.com> - 9.0-2.3
- Add SWID tags.
- Resolves: RHELBLD-6664

* Mon Aug 02 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.2
- Fix macros test
- Related: rhbz#1985500

* Mon Aug 02 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2.1
- Move RPM macros to /usr on behalf of Neal Gompa
- Resolves: rhbz#1985500

* Thu Jul 29 2021 Aviv Sabadra - 9.0-2.0.el9
- Add RHEL-9.0 GA product ID certs
- Resolves: RHELBLD-6663

* Tue Jul 27 2021 Veronika Doubkova - 9.0-1.8.el9
- Updated ProductIDs 
- Resolves: RHELBLD-6794

* Mon Jul 26 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-1.7.el9
- Add presets for pipewire services from Neal Gompa
- Related: rhbz#1956854

* Mon Jul 26 2021 Josh Boyer <jwboyer@redhat.com> - 9.0-1.6.el9
- Add preset for SDDM from Neal Gompa
- Resolves: RhBug 1985511
 
* Fri Jul 02 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-1.5.el9
- Enable logrotate.timer 
- Resolves: RHELBLD-6668

* Wed Apr 28 2021 Aviv Sabadra <asabadra@redhat.com> - 9.0-1.4.el9
- Added SWID tags
- Resolves: RHELBLD-1993

* Tue Apr 06 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-1.3.el9
- Modified cpe strings
- Resolves: RHELBLD-5042

* Tue Mar 23 2021 Josh Boyer <jwboyer@redhat.com> - 9.0-1.2.el9
- Add sysctl.d presets
- Resolves: RhBug 1925547

* Wed Mar 10 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-1.1.el9
- Fix typo in changelog 
- Related: RHELBLD-4843

* Wed Mar 10 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-1.0.el9
- Bump release to 1.0 and update the define beta
- Resolves: RHELBLD-4843

* Tue Mar 09 2021 Veronika Doubkova <vdoubkov@redhat.com> - 9.0-0.13.el9
- Enable iscsi service files 
- Resolves: RHELPLAN-69897

* Wed Feb 17 2021 Aviv Sabadra <asabadra@redhat.com> - 9.0-0.12.el9
- Added SHA256 signed productids
- Resolves: RHELBLD-4538

* Wed Jan 06 2021 Stephen Gallagher <sgallagh@redhat.com> - 9.0-0.11.el9
- Include %%__bootstrap macro to support golang packages

* Wed Dec 16 2020 Josh Boyer <jwboyer@redhat.com> - 9.0-0.10.el9
- Adjust PRETTY_NAME
- Start ostree-mount and mlocate-updatedb by default
- Add DOCUMENTATION_URL

* Tue Dec 15 2020 Aviv Sabadra <asabadra@redhat.com> - 9.0-0.9.el9
- Adding productids. RHELBLD-4065

* Thu Dec 10 2020 Petr Šabata <contyk@redhat.com> - 9.0-0.8.el9
- Reverting the dist tag change post-mass rebuild

* Mon Dec 07 2020 Petr Šabata <contyk@redhat.com> - 9.0-0.7.el9.1
- Bump the %%dist tag to el9.1 for the gcc11 mass rebuild

* Tue Nov 17 2020 Troy Dawson<tdawson@redhat.com> - 9.0-0.7.el9
- Add distprefix to %{dist}
- Cleanup old, unneeded comments

* Mon Nov 02 2020 Stephen Gallagher <sgallagh@redhat.com> - 9.0-0.6.el9
- Add platform definition for modules
- Add codename

* Thu Oct 29 2020 Jan Kaluza <jkaluza@redhat.com> - 9.0-0.5.el9
- Enable dbus and dbus-broker by default to fix Anaconda installer.

* Mon Oct 12 2020 Josh Boyer <jwboyer@redhat.com> - 9.0-0.4.el9
- Adjust EULA
- Resolves: rhbz#1886860

* Sun Oct 11 2020 Aviv Sabadra <asabadra@redhat.com> - 9.0-0.3.el9
- Removed tarballs from the repo
- Resolves: RHELBLD-3105

* Tue Oct 06 2020 Aviv Sabadra <asabadra@redhat.com> - 9.0-0.2.el9
- Add RHEL-9.0 Beta product ID certs
- Resolves: RHELBLD-2542

* Tue Jul 07 2020 Djordje Todorovic <dtodorov@redhat.com>
- Rebuild for RHEL-9.0 bootstrapping
