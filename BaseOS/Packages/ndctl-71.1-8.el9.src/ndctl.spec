Name:		ndctl
Version:	71.1
Release:	8%{?dist}
Summary:	Manage "libnvdimm" subsystem devices (Non-volatile Memory)
License:	GPLv2
Url:		https://github.com/pmem/ndctl
Source0:	https://github.com/pmem/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0: 0003-ndctl-test-Fix-btt-expect-table-compile-warning.patch
Patch1: 0004-ndctl-test-Cleanup-unnecessary-out-label.patch
Patch2: 0005-ndctl-test-Fix-device-dax-mremap-test.patch
Patch3: 0006-ndctl-test-Exercise-soft_offline_page-corner-cases.patch
Patch4: 0007-msft-Add-xlat_firmware_status-for-JEDEC-Byte-Address.patch
Patch5: 0008-ndctl-namespace-Fix-disable-namespace-accounting-rel.patch
Patch6: 0009-zero_info_block-skip-seed-devices.patch
Patch7: 0010-ndctl-update-.gitignore.patch
Patch8: 0011-ndctl-test-add-checking-the-presence-of-jq-command-a.patch
Patch9: 0012-Expose-ndctl_bus_nfit_translate_spa-as-a-public-func.patch
Patch10: 0013-test-libndctl-Use-ndctl_region_set_ro-to-change-disk.patch
Patch11: 0014-daxctl-fail-reconfigure-device-based-on-kernel-onlin.patch
Patch12: 0015-libdaxctl-add-an-API-to-check-if-a-device-is-active.patch
Patch13: 0016-libndctl-check-for-active-system-ram-before-disablin.patch
Patch14: 0017-daxctl-emit-counts-of-total-and-online-memblocks.patch
Patch15: 0018-libndctl-Unify-adding-dimms-for-papr-and-nfit-famili.patch
Patch16: 0019-test-Don-t-skip-tests-if-nfit-modules-are-missing.patch
Patch17: 0020-papr-Add-support-to-parse-save_fail-flag-for-dimm.patch
Patch18: 0021-Use-page-size-as-alignment-value.patch
Patch19: 0022-libndctl-Remove-redundant-checks-and-assignments.patch
Patch20: 0023-ndctl-Update-nvdimm-mailing-list-address.patch
Patch21: 0024-libndctl-papr-Fix-probe-for-papr-scm-compatible-nvdi.patch
Patch22: 0025-ndctl-scrub-Stop-translating-return-values.patch
Patch23: 0026-ndctl-scrub-Reread-scrub-engine-status-at-start.patch
Patch24: 0027-ndctl-dimm-Fix-label-index-block-calculations.patch
Patch25: 0028-ndctl-namespace-Skip-seed-namespaces-when-processing.patch
Patch26: 0029-ndctl-namespace-Suppress-ENXIO-when-processing-all-n.patch
Patch27: 0030-namespace-action-Drop-zero-namespace-checks.patch
Patch28: 0031-ndctl-add-.clang-format.patch
Patch29: 0032-cxl-add-a-cxl-utility-and-libcxl-library.patch
Patch30: 0033-cxl-add-a-local-copy-of-the-cxl_mem-UAPI-header.patch
Patch31: 0034-util-add-the-struct_size-helper-from-the-kernel.patch
Patch32: 0035-libcxl-add-support-for-command-query-and-submission.patch
Patch33: 0036-libcxl-add-support-for-the-Identify-Device-command.patch
Patch34: 0037-libcxl-add-GET_HEALTH_INFO-mailbox-command-and-acces.patch
Patch35: 0038-libcxl-add-support-for-the-GET_LSA-command.patch
Patch36: 0039-libcxl-add-label_size-to-cxl_memdev-and-an-API-to-re.patch
Patch37: 0040-libcxl-add-representation-for-an-nvdimm-bridge-objec.patch
Patch38: 0041-libcxl-add-interfaces-for-label-operations.patch
Patch39: 0042-cxl-add-commands-to-read-write-and-zero-labels.patch
Patch40: 0043-Documentation-cxl-add-library-API-documentation.patch
Patch41: 0044-ndctl-Add-CXL-packages-to-the-RPM-spec.patch
Patch42: 0045-cxl-cli-add-bash-completion.patch
Patch43: 0046-cxl-add-health-information-to-cxl-list.patch
Patch44: 0047-ndctl-install-bash-completion-symlinks.patch
Patch45: 0048-scripts-Add-a-man-page-template-generator.patch
Patch46: 0049-daxctl-Add-Soft-Reservation-theory-of-operation.patch
Patch47: 0061-libcxl-fix-potential-NULL-dereference-in-cxl_memdev_.patch
Patch48: 0064-ndctl-release-v72.patch
Patch49: 0067-ndctl-add-repology-graphic-to-README.md.patch
Patch50: 0068-Documentation-ndctl-fix-self-reference-of-ndctl-disa.patch
Patch51: 0069-ndctl-docs-Clarify-update-firwmware-activation-overf.patch
Patch52: 0070-ndctl-test-Prepare-for-BLK-aperture-support-removal.patch
Patch53: 0071-ndctl-test-Move-reset-to-function-in-common.patch
Patch54: 0072-ndctl-test-Initialize-the-label-area-by-default.patch
Patch55: 0073-ndctl-test-Skip-BLK-flags-checks.patch
Patch56: 0074-ndctl-test-Move-sector-mode-to-a-different-region.patch
Patch57: 0075-ndctl-Deprecate-BLK-aperture-support.patch
Patch58: 0076-ndctl-test-Fix-support-for-missing-dax_pmem_compat-m.patch
Patch59: 0077-util-Distribute-filter-and-json-helpers-to-per-tool-.patch
Patch60: 0078-Documentation-Drop-attrs.adoc-include.patch
Patch61: 0079-build-Drop-unnecessary-tool-config.h-includes.patch
Patch62: 0080-test-Prepare-out-of-line-builds.patch
Patch63: 0081-ndctl-Drop-executable-bit-for-bash-completion-script.patch
Patch64: 0082-build-Add-meson-build-infrastructure.patch
Patch65: 0083-build-Add-meson-rpmbuild-support.patch
Patch66: 0084-ndctl-Jettison-autotools.patch
Patch67: 0085-ndctl-build-Default-asciidoctor-to-enabled.patch
Patch68: 0086-ndctl-update-README.md-for-meson-build.patch
Patch69: 0087-test-Add-suite-identifiers-to-tests.patch
Patch70: 0088-ndctl-Rename-util_filter-to-ndctl_filter.patch
Patch71: 0089-build-Add-tags.patch
Patch72: 0090-json-Add-support-for-json_object_new_uint64.patch
Patch73: 0091-cxl-json-Cleanup-object-leak-false-positive.patch
Patch74: 0092-cxl-list-Support-multiple-memdev-device-name-filter-.patch
Patch75: 0093-cxl-list-Support-comma-separated-lists.patch
Patch76: 0094-cxl-list-Introduce-cxl_filter_walk.patch
Patch77: 0095-cxl-list-Emit-device-serial-numbers.patch
Patch78: 0096-cxl-list-Add-filter-by-serial-support.patch
Patch79: 0097-cxl-lib-Rename-nvdimm-bridge-to-pmem.patch
Patch80: 0098-cxl-list-Cleanup-options-definitions.patch
Patch81: 0099-Documentation-Enhance-libcxl-memdev-API-documentatio.patch
Patch82: 0100-cxl-list-Add-bus-objects.patch
Patch83: 0101-util-json-Warn-on-stderr-about-empty-list-results.patch
Patch84: 0102-util-sysfs-Uplevel-modalias-lookup-helper-to-util.patch
Patch85: 0103-cxl-list-Add-port-enumeration.patch
Patch86: 0104-cxl-list-Add-debug-option.patch
Patch87: 0105-cxl-list-Add-endpoints.patch
Patch88: 0106-cxl-list-Add-host-entries-for-port-like-objects.patch
Patch89: 0107-cxl-list-Add-host-entries-for-memdevs.patch
Patch90: 0108-cxl-list-Move-enabled-memdevs-underneath-their-endpo.patch
Patch91: 0109-cxl-list-Filter-memdev-by-ancestry.patch
Patch92: 0110-cxl-memdev-Use-a-local-logger-for-debug.patch
Patch93: 0111-cxl-memdev-Cleanup-memdev-filter.patch
Patch94: 0112-cxl-memdev-Add-serial-support-for-memdev-related-com.patch
Patch95: 0113-cxl-list-Add-numa_node-to-memdev-listings.patch
Patch96: 0114-util-Implement-common-bind-unbind-helpers.patch
Patch97: 0115-cxl-memdev-Enable-disable-support.patch
Patch98: 0116-cxl-list-Add-decoder-support.patch
Patch99: 0117-cxl-list-Extend-decoder-objects-with-target-informat.patch
Patch100: 0118-cxl-list-Use-physical_node-for-root-port-attachment-.patch
Patch101: 0119-cxl-list-Reuse-the-target-option-for-ports.patch
Patch102: 0120-cxl-list-Support-filtering-memdevs-by-decoders.patch
Patch103: 0121-cxl-list-Support-filtering-memdevs-by-ports.patch
Patch104: 0122-cxl-port-Add-disable-enable-port-command.patch
Patch105: 0123-cxl-list-Filter-dports-and-targets-by-memdevs.patch
Patch106: 0124-ndctl-test-make-inject-smart.sh-more-tolerant-of-dec.patch
Patch107: 0125-libndctl-papr-Add-support-for-reporting-shutdown-cou.patch
Patch108: 0126-libndctl-intel-Indicate-supported-smart-inject-types.patch
Patch109: 0127-libndctl-papr-Add-limited-support-for-inject-smart.patch
Patch110: 0128-ndtest-ack-shutdown-count-Skip-the-test-on-ndtest.patch
Patch111: 0129-ndctl-libndctl-Update-nvdimm-flags-after-smart-injec.patch
Patch112: 0132-libcxl-add-GET_PARTITION_INFO-mailbox-command-and-ac.patch
Patch113: 0133-libcxl-add-accessors-for-capacity-fields-of-the-IDEN.patch
Patch114: 0134-libcxl-return-the-partition-alignment-field-in-bytes.patch
Patch115: 0135-cxl-add-memdev-partition-information-to-cxl-list.patch
Patch116: 0136-libcxl-add-interfaces-for-SET_PARTITION_INFO-mailbox.patch
Patch117: 0137-cxl-add-command-cxl-set-partition.patch
Patch118: 0138-Update-ndctl.spec-to-allow-flatpak-builds.patch
Patch119: 0139-daxctl-provide-safe-versions-of-iteration-API.patch
Patch120: 0140-util-size.h-fix-build-for-older-compilers.patch
Patch121: 0141-build-Automate-rpmbuild.sh.patch
Patch122: 0142-util-size.h-Fix-build-error-for-GCC-10.patch
Patch123: 0143-libcxl-Remove-extraneous-NULL-checks-when-validating.patch
Patch124: 0144-libdaxctl-free-resource-allocated-with-asprintf.patch
Patch125: 0145-cxl-list-tidy-the-error-path-in-add_cxl_decoder.patch
Patch126: 0146-cxl-list-always-free-the-path-var-in-add_cxl_decoder.patch
Patch127: 0147-scripts-docsurgeon-Fix-document-header-for-section-1.patch
Patch128: 0148-ndctl-release-v73.patch
Patch130: 0150-build-Fix-Wall-and-O2-warnings.patch
Patch131: 0151-build-Fix-test-timeouts.patch
Patch132: 0155-build-Move-utility-helpers-to-libutil.a.patch
Patch133: 0156-util-Use-SZ_-size-macros-in-display-size.patch
Patch134: 0157-util-Pretty-print-terabytes.patch
Patch135: 0158-cxl-port-Fix-disable-port-man-page.patch
Patch136: 0159-cxl-bus-Add-bus-disable-support.patch
Patch137: 0160-cxl-list-Auto-enable-single-mode-for-port-listings.patch
Patch138: 0161-cxl-memdev-Fix-bus_invalidate-crash.patch
Patch139: 0162-cxl-list-Add-support-for-filtering-by-host-identifie.patch
Patch140: 0163-cxl-port-Relax-port-identifier-validation.patch
Patch142: 0165-cxl-test-Add-topology-enumeration-and-hotplug-test.patch
Patch143: 0167-daxctl-Fix-kernel-option-typo-in-Soft-Reservation-th.patch
Patch144: 0168-meson-make-modprobedatadir-an-option.patch
Patch145: 0169-namespace-action-Drop-more-zero-namespace-checks.patch
Patch146: 0170-ndctl-dimm-Flush-invalidated-labels-after-overwrite.patch
Patch147: 0171-libcxl-fix-a-segfault-when-memdev-pmem-is-absent.patch
Patch148: 0172-ndctl-bus-Handle-missing-scrub-commands-more-gracefu.patch
Patch149: 0173-util-wrapper.c-Fix-gcc-warning-in-xrealloc.patch
Patch150: 0174-libcxl-Fix-memory-leakage-in-cxl_port_init.patch
Patch151: 0175-cxl-list-Reformat-option-list.patch
Patch152: 0176-cxl-list-Emit-endpoint-decoders-filtered-by-memdev.patch
Patch153: 0177-cxl-list-Hide-0s-in-disabled-decoder-listings.patch
Patch154: 0178-cxl-list-Add-DPA-span-to-endpoint-decoder-listings.patch
Patch155: 0179-ccan-list-Import-latest-list-helpers.patch
Patch156: 0180-cxl-lib-Maintain-decoders-in-id-order.patch
Patch157: 0181-cxl-memdev-Fix-json-for-multi-device-partitioning.patch
Patch158: 0182-cxl-list-Emit-mode-for-endpoint-decoder-objects.patch
Patch159: 0183-cxl-set-partition-Accept-ram-as-an-alias-for-volatil.patch
Patch160: 0184-cxl-memdev-Add-reserve-free-dpa-commands.patch
Patch161: 0185-cxl-test-Update-CXL-memory-parameters.patch
Patch162: 0186-cxl-test-Checkout-region-setup-teardown.patch
Patch163: 0187-cxl-test-add-a-test-to-read-write-zero-labels.patch
Patch164: 0188-cxl-list-Clarify-B-vs-P-p-root.patch
Patch165: 0189-libcxl-add-a-depth-attribute-to-cxl_port.patch
Patch166: 0190-cxl-port-Consolidate-the-debug-option-in-cxl-port-ma.patch
Patch167: 0191-cxl-memdev-refactor-decoder-mode-string-parsing.patch
Patch168: 0192-libcxl-Introduce-libcxl-region-and-mapping-objects.patch
Patch169: 0193-cxl-cli-add-region-listing-support.patch
Patch170: 0194-libcxl-add-low-level-APIs-for-region-creation.patch
Patch171: 0195-cxl-add-a-create-region-command.patch
Patch172: 0196-cxl-add-commands-to-enable-disable-destroy-region.patch
Patch173: 0197-cxl-list-make-memdevs-and-regions-the-default-listin.patch
Patch174: 0198-test-add-a-cxl-create-region-test.patch
Patch175: 0199-cxl-decoder-add-a-max_available_extent-attribute.patch
Patch176: 0200-cxl-Add-list-verbose-option-to-the-cxl-command.patch
Patch177: 0201-cxl-test-Validate-endpoint-interleave-geometry.patch
Patch178: 0202-cxl-list-Add-interleave-parameters-to-decoder-listin.patch
Patch179: 0203-cxl-list-Add-region-to-decoder-listings.patch
Patch180: 0204-cxl-list-Filter-decoders-by-region.patch
Patch181: 0205-cxl-list-Add-depth-to-port-listings.patch
Patch182: 0206-cxl-test-Validate-switch-port-settings-in-cxl-region.patch
Patch183: 0207-meson-fix-modprobedatadir-default-value.patch
Patch184: 0208-ndctl-move-developer-scripts-from-contrib-to-scripts.patch
Patch185: 0209-ndctl-remove-obsolete-m4-directory.patch
Patch186: 0210-ndctl-update-.gitignore.patch
Patch187: 0211-scripts-fix-contrib-do_abidiff-for-updated-fedpkg.patch
Patch188: 0212-scripts-update-release-helper-scripts-for-meson-and-.patch
Patch189: 0213-meson.build-be-specific-for-library-path.patch
Patch190: 0214-cxl-region-fix-a-dereferecnce-after-NULL-check.patch
Patch191: 0215-libcxl-fox-a-resource-leak-and-a-forward-NULL-check.patch
Patch192: 0216-cxl-filter-Fix-an-uninitialized-pointer-dereference.patch
Patch193: 0217-ndctl-release-v74.patch

