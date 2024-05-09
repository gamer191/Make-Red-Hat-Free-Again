Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	6.3.0
Release:	1%{?dist}
License:	GPL+ and LGPLv2+
URL:		https://xfs.wiki.kernel.org
Source0:	http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.xz
Source1:	http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.sign
Source2:        https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/13F703E6C11CF6F0.asc
Source3:	rhel8.0.conf
Requires:	util-linux
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool, gettext, libattr-devel, libuuid-devel
BuildRequires:	libedit-devel, libblkid-devel >= 2.17-0.1.git5e51568
Buildrequires:	lvm2-devel, libicu-devel >= 4.6
BuildRequires:	gnupg2, xz, inih-devel
BuildRequires:  userspace-rcu-devel
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Provides:	xfsprogs-qa-devel
Obsoletes:	xfsprogs-qa-devel <= %{version}
Conflicts:	xfsdump < 3.0.1
Suggests:	xfsprogs-xfs_scrub

Patch0:		xfsprogs-rhelonly-disable-old-kernel-bigtime-inobtcnt-on.patch
Patch1:		xfsprogs-rhelonly-example-conf.patch
Patch2:		xfsprogs-rhelonly-mkfs-tolerate-tiny-filesystems.patch
Patch3:		xfsprogs-rhelonly-xfs_quota-fix-missing-mount-point-warning.patch
Patch4:		xfsprogs-6.4.0-set-bnobt-cntbt-numrecs-correctly-when-formattin.patch
Patch5:		xfsprogs-6.4.0-mkfs-fix-man-s-default-value-for-sparse-option.patch
Patch6:		xfsprogs-6.4.0-xfs_repair-don-t-add-junked-entries-to-the-rebuilt-d.patch
Patch7:		xfsprogs-6.4.0-xfs_repair-fix-messaging-when-fixing-imap-due-to-spa.patch
Patch8:		xfsprogs-6.4.0-xfs_repair-don-t-spray-correcting-imap-all-by-itself.patch
Patch9:		xfsprogs-6.4.0-xfs_repair-fix-messaging-when-shortform_dir2_junk-is.patch
Patch10:	xfsprogs-6.4.0-xfs_db-move-obfuscate_name-assertion-to-callers.patch
Patch11:	xfsprogs-6.4.0-xfs_db-fix-metadump-name-obfuscation-for-ascii-ci-fi.patch
Patch12:	xfsprogs-6.5.0-mkfs.xfs.8-correction-on-mkfs.xfs-manpage-since-refl.patch
Patch13:	xfsprogs-6.4.0-xfs-stabilize-the-dirent-name-transformation-functio.patch

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

This implementation is on-disk compatible with the IRIX version
of XFS.

%package devel
Summary: XFS filesystem-specific headers
Requires: xfsprogs = %{version}-%{release}, libuuid-devel

%description devel
xfsprogs-devel contains the header files needed to develop XFS
filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%package xfs_scrub
Summary: XFS filesystem online scrubbing utilities
Requires: xfsprogs = %{version}-%{release}, python3

%description xfs_scrub
xfs_scrub attempts to check and repair all metadata in a mounted XFS filesystem.
WARNING!  This program is EXPERIMENTAL, which means that its behavior and
interface could change at any time!

%prep
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1

%build
export tagname=CC

%configure \
	--enable-editline=yes	\
	--enable-blkid=yes	\
	--enable-lto=no

%make_build

%install
make DIST_ROOT=$RPM_BUILD_ROOT install install-dev \
	PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir}

# nuke .la files, etc
rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.{la,a}}

# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

