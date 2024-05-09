Name:           lorax-templates-rhel
Version:        9.0
Release:        39%{?dist}
Summary:        RHEL8 build templates for lorax and livemedia-creator

License:        GPLv2+
URL:            https://github.com/weldr/lorax
BuildArch:      noarch
Source0:        lorax-templates-rhel-9.0-39.tar.gz

# Required for the template branding support
Requires:       lorax >= 34.9.1

# Where are these supposed to end up?
%define templatedir %{_datadir}/lorax/templates.d/80-rhel

%description
RHEL-specific Lorax templates for creating the boot.iso and live isos are
placed in %{templatedir}

%prep
%setup

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{templatedir}
cp -a 80-rhel/* $RPM_BUILD_ROOT/%{templatedir}

%files
%dir %{templatedir}
%{templatedir}/*

%changelog
* Tue Feb 06 2024 Brian C. Lane <bcl@redhat.com> - 9.0-39
- templates: Remove libreport bugzilla plugins (bcl)
  Resolves: RHEL-24421

* Fri Nov 03 2023 Brian C. Lane <bcl@redhat.com> - 9.0-38
- tools: Add support for Jira RHEL-XXX issues (bcl)
  Related: RHEL-15122
- Add setpriv as ostree containers dependency (bcl)
  Resolves: RHEL-15122

* Wed Jan 11 2023 Brian C. Lane <bcl@redhat.com> - 9.0-37
- rsyslog.conf: Set WorkDirectory to /var/lib/rsyslog (bcl)
  Resolves: rhbz#2160070

* Mon Nov 28 2022 Brian C. Lane <bcl@redhat.com> - 9.0-36
- On ppc64le Use core.elf from grub2 package (bcl)
  Resolves: rhbz#2143422

* Tue Apr 05 2022 Brian C. Lane <bcl@redhat.com> - 9.0-35
- Makefile: Making it easier to create releases (bcl)
  Related: rhbz#2071074
- runtime-postinstall: Remove machine specific nvme files (bcl)
  Resolves: rhbz#2071074

* Thu Feb 24 2022 Brian C. Lane <bcl@redhat.com> - 9.0-34
- Restore missing packages (bcl)
  Resolves: rhbz#2056086

* Fri Feb 04 2022 Brian C. Lane <bcl@redhat.com> - 9.0-33
- Keep nvram kernel module (bcl)
  Resolves: rhbz#2050878

* Tue Jan 25 2022 Brian C. Lane <bcl@redhat.com> - 9.0-32
- Fix missing generic.ins on s390x (bcl)
  Resolves: rhbz#2044448

* Thu Jan 13 2022 Brian C. Lane <bcl@redhat.com> - 9.0-31
- Do not install rng-tools (bcl)
  Resolves: rhbz#2028720
- Revert "Add inst.rngd cmdline option" (bcl)
  Related: rhbz#2028720

* Wed Jan 12 2022 Brian C. Lane <bcl@redhat.com> - 9.0-30
- Add .discinfo on all arches (bcl)
  Resolves: rhbz#2030008
- Add inst.rngd cmdline option (bcl)
  Resolves: rhbz#2028720

* Tue Jan 11 2022 Brian C. Lane <bcl@redhat.com> - 9.0-29
- Drop ia32 uefi package installation (bcl)
  Resolves: rhbz#2038397
- Enable sftp when using inst.sshd (bcl)
  Resolves: rhbz#2035049

* Mon Nov 01 2021 Brian C. Lane <bcl@redhat.com> - 9.0-28
- Drop ppc 32 bit support from grub template for live iso (bcl)
  Resolves: rhbz#2017175

* Wed Oct 27 2021 Brian C. Lane <bcl@redhat.com> - 9.0-27
- Switch to using xorrisofs instead of mkisofs (bcl)
  Resolves: rhbz#2017134

* Thu Oct 21 2021 Brian C. Lane <bcl@redhat.com> - 9.0-26
- templates: Change nomodeset / basic graphics to use inst.text (bcl)
  Resolves: rhbz#1961092
- templates: Drop nomodeset / basic graphics menu from live configs (bcl)
  Related: rhbz#1961092

* Wed Oct 06 2021 Brian C. Lane <bcl@redhat.com> - 9.0-25
- runtime-cleanup: Remove dropped packages from template (bcl)
  Resolves: rhbz#1991006
- Install nvme-cli tool (bcl)
  Resolves: rhbz#2010254
- sshd_config: Update sshd options (bcl)
  Resolves: rhbz#2007288

* Thu Sep 09 2021 Brian C. Lane <bcl@redhat.com> - 9.0-24
- Install unicode.pf2 from new directory
  Related: rhbz#2003030

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 9.0-23
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 22 2021 Brian C. Lane <bcl@redhat.com> - 9.0-22
- runtime-postinstall: Move configuration of NM default autoconnections to Anaconda (rvykydal)
  Related: rhbz#1978264

* Mon Jul 19 2021 Brian C. Lane <bcl@redhat.com> - 9.0-21
- runtime-install: Include Xorg and tigervnc on s390x for local GUI installation on KVM
  Resolves: rhbz#1983688

* Wed Jun 23 2021 Brian C. Lane <bcl@redhat.com> - 9.0-20
- runtime-install: Remove gfs2-utils (bcl)
  Resolves: rhbz#1975378

* Wed May 19 2021 Brian C. Lane <bcl@redhat.com> - 9.0-19
- Replace metacity with gnome-kiosk (bcl)
  Resolves: rhbz#1961099

* Wed May 12 2021 Brian C. Lane <bcl@redhat.com> - 9.0-18
- runtime-cleanup: branding.logos includes the full package name (bcl)
  Resolves: rhbz#1956205

* Mon May 10 2021 Brian C. Lane <bcl@redhat.com> - 9.0-17
- runtime-install: Install ipcalc (bcl)
  Resolves: rhbz#1959130
- runtime-install: Install prefixdevname (bcl)
  Resolves: rhbz#1958173

* Fri May 07 2021 Brian C. Lane <bcl@redhat.com> - 9.0-16
- Fix required lorax version for branding change (bcl)
  Related: rhbz#1956205

* Wed May 05 2021 Brian C. Lane <bcl@redhat.com> - 9.0-15
- runtime-cleanup: Use branding package name instead of product.name (bcl)
  Resolves: rhbz#1956205
- tests: Update gating test iso name to rhel 9 (bcl)
- runtime-cleanup: Remove dump from cleanup (bcl)
  Related: rhbz#1931762

* Mon May 03 2021 Brian C. Lane <bcl@redhat.com> - 9.0-14
- runtime-cleanup: Remove mcpp and libmcpp cleanup (bcl)
  Resolves: rhbz#1955429
- Revert "Remove spice-vdagent" (bcl)
  Resolves: rhbz#1945898

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 9.0-13
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Apr 05 2021 Josh Boyer <jwboyer@redhat.com> - 9.0-12
- Remove spice-vdagent
  Resovles: rhbz#1945898

* Thu Mar 04 2021 Brian C. Lane <bcl@redhat.com> - 9.0-11
- dump has been removed
  Resolves: rhbz#1931762

* Tue Feb 16 2021 Brian C. Lane <bcl@redhat.com> - 9.0-10
- Use inst.rescue to trigger rescue mode (awilliam)
- Use image dependencies metapackage (vslavik)

* Tue Feb 02 2021 Brian C. Lane <bcl@redhat.com> - 9.0-9
- runtime-install: Remove system-storage-manager
  Resolves: rhbz#1924154

* Tue Dec 08 2020 Brian C. Lane <bcl@redhat.com> - 9.0-8
- Remove unsupported filesystem tools (bcl)

* Thu Dec 03 2020 Brian C. Lane <bcl@redhat.com> - 9.0-7
- Switch to using upstream mk-s390image for s390 cdboot.img creation
  Resolves: rhbz#1903923

* Tue Dec 01 2020 Brian C. Lane <bcl@redhat.com> - 9.0-6
- Don't remove libldap_r libraries during runtime-cleanup.tmpl

* Thu Oct 29 2020 Brian C. Lane <bcl@redhat.com> - 9.0-5
- Install device-mapper-multipath (bcl)
  Work around problem with libblockdev-mpath Recommends not working

* Thu Oct 29 2020 Jan Kaluza <jkaluza@redhat.com> - 9.0-4
- Add spice-vdagentd conf back - anaconda still needs it.

* Thu Oct 29 2020 Jan Kaluza <jkaluza@redhat.com> - 9.0-3
- Add spice-vdagent back - anaconda still needs it.

* Wed Oct 28 2020 Stephen Gallagher <sgallagh@redhat.com> - 9.0-2
- Replace ppc64le template with upstream version

* Tue Oct 27 2020 Brian C. Lane <bcl@redhat.com> - 9.0-1
- Update release version for RHEL 9.0
- Remove spice-vdagent (bcl)
- Initial RHEL 9 Alpha changes (bcl)

* Tue Jul 07 2020 Brian C. Lane <bcl@redhat.com> - 8.3-4
- rsyslog: Disable journal ratelimits during install
  Related: rhbz#1752754

* Thu Jun 25 2020 Brian C. Lane <bcl@redhat.com> - 8.3-3
- include generic.ins for s390 boot iso (dan)
  Resolves: rhbz#1844517

* Wed Jun 03 2020 Brian C. Lane <bcl@redhat.com> - 8.3-2
- Keep /etc/default/useradd in install.img
  Resolves: rhbz#1843609

* Wed May 13 2020 Brian C. Lane <bcl@redhat.com> - 8.3-1
- Use smarter multipath detection logic
  Resolves: rhbz#1763906

* Thu Feb 27 2020 Brian C. Lane <bcl@redhat.com> - 8.2-6
- Restore the 98dracut-systemd service files to the install.img (bcl)
  Related: rhbz#1805405
- Add eject back into the boot.iso (bcl)
  Resolves: rhbz#1805405

* Fri Jan 10 2020 Brian C. Lane <bcl@redhat.com> - 8.2-5
- Install rdma-core and libmlx4 packages
  Resolves: rhbz#1762662

* Wed Dec 11 2019 Brian C. Lane <bcl@redhat.com> - 8.2-4
- Use mkisofs for the s390 live-iso template
  Resolves: rhbz#1746424

* Tue Nov 12 2019 Brian C. Lane <bcl@redhat.com> - 8.2-3
- Add dmidecode on supported architectures
  Resolves: rhbz#1714793

* Fri Nov 08 2019 Brian C. Lane <bcl@redhat.com> - 8.2-2
- Update ppc64le isolabel to match x86_64 logic (bcl)
  Resolves: rhbz#1757338
- set inst.stage2 for ppc64le image (bcl)
  Resolves: rhbz#1757338

* Thu Oct 31 2019 Brian C. Lane <bcl@redhat.com> - 8.2-1
- Update package version for 8.2 release
- Drop unneeded uboot-tools, and remove iso-graft from the aarch64.tmpl
  Resolves: rhbz#1763922
- Add live iso support to s390
  Resolves: rhbz#1746424

* Tue Sep 03 2019 Brian C. Lane <bcl@redhat.com> - 8.1-3
- Fix path to generic.prm (bcl)
  Resolves: rhbz#1746424

* Wed May 15 2019 Brian C. Lane <bcl@redhat.com> - 8.1-2
- Install redhat-release-eula package (bcl)
  Related: rhbz#1700465
- Don't remove chmem and lsmem from install.img (bcl)
  Resolves: rhbz#1691472
- Include the hid-multitouch kernel module (bcl)
  Resolves: rhbz#1670182
- Add extra boot args to the livemedia-creator iso templates (bcl)
  Resolves: rhbz#1694180
- Add a ppc64le template for live iso creation (bcl)
  Related: rhbz#1694180
- Add live-install.tmpl (bcl)
  Related: rhbz#1694180

* Wed Mar 27 2019 Brian C. Lane <bcl@redhat.com> - 8.1-1
- Update package version for 8.1 release
- Make sure lscpu is installed
  Resolves: rhbz#1684735

* Wed Sep 19 2018 Brian C. Lane <bcl@redhat.com> - 8.0-19
- Include python3-pyatspi on boot.iso (bcl)
  Resolves: rhbz#1543290

* Wed Sep 12 2018 Brian C. Lane <bcl@redhat.com> - 8.0-18
- re-add temporarily removed packages (bcl)
  Related: rhbz#1622395
- Use google-noto-sans-cjk-ttc-fonts (bcl)
  Resolves: rhbz#1626368

* Fri Sep 07 2018 Brian C. Lane <bcl@redhat.com> - 8.0-17
- Install the oscap-anaconda-addon
  Resolves: rhbz#1626459

* Wed Aug 22 2018 Brian C. Lane <bcl@redhat.com> - 8.0-16
- Install libreport-rhel-anaconda-bugzilla
  Related: rhbz#1593734

* Mon Aug 20 2018 Brian C. Lane <bcl@redhat.com> - 8.0-15
- import-state.service from initscripts is needed by Anaconda
  Resolves: rhbz#1618668

* Mon Aug 20 2018 Josh Boyer <jwboyer@redhat.com> - 8.0-14
- Remove fbset from runtime-install
  Resolves: rhbz#1615430

* Wed Aug 15 2018 Brian C. Lane <bcl@redhat.com> - 8.0-13
- Add prefixdevname package
  Resolves: rhbz#1615991

* Thu Aug 02 2018 Troy Dawson <tdawson@redhat.com> - 8.0-12
- Drop dependency on bridge-utils Resolves: #1588705

* Thu Jul 26 2018 Troy Dawson <tdawson@redhat.com> - 8.0-11
- Expand variables and wildcards in runtime-install.tmpl
- Cleanup the sections and packages not in RHEL8.

* Wed Jul 25 2018 Andrew Hills <ahills@redhat.com> - 8.0-10
- Drop btrfs-progs from installpkgs (RCM-38058)

* Fri Jul 20 2018 Brian C. Lane <bcl@redhat.com> - 8.0-8
- Don't activate default auto connections after switchroot
  Resolves: rhbz#1555934

* Mon Jul 09 2018 Brian C. Lane <bcl@redhat.com> - 8.0-7
- Add hostname to the rootfs for iscsi
  Resolves: rhbz#1599183

* Thu Jun 21 2018 Ian McLeod <imcleod@redhat.com> - 8.0-6
- Temporarily disable dracut-fips to allow building images in VMs

* Wed Jun 20 2018 David Cantrell <dcantrell@redhat.com> - 8.0-5
- Make sure perl-interpreter is installed

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-4
- Comment where RHEL8 removals have taken place
- Temporarily remove X server and drivers from all architectures

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-3
- Properly update build environment to pull these changes in

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-2
- Remove several _more_ packages from installer - same reason as below

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-1
- Remove several packages from installer based on current state of BaseOS/AppStream

* Mon Jun 18 2018 Will Woods <wwoods@redhat.com> - 8.0-0
- Initial creation of lorax-templates-rhel package