Requires:	ndctl-libs%{?_isa} = %{version}-%{release}
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires:	autoconf
%if 0%{?rhel} < 9
BuildRequires:	asciidoc
%define asciidoc -Dasciidoctor=disabled
%else
BuildRequires:	rubygem-asciidoctor
%define asciidoc -Dasciidoctor=enabled
%endif
BuildRequires:	xmlto
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	keyutils-libs-devel

%description
Utility library for managing the "libnvdimm" subsystem.  The "libnvdimm"
subsystem defines a kernel device model and control message interface for
platform NVDIMM resources like those defined by the ACPI 6+ NFIT (NVDIMM
Firmware Interface Table).


%package -n ndctl-devel
Summary:	Development files for libndctl
License:	LGPLv2
Requires:	ndctl-libs%{?_isa} = %{version}-%{release}

%description -n ndctl-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n daxctl
Summary:	Manage Device-DAX instances
License:	GPLv2
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}

%description -n daxctl
The daxctl utility provides enumeration and provisioning commands for
the Linux kernel Device-DAX facility. This facility enables DAX mappings
of performance / feature differentiated memory without need of a
filesystem.

%package -n daxctl-devel
Summary:	Development files for libdaxctl
License:	LGPLv2
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}

%description -n daxctl-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}, a library for enumerating
"Device DAX" devices.  Device DAX is a facility for establishing DAX
mappings of performance / feature-differentiated memory.