# add backward compatible configure file for mkfs
%global mkfsdir %{_datadir}/xfsprogs/mkfs
install -m 0755 -d %{buildroot}%{mkfsdir}
install -m 0644 %{SOURCE3} %{buildroot}%{mkfsdir}

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc doc/CHANGES README
%{_libdir}/*.so.*
%dir %{_usr}/%{_lib}/xfsprogs
%{_usr}/%{_lib}/xfsprogs/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/*
%{_unitdir}/*
%{mkfsdir}
%exclude %{_sbindir}/xfs_scrub*
%exclude %{_mandir}/man8/xfs_scrub*
%exclude %{_usr}/%{_lib}/xfsprogs/xfs_scrub*
%exclude %{_mandir}/man8/xfs_scrub_all*
%exclude %{_unitdir}/xfs_scrub*

%files xfs_scrub
%{_sbindir}/xfs_scrub*
%{_mandir}/man8/xfs_scrub*
%{_usr}/%{_lib}/xfsprogs/xfs_scrub*
%{_mandir}/man8/xfs_scrub_all*
%{_unitdir}/xfs_scrub*

%files devel
%{_mandir}/man2/*
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xfs_fs_compat.h
%{_includedir}/xfs/xfs_types.h
%{_includedir}/xfs/xfs_format.h
%{_includedir}/xfs/xfs_da_format.h
%{_includedir}/xfs/xfs_log_format.h
%{_includedir}/xfs/xqm.h

%{_libdir}/*.so

%changelog
* Mon Nov 13 2023 Pavel Reichl <preichl@redhat.com> - 6.3.0-1
- Rebase to upstream version 6.3.0
-
- Following is a list of dropped backported patches which
- are contained in the current rebase:
- xfsprogs-5.19.0-xfs-hoist-refcount-record-merge-predicates.patch (v6.2.0)
- xfsprogs-5.19.0-xfs_db-fix-dir3-block-magic-check.patch (v6.1.0)
- xfsprogs-5.19.0-xfs-estimate-post-merge-refcounts-correctly.patch (v6.2.0)
- xfsprogs-5.19.0-xfs-get-rid-of-assert-from-xfs_btree_islastblock.patch (v6.2.0)
- xfsprogs-5.19.0-xfs-fix-off-by-one-error-in-xfs_btree_space_to_heigh.patch (v6.2.0)
- xfsprogs-5.19.0-xfs-fix-sb-write-verify-for-lazysbcount.patch (v6.1.0)
- xfsprogs-5.19.0-xfs-removed-useless-condition-in-function-xfs_attr_n.patch (v6.0.0)
- xfsprogs-5.19.0-xfs_repair-retain-superblock-buffer-to-avoid-write-h.patch (v6.1.0)
-
- Rename the remaining patches so the name contains upstream version in which
- they are implemented, or "rhelonly".
-
- Drop Eric Sandeen's public key used to check tarball signature and replace it by
- Carlos Maiolino's (current upstream xfsprogs maintainer).
-
- Following is a list of newly backported patches from versions released after 6.3
- which are fixing patches present in version 6.3:
- xfsprogs-6.4.0-xfs_repair-don-t-add-junked-entries-to-the-rebuilt-d.patch
- xfsprogs-6.4.0-xfs_repair-don-t-spray-correcting-imap-all-by-itself.patch
- xfsprogs-6.4.0-xfs_repair-fix-messaging-when-fixing-imap-due-to-spa.patch
- xfsprogs-6.4.0-xfs_repair-fix-messaging-when-shortform_dir2_junk-is.patch
-
- Backport:
- xfsprogs-6.4.0-xfs_db-move-obfuscate_name-assertion-to-callers.patch
- xfsprogs-6.4.0-xfs_db-fix-metadump-name-obfuscation-for-ascii-ci-fi.patch
- xfsprogs-6.4.0-xfs-stabilize-the-dirent-name-transformation-functio.patch
- to implement RHEL-RHEL-8284
-
- Backport xfsprogs-rhelonly-xfs_quota-fix-missing-mount-point-warning.patch
- to implement RHEL-7900
-
- Related: RHEL-15399
- Related: RHEL-8284
- Related: RHEL-7900

* Wed Aug 02 2023 Pavel Reichl <preichl@redhat.com> - 5.19.0-4
- Fix man page, mkfs.xfs(8): Update section on dax+reflink
- compatibility (#2226900)

* Tue Jun 20 2023 Pavel Reichl <preichl@redhat.com> - 5.19.0-3
- Fix man page default for sparse mkfs option (#2216118)

* Fri May 26 2023 Pavel Reichl <preichl@redhat.com> - 5.19.0-2
- Fix xfs corrupted when AG size is a multiple of stripe width
- Related: rhbz#2192982

* Tue Jan 10 2023 Pavel Reichl <preichl@redhat.com> - 5.19.0-1
- New upstream release
- Tolerate tiny (<300MB) filesystems
- Rename xfsprogs-5.12.0-default-bigtime-inobtcnt-on.patch to
    xfsprogs-5.19.0-disable-old-kernel-bigtime-inobtcnt-on.patch
    and amend it to reflect upstream changes
- Backport all "Fixing" patches relevant to 5.19
  Related: rhbz#2142910

* Fri Jan 21 2022 Pavel Reichl <preichl@redhat.com> - 5.14.2-1
- New upstream release
  Related: rhbz#2041525

* Wed Dec 01 2021 Pavel Reichl <preichl@redhat.com> - 5.12.0-5
- Add an example of backward compatible conf. file for mkfs
  Related: rhbz#2026002

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 5.12.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 16 2021 Eric Sandeen <sandeen@redhat.com> 5.12.0-3
- Local change to default bigtime & inobtcnt to off under older kernels

* Thu Jun 03 2021 Eric Sandeen <sandeen@redhat.com> 5.12.0-2
- Turn on bigtime (y2038) and inobtcnt features by default

* Thu Jun 03 2021 Eric Sandeen <sandeen@redhat.com> 5.12.0-1
- New upstream release

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 5.10.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Eric Sandeen <sandeen@redhat.com> 5.10.0-1
- New upstream release
- New mkfs config file feature
- Y2038+ format support

* Tue Oct 20 2020 Eric Sandeen <sandeen@redhat.com> 5.9.0-1
- New upstream release

* Fri Sep 04 2020 Eric Sandeen <sandeen@redhat.com> 5.8.0-1
- New upstream release

* Fri Jul 24 2020 Eric Sandeen <sandeen@redhat.com> 5.7.0-1
- New upstream release
- Replace libreadline with libedit
- Add tarball signature checking

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 5.6.0-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 5.6.0-2
- Rebuild for ICU 67

* Tue Apr 14 2020 Eric Sandeen <sandeen@redhat.com> 5.6.0-1
- New upstream release

* Fri Mar 13 2020 Eric Sandeen <sandeen@redhat.com> 5.5.0-1
- New upstream release

* Fri Jan 31 2020 Eric Sandeen <sandeen@redhat.com> 5.4.0-3
- Fix global redefinitions for gcc10 build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Eric Sandeen <sandeen@redhat.com> 5.4.0-1
- New upstream release

* Fri Nov 15 2019 Eric Sandeen <sandeen@redhat.com> 5.3.0-1
- New upstream release

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 5.2.1-2
- Rebuild for ICU 65

* Wed Aug 21 2019 Eric Sandeen <sandeen@redhat.com> 5.2.1-1
- New upstream release

* Fri Aug 16 2019 Eric Sandeen <sandeen@redhat.com> 5.2.0-1
- New upstream release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eric Sandeen <sandeen@redhat.com> 5.1.0-1
- New upstream release

* Wed May 08 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-2
- Create new xfs_scrub subpackage (#1666839)

* Fri May 03 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-1
- New upstream release

* Fri Feb 22 2019 Eric Sandeen <sandeen@redhat.com> 4.20.0-1
- New upstream release

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.19.0-4
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 4.19.0-2
- Rebuild for ICU 63

* Tue Nov 13 2018 Eric Sandeen <sandeen@redhat.com> 4.19.0-1
- New upstream release

* Fri Aug 24 2018 Eric Sandeen <sandeen@redhat.com> 4.18.0-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 4.17.0-2
- Rebuild for ICU 62

* Thu Jun 28 2018 Eric Sandeen <sandeen@redhat.com> 4.17.0-1
- New upstream release

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 4.16.0-2
- Rebuild for ICU 61.1

* Thu Apr 26 2018 Eric Sandeen <sandeen@redhat.com> 4.16.0-1
- New upstream release
- Clean up specfile

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.1-1
- New upstream release
- Update Polish translation

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-2
- BuildRequires: gcc

* Sat Feb 24 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-1
- New upstream release
- Adds new xfs_scrub utility and services

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Eric Sandeen <sandeen@redhat.com> 4.14.0-1
- New upstream release

* Wed Sep 27 2017 Eric Sandeen <sandeen@redhat.com> 4.13.1-1
- New upstream release
- Trim ancient changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 4.12.0-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Eric Sandeen <sandeen@redhat.com> 4.12.0-1
- New upstream release

* Fri May 05 2017 Eric Sandeen <sandeen@redhat.com> 4.11.0-1
- New upstream release

* Sun Feb 26 2017 Eric Sandeen <sandeen@redhat.com> 4.10.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.9.0-2
- Rebuild for readline 7.x

* Thu Jan 05 2017 Eric Sandeen <sandeen@redhat.com> 4.9.0-1
- New upstream release

* Tue Oct 18 2016 Eric Sandeen <sandeen@redhat.com> 4.8.0-1
- New upstream release

* Tue Sep 06 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-2
- Add libattr-devel build dependency to fix xfs_fsr

* Sun Sep 04 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-1
- New upstream release

* Tue Mar 15 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-1
- New upstream release

* Thu Mar 10 2016 Eric Sandeen <sandeen@redhat.com> 4.3.0-3
- Fix build w/ new kernels which have [sg]etxattr promotion

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Eric Sandeen <sandeen@redhat.com> 4.3.0-1
- New upstream release

* Wed Sep 09 2015 Eric Sandeen <sandeen@redhat.com> 4.2.0-1
- New upstream release

* Thu Jul 30 2015 Eric Sandeen <sandeen@redhat.com> 3.2.4-1
- New upstream release
- Addresses CVE-2012-2150 for xfs_metadump

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Eric Sandeen <sandeen@redhat.com> 3.2.3-1
- New upstream release