%package -n cxl-cli
Summary:	Manage CXL devices
License:	GPLv2
Requires:	cxl-libs%{?_isa} = %{version}-%{release}

%description -n cxl-cli
The cxl utility provides enumeration and provisioning commands for
the Linux kernel CXL devices.

%package -n cxl-devel
Summary:	Development files for libcxl
License:	LGPLv2
Requires:	cxl-libs%{?_isa} = %{version}-%{release}

%description -n cxl-devel
This package contains libraries and header files for developing applications
that use libcxl, a library for enumerating and communicating with CXL devices.

%package -n ndctl-libs
Summary:	Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
License:	LGPLv2
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}


%description -n ndctl-libs
Libraries for %{name}.

%package -n daxctl-libs
Summary:	Management library for "Device DAX" devices
License:	LGPLv2

%description -n daxctl-libs
Device DAX is a facility for establishing DAX mappings of performance /
feature-differentiated memory. daxctl-libs provides an enumeration /
control API for these devices.

%package -n cxl-libs
Summary:	Management library for CXL devices
License:	LGPLv2

%description -n cxl-libs
libcxl is a library for enumerating and communicating with CXL devices.


%prep
%autosetup -p1 ndctl-%{version}

%build
%meson %{?asciidoc} -Dversion-tag=%{version}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n ndctl-libs

%ldconfig_scriptlets -n daxctl-libs

%define bashcompdir %(pkg-config --variable=completionsdir bash-completion)

%files
%license LICENSES/preferred/GPL-2.0 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_bindir}/ndctl
%{_mandir}/man1/ndctl*
%{bashcompdir}/
%{_unitdir}/ndctl-monitor.service
%{_sysconfdir}/ndctl/keys/keys.readme
%{_sysconfdir}/modprobe.d/nvdimm-security.conf

%config(noreplace) %{_sysconfdir}/ndctl/monitor.conf

%files -n daxctl
%license LICENSES/preferred/GPL-2.0 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_bindir}/daxctl
%{_mandir}/man1/daxctl*
%{_datadir}/daxctl/daxctl.conf

%files -n cxl-cli
%license LICENSES/preferred/GPL-2.0 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_bindir}/cxl
%{_mandir}/man1/cxl*
%{bashcompdir}/cxl

%files -n ndctl-libs
%doc README.md
%license LICENSES/preferred/LGPL-2.1 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_libdir}/libndctl.so.*

%files -n daxctl-libs
%doc README.md
%license LICENSES/preferred/LGPL-2.1 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_libdir}/libdaxctl.so.*

%files -n cxl-libs
%doc README.md
%license LICENSES/preferred/LGPL-2.1 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_libdir}/libcxl.so.*

%files -n ndctl-devel
%license LICENSES/preferred/LGPL-2.1
%{_includedir}/ndctl/
%{_libdir}/libndctl.so
%{_libdir}/pkgconfig/libndctl.pc

%files -n daxctl-devel
%license LICENSES/preferred/LGPL-2.1
%{_includedir}/daxctl/
%{_libdir}/libdaxctl.so
%{_libdir}/pkgconfig/libdaxctl.pc

%files -n cxl-devel
%license LICENSES/preferred/LGPL-2.1
%{_includedir}/cxl/
%{_libdir}/libcxl.so
%{_libdir}/pkgconfig/libcxl.pc
%{_mandir}/man3/cxl*
%{_mandir}/man3/libcxl.3*


%changelog
* Thu Oct 13 2022 Jeff Moyer <jmoyer@redhat.com> - 71.1-8
- Backport changes up to v74, excluding the config file changes. (Jeff Moyer)
  This includes support for the CXL commands, and adds the following
  packages: cxl-cli, cxl-devel, cxl-libs
- Resolves: rhbz#2132167

* Tue Jun 14 2022 Bryan Gurney <bgurney@redhat.com> - 71.1-7
- Pull in fixes from upstream v72 and v73 (Jeff Moyer)
- Fix enable-namespace all reporting errors incorrectly
- Add support for inject-smart on papr scm
- Related: rhbz#2040075
- Related: rhbz#1873851
- Related: rhbz#1880578
- Related: rhbz#1922538
- Related: rhbz#2087707

* Wed Dec 1 2021 Bryan Gurney <bgurney@redhat.com> - 71.1-6
- Add gating test
- Related: rhbz#2028152

* Mon Nov 29 2021 Bryan Gurney <bgurney@redhat.com> - 71.1-5
- Rebuild with latest json-c version
- Related: rhbz#2023317

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 71.1-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 71.1-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 71.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Vishal Verma <vishal.l.verma@intel.com> - 71.1-1
- release v71.1

* Sat Dec 19 2020 Vishal Verma <vishal.l.verma@intel.com> - 71-1
- release v71

* Sat Oct 10 2020 Vishal Verma <vishal.l.verma@intel.com> - 70.1-1
- release v70.1

* Tue Oct 06 2020 Vishal Verma <vishal@stellar.sh> - 70-1
- release v70

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Vishal Verma <vishal.l.verma@intel.com> - 69-1
- release v69

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 68-2
- Rebuild (json-c)

* Tue Mar 24 2020 Vishal Verma <vishal@stellar.sh> - 68-1
- release v68

* Fri Jan 31 2020 Vishal Verma <vishal.l.verma@intel.com> - 67-3
- Add fix for GCC10 builds

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Vishal Verma <vishal.l.verma@intel.com> - 67-1
- release v67

* Wed Aug 07 2019 Vishal Verma <vishal.l.verma@intel.com> - 66-1
- release v66

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Vishal Verma <vishal.l.verma@intel.com> - 65-1
- release v65

* Wed Feb 06 2019 Vishal Verma <vishal.l.verma@intel.com> - 64.1-1
- release v64.1

* Mon Feb 04 2019 Vishal Verma <vishal.l.verma@intel.com> - 64-1
- release v64

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Vishal Verma <vishal.l.verma@intel.com> - 63-1
- release v63
- remove ndctl-udev and related files

* Tue Aug 14 2018 Vishal Verma <vishal@stellar.sh> - 62-1
- release v62
- Add files for udev and ndctl-monitor

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Vishal Verma <vishal.l.verma@intel.com> - 61.2-1
- release v61.2

* Tue Jun 26 2018 Vishal Verma <vishal@stellar.sh> - 61.1-1
- release v61.1

* Tue Jun 26 2018 Vishal Verma <vishal@stellar.sh> - 61-1
- new version

* Thu May 17 2018 Dan Williams <dan.j.williams@intel.com> - 60.3-1
- release v60.3

* Mon Apr 23 2018 Dan Williams <dan.j.williams@intel.com> - 60.1-1
- release v60.1

* Thu Apr 19 2018 Dan Williams <dan.j.williams@intel.com> - 60-1
- release v60

* Tue Mar 27 2018 Dan Williams <dan.j.williams@intel.com> - 59.3-1
- release v59.3

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 59.2-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Dan Williams <dan.j.williams@intel.com> - 59.2-1
- release v59.2

* Fri Feb 09 2018 Dan Williams <dan.j.williams@intel.com> - 59.1-1
- release v59.1

* Fri Feb 09 2018 Dan Williams <dan.j.williams@intel.com> - 59-1
- release v59

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 58.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 58.4-2
- Rebuilt for libjson-c.so.3

* Thu Nov 16 2017 Dan Williams <dan.j.williams@intel.com> - 58.4-1
- release v58.4

* Thu Sep 21 2017 Dan Williams <dan.j.williams@intel.com> - 58.2-1
- release v58.2

* Fri Sep 08 2017 Dan Williams <dan.j.williams@intel.com> - 58.1-2
- gate libpmem dependency on x86_64

* Fri Sep 08 2017 Dan Williams <dan.j.williams@intel.com> - 58.1-1
- add libpmem dependency
- release v58.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Dan Williams <dan.j.williams@intel.com> - 57.1-1
- Release v57.1

* Sat May 27 2017 Dan Williams <dan.j.williams@intel.com> - 57-1
- Release v57

* Fri Feb 10 2017 Dan Williams <dan.j.williams@intel.com> - 56-1
- Release v56

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Dan Williams <dan.j.williams@intel.com> - 55-1
- release v55

* Fri Aug 05 2016 Dan Williams <dan.j.williams@intel.com> - 54-1
- add explicit lib version dependencies

* Sat May 28 2016 Dan Williams <dan.j.williams@intel.com> - 53.1-1
- Fix up tag format vs source url confusion

* Fri May 27 2016 Dan Williams <dan.j.williams@intel.com> - 53-1
- add daxctl-libs + daxctl-devel packages
- add bash completion

* Mon Apr 04 2016 Dan Williams <dan.j.williams@intel.com> - 52-1
- Initial rpm submission to Fedora
