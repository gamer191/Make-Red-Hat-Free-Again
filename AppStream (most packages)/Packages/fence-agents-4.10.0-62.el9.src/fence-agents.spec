# Copyright 2004-2011 Red Hat, Inc.
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU General Public License v.2.

# keep around ready for later user
## global alphatag git0a6184070

# bundles
# azure
%global oauthlib		oauthlib
%global oauthlib_version	3.2.2
# kubevirt
%global openshift		openshift
%global openshift_version	0.12.1
%global ruamelyamlclib		ruamel.yaml.clib
%global ruamelyamlclib_version	0.2.6
%global kubernetes		kubernetes
%global kubernetes_version	12.0.1
%global certifi 		certifi
%global certifi_version 	2023.7.22
%global googleauth		google-auth
%global googleauth_version	2.3.0
%global cachetools		cachetools
%global cachetools_version	4.2.4
%global pyasn1modules		pyasn1-modules
%global pyasn1modules_version	0.2.8
%global pyasn1			pyasn1
%global pyasn1_version		0.4.8
%global dateutil		dateutil
%global dateutil_version	2.8.2
%global pyyaml			PyYAML
%global pyyaml_version		5.1
%global six			six
%global six_version		1.16.0
%global urllib3 		urllib3
%global urllib3_version 	1.26.18
%global websocketclient 	websocket-client
%global websocketclient_version 1.2.1
%global jinja2			Jinja2
%global jinja2_version		3.1.3
%global markupsafe		MarkupSafe
%global markupsafe_version	2.0.1
%global stringutils		string-utils
%global stringutils_version	1.0.0
%global requests		requests
%global requests_version	2.26.0
%global chrstnormalizer		charset-normalizer
%global chrstnormalizer_version	2.0.7
%global idna			idna
%global idna_version		3.3
%global reqstsoauthlib		requests-oauthlib
%global reqstsoauthlib_version	1.3.0
%global ruamelyaml		ruamel.yaml
%global ruamelyaml_version	0.17.16
%global setuptools		setuptools
%global setuptools_version	58.3.0

Name: fence-agents
Summary: Set of unified programs capable of host isolation ("fencing")
Version: 4.10.0
Release: 62%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
URL: https://github.com/ClusterLabs/fence-agents
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.gz
### HA support requirements-*.txt ###
Source100: requirements-aliyun.txt
Source101: requirements-aws.txt
Source102: requirements-azure.txt
Source103: requirements-google.txt
Source104: requirements-common.txt
### HA support libs/utils ###
# awscli 2+ is only available from github (and needs to be renamed from aws-cli... to awscli)
Source900: awscli-2.2.15.tar.gz
# From awscli's requirements.txt: https://github.com/boto/botocore/zipball/v2#egg=botocore
Source901: botocore-2.0.0dev123.zip
# update with ./update-ha-support.sh and replace lines below with output
### BEGIN ###
# aliyun
Source1000: aliyun-python-sdk-core-2.11.5.tar.gz
Source1001: aliyun_python_sdk_ecs-4.24.7-py2.py3-none-any.whl
Source1002: aliyuncli-2.1.10-py2.py3-none-any.whl
Source1003: cffi-1.14.5-cp39-cp39-manylinux1_x86_64.whl
Source1004: colorama-0.3.3.tar.gz
Source1005: jmespath-0.7.1-py2.py3-none-any.whl
Source1006: pycryptodome-3.20.0.tar.gz
Source1007: pycparser-2.20-py2.py3-none-any.whl
# awscli
Source1008: awscrt-0.11.13-cp39-cp39-manylinux2014_x86_64.whl
Source1009: colorama-0.4.3-py2.py3-none-any.whl
Source1010: cryptography-3.3.2-cp36-abi3-manylinux2010_x86_64.whl
Source1011: distro-1.5.0-py2.py3-none-any.whl
Source1012: docutils-0.15.2-py3-none-any.whl
Source1013: prompt_toolkit-2.0.10-py3-none-any.whl
Source1014: ruamel.yaml-0.15.100.tar.gz
Source1015: six-1.16.0-py2.py3-none-any.whl
Source1016: wcwidth-0.1.9-py2.py3-none-any.whl
# aws
Source1017: boto3-1.17.102-py2.py3-none-any.whl
Source1018: botocore-1.20.102-py2.py3-none-any.whl
Source1019: python_dateutil-2.8.1-py2.py3-none-any.whl
Source1020: s3transfer-0.4.2-py2.py3-none-any.whl
Source1021: urllib3-1.26.18.tar.gz
# azure
Source1022: adal-1.2.7-py2.py3-none-any.whl
Source1023: azure_common-1.1.27-py2.py3-none-any.whl
Source1024: azure_core-1.15.0-py2.py3-none-any.whl
Source1025: azure_mgmt_compute-21.0.0-py2.py3-none-any.whl
Source1026: azure_mgmt_core-1.2.2-py2.py3-none-any.whl
Source1027: azure_mgmt_network-19.0.0-py2.py3-none-any.whl
Source1028: azure-identity-1.10.0.zip
Source1029: chardet-4.0.0-py2.py3-none-any.whl
Source1030: idna-2.10-py2.py3-none-any.whl
Source1031: isodate-0.6.0-py2.py3-none-any.whl
Source1032: msrest-0.6.21-py2.py3-none-any.whl
Source1033: msrestazure-0.6.4-py2.py3-none-any.whl
Source1034: %{oauthlib}-%{oauthlib_version}.tar.gz
Source1035: PyJWT-2.1.0-py3-none-any.whl
Source1036: requests-2.25.1-py2.py3-none-any.whl
Source1037: requests_oauthlib-1.3.0-py2.py3-none-any.whl
Source1038: msal-1.18.0.tar.gz
Source1039: msal-extensions-1.0.0.tar.gz
Source1040: portalocker-2.5.1.tar.gz
# google
Source1041: cachetools-4.2.2-py3-none-any.whl
Source1042: chardet-3.0.4-py2.py3-none-any.whl
Source1043: google_api_core-1.30.0-py2.py3-none-any.whl
Source1044: google_api_python_client-1.12.8-py2.py3-none-any.whl
Source1045: googleapis_common_protos-1.53.0-py2.py3-none-any.whl
Source1046: google_auth-1.32.0-py2.py3-none-any.whl
Source1047: google_auth_httplib2-0.1.0-py2.py3-none-any.whl
Source1048: httplib2-0.19.1-py3-none-any.whl
Source1049: packaging-20.9-py2.py3-none-any.whl
Source1050: protobuf-3.17.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl
Source1051: pyasn1-0.4.8-py2.py3-none-any.whl
Source1052: pyasn1_modules-0.2.8-py2.py3-none-any.whl
Source1053: pyparsing-2.4.7-py2.py3-none-any.whl
Source1054: pyroute2-0.6.4.tar.gz
Source1055: pyroute2.core-0.6.4.tar.gz
Source1056: pyroute2.ethtool-0.6.4.tar.gz
Source1057: pyroute2.ipdb-0.6.4.tar.gz
Source1058: pyroute2.ipset-0.6.4.tar.gz
Source1059: pyroute2.ndb-0.6.4.tar.gz
Source1060: pyroute2.nftables-0.6.4.tar.gz
Source1061: pyroute2.nslink-0.6.4.tar.gz
Source1062: pytz-2021.1-py2.py3-none-any.whl
Source1063: rsa-4.7.2-py3-none-any.whl
Source1064: setuptools-57.0.0-py3-none-any.whl
Source1065: uritemplate-3.0.1-py2.py3-none-any.whl
# common (pexpect / suds)
Source1066: pexpect-4.8.0-py2.py3-none-any.whl
Source1067: ptyprocess-0.7.0-py2.py3-none-any.whl
Source1068: suds_community-0.8.5-py3-none-any.whl
### END ###
# kubevirt
## pip download --no-binary :all: openshift "ruamel.yaml.clib>=0.1.2"
### BEGIN
Source1069: %{openshift}-%{openshift_version}.tar.gz
Source1070: %{ruamelyamlclib}-%{ruamelyamlclib_version}.tar.gz
Source1071: %{kubernetes}-%{kubernetes_version}.tar.gz
Source1072: %{certifi}-%{certifi_version}.tar.gz
Source1073: %{googleauth}-%{googleauth_version}.tar.gz
Source1074: %{cachetools}-%{cachetools_version}.tar.gz
Source1075: %{pyasn1modules}-%{pyasn1modules_version}.tar.gz
Source1076: %{pyasn1}-%{pyasn1_version}.tar.gz
Source1077: python-%{dateutil}-%{dateutil_version}.tar.gz
Source1078: %{pyyaml}-%{pyyaml_version}.tar.gz
## rsa is dependency for "pip install",
## but gets removed to use cryptography lib instead
Source1079: rsa-4.7.2.tar.gz
Source1080: %{six}-%{six_version}.tar.gz
Source1081: %{websocketclient}-%{websocketclient_version}.tar.gz
Source1082: %{jinja2}-%{jinja2_version}.tar.gz
Source1083: %{markupsafe}-%{markupsafe_version}.tar.gz
Source1084: python-%{stringutils}-%{stringutils_version}.tar.gz
Source1085: %{requests}-%{requests_version}.tar.gz
Source1086: %{chrstnormalizer}-%{chrstnormalizer_version}.tar.gz
Source1087: %{idna}-%{idna_version}.tar.gz
Source1088: %{reqstsoauthlib}-%{reqstsoauthlib_version}.tar.gz
Source1089: %{ruamelyaml}-%{ruamelyaml_version}.tar.gz
Source1090: %{setuptools}-%{setuptools_version}.tar.gz
## required for installation
Source1091: setuptools_scm-6.3.2.tar.gz
Source1092: packaging-21.2-py3-none-any.whl
Source1093: poetry-core-1.0.7.tar.gz
Source1094: pyparsing-3.0.1.tar.gz
Source1095: tomli-1.0.1.tar.gz
Source1096: wheel-0.37.0-py2.py3-none-any.whl
### END

Patch0: ha-cloud-support-aliyun.patch
Patch1: ha-cloud-support-aws.patch
Patch2: ha-cloud-support-azure.patch
Patch3: ha-cloud-support-google.patch
Patch4: bundled-pexpect.patch
Patch5: bundled-suds.patch
Patch6: bz2010652-fence_azure_arm-fix-sovereign-cloud-msi-support.patch
Patch7: bz2010709-1-fence_amt_ws-fix-or-causing-dead-code.patch
Patch8: bz2010709-2-fence_amt_ws-boot-option.patch
Patch9: bz2000954-1-configure-fix-virt.patch
Patch10: bz2000954-2-fence_kubevirt.patch
Patch11: bz2022334-fence_zvmip-add-ssl-tls-support.patch
Patch12: bz2029791-1-fence_openstack-add-ssl-insecure.patch
Patch13: bz2029791-2-fence_openstack-cacert-default.patch
Patch14: bz2000954-3-fence_kubevirt-get-namespace-from-context.patch
Patch15: bz2041933-bz2041935-1-fence_openstack-clouds-openrc.patch
Patch16: bz2041933-bz2041935-2-fence_openstack-clouds-openrc.patch
Patch17: bz2042496-fence_ibm_vpc-fence_ibm_powervs.patch
Patch18: bz2022334-fence_zvmip-add-disable-ssl.patch
Patch19: bz2065114-fence_lpar-refactor.patch
Patch20: bz2072420-1-all-agents-unify-ssl-parameters.patch
Patch21: bz2079889-fence_gce-update.patch
Patch22: bz2081235-fence_ibm_vpc-fix-parameters.patch
Patch23: bz2086559-fence_apc-fence_ilo_moonshot-import-logging.patch
Patch24: bz2072420-2-fence_zvmip-connect-error.patch
Patch25: bz2092385-fence_ibm_vpc-add-proxy-support.patch
Patch26: bz2093216-fence_ibm_powervs-proxy-private-api-servers.patch
Patch27: bz2041933-bz2041935-3-fencing-source_env-dont-process-empty-lines.patch
Patch28: bz2122944-1-fence_vmware_soap-set-timeout-cleanup-tmp-dirs.patch
Patch29: bz2122944-2-fence_vmware_soap-login-timeout-15s.patch
Patch30: bz2111998-fence_ibm_vpc-add-token-cache-support.patch
Patch31: bz2132008-fence_virt-add-note-reboot-action.patch
Patch32: bz2134015-fence_lpar-only-output-additional-info-on-debug.patch
Patch33: bz2136191-fence_ibm_powervs-improve-defaults.patch
Patch34: bz2138823-fence_virtd-update-manpage.patch
Patch35: bz2144531-fence_virtd-warn-files-not-mode-600.patch
Patch36: bz2149655-fence_virtd-update-fence_virt.conf-manpage.patch
Patch37: bz2160480-fence_scsi-fix-validate-all.patch
Patch38: bz2152107-fencing-1-add-plug_separator.patch
Patch39: bz2152107-fencing-2-update-DEPENDENCY_OPT.patch
Patch40: bz2183162-fence_aws-1-add-skip-race-check-parameter.patch
Patch41: bz2183162-fence_aws-2-fail-when-power-action-request-fails.patch
Patch42: bz2187327-fence_scsi-1-detect-devices-in-shared-vgs.patch
Patch43: bz2187327-fence_scsi-2-support-space-separated-devices.patch
Patch44: bz2211930-fence_azure-arm-stack-hub-support.patch
Patch45: bz2221643-fence_ibm_powervs-performance-improvements.patch
Patch46: bz2224267-fence_ipmilan-fix-typos-in-metadata.patch
Patch47: RHEL-5396-fence_scsi-1-fix-ISID-reg-handling.patch
Patch48: RHEL-5396-fence_scsi-2-fix-ISID-reg-handling-off.patch
Patch49: RHEL-14344-fence_zvmip-1-document-user-permissions.patch
Patch50: RHEL-14030-1-all-agents-metadata-update-IO-Power-Network.patch
Patch51: RHEL-14030-2-fence_cisco_mds-undo-metadata-change.patch
Patch52: RHEL-14344-fence_zvmip-2-fix-manpage-formatting.patch

### HA support libs/utils ###
# all archs
Patch1000: bz2217902-1-kubevirt-fix-bundled-dateutil-CVE-2007-4559.patch
# cloud (x86_64 only)
Patch2000: bz2217902-2-aws-awscli-azure-fix-bundled-dateutil-CVE-2007-4559.patch

%global supportedagents amt_ws apc apc_snmp bladecenter brocade cisco_mds cisco_ucs compute drac5 eaton_snmp emerson eps evacuate hpblade ibmblade ibm_powervs ibm_vpc ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan kdump kubevirt lpar mpath redfish rhevm rsa rsb sbd scsi vmware_rest vmware_soap wti
%ifarch x86_64
%global testagents virsh heuristics_ping aliyun aws azure_arm gce openstack virt
%endif
%ifarch ppc64le
%global testagents virsh heuristics_ping openstack
%endif
%ifarch s390x
%global testagents virsh zvm heuristics_ping
%endif
%ifnarch x86_64 ppc64le s390x
%global testagents virsh heuristics_ping
%endif

# skipped: pve, raritan, rcd-serial, virsh
%global allfenceagents %(cat <<EOF
fence-agents-amt-ws \\
fence-agents-apc \\
fence-agents-apc-snmp \\
fence-agents-bladecenter \\
fence-agents-brocade \\
fence-agents-cisco-mds \\
fence-agents-cisco-ucs \\
fence-agents-drac5 \\
fence-agents-eaton-snmp \\
fence-agents-emerson \\
fence-agents-eps \\
fence-agents-heuristics-ping \\
fence-agents-hpblade \\
fence-agents-ibmblade \\
fence-agents-ifmib \\
fence-agents-ilo-moonshot \\
fence-agents-ilo-mp \\
fence-agents-ilo-ssh \\
fence-agents-ilo2 \\
fence-agents-intelmodular \\
fence-agents-ipdu \\
fence-agents-ipmilan \\
fence-agents-kdump \\
fence-agents-mpath \\
fence-agents-redfish \\
fence-agents-rhevm \\
fence-agents-rsa \\
fence-agents-rsb \\
fence-agents-sbd \\
fence-agents-scsi \\
fence-agents-vmware-rest \\
fence-agents-vmware-soap \\
fence-agents-wti \\

EOF)

%ifarch x86_64
%global allfenceagents %(cat <<EOF
%{allfenceagents} \\
fence-virt \\

EOF)
%endif

# Build dependencies
## general
BuildRequires: autoconf automake libtool make
## compiled code (-kdump)
BuildRequires: gcc
## man pages generating
BuildRequires: libxslt
## Python dependencies
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
BuildRequires: python3-devel python3-pip
# wheel for HA support subpackages
BuildRequires: python3-wheel
BuildRequires: python3-pycurl python3-requests
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7
BuildRequires: openwsman-python3
%endif
%if 0%{?suse_version}
BuildRequires: python3-openwsman
%endif
%else
BuildRequires: python-devel
BuildRequires: python-pycurl python-requests
BuildRequires: openwsman-python
%endif

# fence-virt
%if 0%{?suse_version}
%define nss_devel mozilla-nss-devel
%define nspr_devel mozilla-nspr-devel
%define systemd_units systemd
%else
%define nss_devel nss-devel
%define nspr_devel nspr-devel
%define systemd_units systemd-units
%endif

BuildRequires:  corosynclib-devel libvirt-devel
BuildRequires:  libxml2-devel %{nss_devel} %{nspr_devel}
BuildRequires:  flex bison libuuid-devel
BuildRequires: %{systemd_units}


# turn off the brp-python-bytecompile script
# (for F28+ or equivalent, the latter is the preferred form)
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompilespace:.*$!!g')
#undefine __brp_python_bytecompile

%prep
%setup -q -n %{name}-%{version}%{?rcver:%{rcver}}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}
%patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%patch -p1 -P 4
%patch -p1 -P 5
%patch -p1 -P 6
%patch -p1 -P 7
%patch -p1 -P 8
%patch -p1 -P 9
%patch -p1 -P 10
%patch -p1 -P 11
%patch -p1 -P 12
%patch -p1 -P 13
%patch -p1 -P 14 -F2
%patch -p1 -P 15 -F1
%patch -p1 -P 16
%patch -p1 -P 17
%patch -p1 -P 18
%patch -p1 -P 19
%patch -p1 -P 20
%patch -p1 -P 21
%patch -p1 -P 22
%patch -p1 -P 23
%patch -p1 -P 24
%patch -p1 -P 25
%patch -p1 -P 26
%patch -p1 -P 27
%patch -p1 -P 28
%patch -p1 -P 29
%patch -p1 -P 30
%patch -p1 -P 31
%patch -p1 -P 32
%patch -p1 -P 33
%patch -p1 -P 34
%patch -p1 -P 35
%patch -p1 -P 36
%patch -p1 -P 37
%patch -p1 -P 38
%patch -p1 -P 39
%patch -p1 -P 40
%patch -p1 -P 41
%patch -p1 -P 42
%patch -p1 -P 43
%patch -p1 -P 44
%patch -p1 -P 45
%patch -p1 -P 46
%patch -p1 -P 47
%patch -p1 -P 48
%patch -p1 -P 49
%patch -p1 -P 50
%patch -p1 -P 51
%patch -p1 -P 52

# prevent compilation of something that won't get used anyway
sed -i.orig 's|FENCE_ZVM=1|FENCE_ZVM=0|' configure.ac

%build
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
	export PYTHON="%{__python3}"
%endif

# support libs
%ifarch x86_64
LIBS="%{_sourcedir}/requirements-*.txt"
echo "awscli" >> %{_sourcedir}/requirements-awscli.txt
%endif
%ifnarch x86_64
LIBS="%{_sourcedir}/requirements-common.txt"
%endif
for x in $LIBS; do
	%{__python3} -m pip install --target support/$(echo $x | sed -E "s/.*requirements-(.*).txt/\1/") --no-index --find-links %{_sourcedir} -r $x
done

# fix incorrect #! detected by CI
%ifarch x86_64
sed -i -e "/^#\!\/Users/c#\!%{__python3}" support/aws/bin/jp support/aliyun/bin/jp support/awscli/bin/jp
%endif

%ifarch x86_64
sed -i -e "/^import awscli.clidriver/isys.path.insert(0, '/usr/lib/%{name}/support/awscli')" support/awscli/bin/aws
%endif

# kubevirt
%{__python3} -m pip install --user --no-index --find-links %{_sourcedir} setuptools-scm
%{__python3} -m pip install --target support/kubevirt --no-index --find-links %{_sourcedir} openshift
rm -rf kubevirt/rsa*

# regular patch doesnt work in build-section
pushd support
/usr/bin/patch --no-backup-if-mismatch -p1 --fuzz=0 < %{PATCH1000}

%ifarch x86_64
/usr/bin/patch --no-backup-if-mismatch -p1 --fuzz=0 < %{PATCH2000}
%endif
popd

./autogen.sh
%{configure} --disable-libvirt-qmf-plugin PYTHONPATH="support/aliyun:support/aws:support/azure:support/google:support/common" \
%if %{defined _tmpfilesdir}
	SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
	--with-fencetmpdir=/run/fence-agents \
%endif
	--with-agents='%{supportedagents} %{testagents}'

CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}

# support libs
mkdir -p %{buildroot}%{_usr}/lib/%{name}
mv support %{buildroot}%{_usr}/lib/%{name}

export PYTHONPATH=%{buildroot}%{_usr}/lib/%{name}/support
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/
%ifarch x86_64
install -m 0644 agents/virt/fence_virtd.service %{buildroot}/%{_unitdir}/
%endif
# bytecompile Python source code in a non-standard location
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/fence
%endif
# XXX unsure if /usr/sbin/fence_* should be compiled as well

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# remove .a files
rm -f %{buildroot}/%{_libdir}/%{name}/*.*a
rm -f %{buildroot}/%{_libdir}/fence-virt/*.*a

%post
ccs_update_schema > /dev/null 2>&1 ||:
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable fence_virtd.service &> /dev/null || :
    /bin/systemctl stop fence_virtd.service &> /dev/null || :
fi

%postun
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
/bin/systemctl daemon-reload &> /dev/null || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart fence_virtd.service &> /dev/null || :
fi

%triggerun -- fence_virtd < 0.3.0-1
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Packages_migrating_to_a_systemd_unit_file_from_a_SysV_initscript
/usr/bin/systemd-sysv-convert --save fence_virtd &> /dev/null || :
/sbin/chkconfig --del fence_virtd &> /dev/null || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
/bin/systemctl try-restart fence_virtd.service &> /dev/null || :

%description
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar. They operate through a unified interface
(calling conventions) devised for the original Red Hat clustering solution.

%package common
License: GPLv2+ and LGPLv2+
Summary: Common base for Fence Agents
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-pycurl
%else
Requires: python-pycurl
%endif
# pexpect / suds
Provides: bundled(python-pexpect) = 4.8.0
Provides: bundled(python-ptyprocess) = 0.7.0
Provides: bundled(python-suds) = 0.8.5
BuildArch: noarch
%description common
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package contains support files including the Python fencing library.
%files common
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_datadir}/fence
%exclude %{_datadir}/fence/azure_fence.*
%exclude %{_datadir}/fence/__pycache__/azure_fence.*
%exclude %{_datadir}/fence/XenAPI.*
%exclude %{_datadir}/fence/__pycache__/XenAPI.*
%{_datadir}/cluster
%exclude %{_datadir}/cluster/fence_mpath_check*
%exclude %{_datadir}/cluster/fence_scsi_check*
%{_datadir}/pkgconfig/%{name}.pc
%exclude %{_sbindir}/*
%exclude %{_mandir}/man8/*
%if %{defined _tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%endif
%if %{defined _tmpfilesdir}
%dir %attr (1755, root, root)	/run/%{name}
%else
%dir %attr (1755, root, root)	%{_var}/run/%{name}
%endif
%dir %{_usr}/lib/%{name}
%{_usr}/lib/%{name}/support/common

%ifarch x86_64
%package -n ha-cloud-support
License: GPLv2+ and LGPLv2+
Summary: Support libraries for HA Cloud agents
# aliyun
Provides: bundled(python-aliyun-python-sdk-core) = 2.11.5
Provides: bundled(python-aliyun-python-sdk-ecs) = 4.24.7
Provides: bundled(aliyuncli) = 2.1.10
Provides: bundled(python-cffi) = 1.14.5
Provides: bundled(python-colorama) = 0.3.3
Provides: bundled(python-jmespath) = 0.7.1
Provides: bundled(python-pycryptodome) = 3.20.0
Provides: bundled(python-pycparser) = 2.20
# awscli
Provides: bundled(awscli) = 2.2.15
Provides: bundled(python-awscrt) = 0.11.13
Provides: bundled(python-colorama) = 0.4.3
Provides: bundled(python-cryptography) = 3.3.2
Provides: bundled(python-distro) = 1.5.0
Provides: bundled(python-docutils) = 0.15.2
Provides: bundled(python-prompt-toolkit) = 2.0.10
Provides: bundled(python-ruamel-yaml) = 0.15.100
Provides: bundled(python-six) = 1.16.0
Provides: bundled(python-wcwidth) = 0.1.9
# aws
Provides: bundled(python-boto3) = 1.17.102
Provides: bundled(python-botocore) = 1.20.102
Provides: bundled(python-dateutil) = 2.8.1
Provides: bundled(python-s3transfer) = 0.4.2
Provides: bundled(python-urllib3) = 1.26.18
# azure
Provides: bundled(python-adal) = 1.2.7
Provides: bundled(python-azure-common) = 1.1.27
Provides: bundled(python-azure-core) = 1.15.0
Provides: bundled(python-azure-mgmt-compute) = 21.0.0
Provides: bundled(python-azure-mgmt-core) = 1.2.2
Provides: bundled(python-azure-mgmt-network) = 19.0.0
Provides: bundled(python-certifi) = %{certifi_version}
Provides: bundled(python-chardet) = 4.0.0
Provides: bundled(python-idna) = 2.10
Provides: bundled(python-isodate) = 0.6.0
Provides: bundled(python-msrest) = 0.6.21
Provides: bundled(python-msrestazure) = 0.6.4
Provides: bundled(python-oauthlib) = 3.1.1
Provides: bundled(python-PyJWT) = 2.1.0
Provides: bundled(python-requests) = 2.25.1
Provides: bundled(python-requests-oauthlib) = 1.3.0
# google
Provides: bundled(python-cachetools) = 4.2.2
Provides: bundled(python-chardet) = 3.0.4
Provides: bundled(python-google-api-core) = 1.30.0
Provides: bundled(python-google-api-client) = 1.12.8
Provides: bundled(python-googleapis-common-protos) = 1.53.0
Provides: bundled(python-google-auth) = 1.32.0
Provides: bundled(python-google-auth-httplib2) = 0.1.0
Provides: bundled(python-httplib2) = 0.19.1
Provides: bundled(python-packaging) = 20.9
Provides: bundled(python-protobuf) = 3.17.3
Provides: bundled(python-pyasn1) = 0.4.8
Provides: bundled(python-pyasn1-modules) = 0.2.8
Provides: bundled(python-pyparsing) = 2.4.7
Provides: bundled(python-pyroute2) = 0.6.4
Provides: bundled(python-pyroute2-core) = 0.6.4
Provides: bundled(python-pyroute2-ethtool) = 0.6.4
Provides: bundled(python-pyroute2-ipdb) = 0.6.4
Provides: bundled(python-pyroute2-ipset) = 0.6.4
Provides: bundled(python-pyroute2-ndb) = 0.6.4
Provides: bundled(python-pyroute2-nftables) = 0.6.4
Provides: bundled(python-pyroute2-nslink) = 0.6.4
Provides: bundled(python-pytz) = 2021.1
Provides: bundled(python-rsa) = 4.7.2
Provides: bundled(python-setuptools) = 57.0.0
Provides: bundled(python-uritemplate) = 3.0.1
%description -n ha-cloud-support
Support libraries for Fence Agents.
%files -n ha-cloud-support
%dir %{_usr}/lib/%{name}
%{_usr}/lib/%{name}/support
%exclude %{_usr}/lib/%{name}/support/common
%exclude %{_usr}/lib/%{name}/support/kubevirt
%endif

%package all
License: GPLv2+ and LGPLv2+ and ASL 2.0
Summary: Set of unified programs capable of host isolation ("fencing")
Requires: %{allfenceagents}
%ifarch ppc64le
Requires: fence-agents-lpar >= %{version}-%{release}
%endif
%ifarch s390x
Requires: fence-agents-zvm >= %{version}-%{release}
%endif
Provides: fence-agents = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description all
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package serves as a catch-all for all supported fence agents.
%files all

%ifarch x86_64
%package aliyun
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Alibaba Cloud (Aliyun)
Requires: fence-agents-common >= %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Requires: python3-jmespath >= 0.9.0
Obsoletes: %{name} < %{version}-%{release}
%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.
%files aliyun
%defattr(-,root,root,-)
%{_sbindir}/fence_aliyun
%{_mandir}/man8/fence_aliyun.8*
%endif

%package amt-ws
License: ASL 2.0
Summary: Fence agent for Intel AMT (WS-Man) devices
Requires: fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7
Requires: openwsman-python3
%endif
%if 0%{?suse_version}
Requires: python3-openwsman
%endif
%else
Requires: openwsman-python
%endif
BuildArch: noarch
%description amt-ws
Fence agent for AMT (WS-Man) devices.
%files amt-ws
%{_sbindir}/fence_amt_ws
%{_mandir}/man8/fence_amt_ws.8*

%package apc
License: GPLv2+ and LGPLv2+
Summary: Fence agent for APC devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc
Fence agent for APC devices that are accessed via telnet or SSH.
%files apc
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License: GPLv2+ and LGPLv2+
Summary: Fence agents for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc-snmp
Fence agents for APC devices that are accessed via the SNMP protocol.
%files apc-snmp
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*
%{_sbindir}/fence_tripplite_snmp
%{_mandir}/man8/fence_tripplite_snmp.8*

%ifarch x86_64
%package aws
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description aws
Fence agent for Amazon AWS instances.
%files aws
%{_sbindir}/fence_aws
%{_mandir}/man8/fence_aws.8*
%endif

%ifarch x86_64
%package azure-arm
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description azure-arm
Fence agent for Azure Resource Manager instances.
%files azure-arm
%{_sbindir}/fence_azure_arm
%{_datadir}/fence/azure_fence.py*
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7
%{_datadir}/fence/__pycache__/azure_fence.*
%endif
%{_mandir}/man8/fence_azure_arm.8*
%endif

%package bladecenter
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM BladeCenter
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description bladecenter
Fence agent for IBM BladeCenter devices that are accessed
via telnet or SSH.
%files bladecenter
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Brocade switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description brocade
Fence agent for Brocade devices that are accessed via telnet or SSH.
%files brocade
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-mds
Fence agent for Cisco MDS 9000 series devices that are accessed
via the SNMP protocol.
%files cisco-mds
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Cisco UCS series
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-pycurl
%else
Requires: python-pycurl
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-ucs
Fence agent for Cisco UCS series devices that are accessed
via the SNMP protocol.
%files cisco-ucs
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%ifarch x86_64 ppc64le
%package compute
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Nova compute nodes
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-requests
%else
Requires: python-requests
%endif
Requires: fence-agents-common = %{version}-%{release}
Obsoletes: ha-openstack-support <= %{version}-%{release}
%description compute
Fence agent for Nova compute nodes.
%files compute
%{_sbindir}/fence_compute
%{_sbindir}/fence_evacuate
%{_mandir}/man8/fence_compute.8*
%{_mandir}/man8/fence_evacuate.8*
%endif

%package drac5
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Dell DRAC 5
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description drac5
Fence agent for Dell DRAC 5 series devices that are accessed
via telnet or SSH.
%files drac5
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eaton-snmp
Fence agent for Eaton network power switches that are accessed
via the SNMP protocol.
%files eaton-snmp
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package emerson
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description emerson
Fence agent for Emerson devices that are accessed via
the SNMP protocol.
%files emerson
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License: GPLv2+ and LGPLv2+
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eps
Fence agent for ePowerSwitch 8M+ power switches that are accessed
via the HTTP(s) protocol.
%files eps
%{_sbindir}/fence_eps
%{_mandir}/man8/fence_eps.8*

%ifarch x86_64
%package gce
License: GPLv2+ and LGPLv2+
Summary: Fence agent for GCE (Google Cloud Engine)
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description gce
Fence agent for GCE (Google Cloud Engine) instances.
%files gce
%{_sbindir}/fence_gce
%{_mandir}/man8/fence_gce.8*
%endif

%package heuristics-ping
License: GPLv2+ and LGPLv2+
Summary: Pseudo fence agent to affect other agents based on ping-heuristics
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description heuristics-ping
Fence pseudo agent used to affect other agents based on
ping-heuristics.
%files heuristics-ping
%{_sbindir}/fence_heuristics_ping
%{_mandir}/man8/fence_heuristics_ping.8*

%package hpblade
License: GPLv2+ and LGPLv2+
Summary: Fence agent for HP BladeSystem devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description hpblade
Fence agent for HP BladeSystem devices that are accessed via telnet
or SSH.
%files hpblade
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibmblade
Fence agent for IBM BladeCenter devices that are accessed
via the SNMP protocol.
%files ibmblade
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ibm-powervs
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM PowerVS
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-powervs
Fence agent for IBM PowerVS that are accessed via REST API.
%files ibm-powervs
%{_sbindir}/fence_ibm_powervs
%{_mandir}/man8/fence_ibm_powervs.8*

%package ibm-vpc
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM Cloud VPC
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-vpc
Fence agent for IBM Cloud VPC that are accessed via REST API.
%files ibm-vpc
%{_sbindir}/fence_ibm_vpc
%{_mandir}/man8/fence_ibm_vpc.8*

%package ifmib
License: GPLv2+ and LGPLv2+
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ifmib
Fence agent for IF-MIB interfaces that are accessed via
the SNMP protocol.
%files ifmib
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License: GPLv2+ and LGPLv2+
Summary: Fence agents for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo2
Fence agents for HP iLO2 devices that are accessed via
the HTTP(s) protocol.
%files ilo2
%{_sbindir}/fence_ilo
%{_sbindir}/fence_ilo2
%{_mandir}/man8/fence_ilo.8*
%{_mandir}/man8/fence_ilo2.8*

%package ilo-moonshot
License: GPLv2+ and LGPLv2+
Summary: Fence agent for HP iLO Moonshot devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-moonshot
Fence agent for HP iLO Moonshot devices that are accessed
via telnet or SSH.
%files ilo-moonshot
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License: GPLv2+ and LGPLv2+
Summary: Fence agent for HP iLO MP devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-mp
Fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%files ilo-mp
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License: GPLv2+ and LGPLv2+
Summary: Fence agents for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-ssh
Fence agents for HP iLO devices that are accessed via telnet or SSH.
%files ilo-ssh
%{_sbindir}/fence_ilo_ssh
%{_mandir}/man8/fence_ilo_ssh.8*
%{_sbindir}/fence_ilo3_ssh
%{_mandir}/man8/fence_ilo3_ssh.8*
%{_sbindir}/fence_ilo4_ssh
%{_mandir}/man8/fence_ilo4_ssh.8*
%{_sbindir}/fence_ilo5_ssh
%{_mandir}/man8/fence_ilo5_ssh.8*

%package intelmodular
License: GPLv2+ and LGPLv2+
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description intelmodular
Fence agent for Intel Modular interfaces that are accessed
via the SNMP protocol.
%files intelmodular
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipdu
Fence agent for IBM iPDU network power switches that are accessed
via the SNMP protocol.
%files ipdu
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License: GPLv2+ and LGPLv2+
Summary: Fence agents for devices with IPMI interface
Requires: /usr/bin/ipmitool
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipmilan
Fence agents for devices with IPMI interface.
%files ipmilan
%{_sbindir}/fence_ipmilan
%{_mandir}/man8/fence_ipmilan.8*
%{_sbindir}/fence_idrac
%{_mandir}/man8/fence_idrac.8*
%{_sbindir}/fence_ilo3
%{_mandir}/man8/fence_ilo3.8*
%{_sbindir}/fence_ilo4
%{_mandir}/man8/fence_ilo4.8*
%{_sbindir}/fence_ilo5
%{_mandir}/man8/fence_ilo5.8*
%{_sbindir}/fence_ipmilanplus
%{_mandir}/man8/fence_ipmilanplus.8*
%{_sbindir}/fence_imm
%{_mandir}/man8/fence_imm.8*

%package kdump
License: GPLv2+ and LGPLv2+
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common = %{version}-%{release}
# this cannot be noarch since it's compiled
%description kdump
Fence agent for use with kdump crash recovery service.
%files kdump
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%package kubevirt
License: GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Summary: Fence agent for KubeVirt platform
Requires: fence-agents-common = %{version}-%{release}
Provides: bundled(python3-%{openshift}) = %{openshift_version}
Provides: bundled(python3-%{ruamelyamlclib}) = %{ruamelyamlclib_version}
Provides: bundled(python3-%{kubernetes}) = %{kubernetes_version}
Provides: bundled(python3-%{certifi}) = %{certifi_version}
Provides: bundled(python3-%{googleauth}) = %{googleauth_version}
Provides: bundled(python3-%{cachetools}) = %{cachetools_version}
Provides: bundled(python3-%{pyasn1modules}) = %{pyasn1modules_version}
Provides: bundled(python3-%{pyasn1}) = %{pyasn1_version}
Provides: bundled(python3-%{dateutil}) = %{dateutil_version}
Provides: bundled(python3-%{pyyaml}) = %{pyyaml_version}
Provides: bundled(python3-%{six}) = %{six_version}
Provides: bundled(python3-%{urllib3}) = %{urllib3_version}
Provides: bundled(python3-%{websocketclient}) = %{websocketclient_version}
Provides: bundled(python3-%{jinja2}) = %{jinja2_version}
Provides: bundled(python3-%{markupsafe}) = %{markupsafe_version}
Provides: bundled(python3-%{stringutils}) = %{stringutils_version}
Provides: bundled(python3-%{requests}) = %{requests_version}
Provides: bundled(python3-%{chrstnormalizer}) = %{chrstnormalizer_version}
Provides: bundled(python3-%{idna}) = %{idna_version}
Provides: bundled(python3-%{reqstsoauthlib}) = %{reqstsoauthlib_version}
Provides: bundled(python3-%{oauthlib}) = %{oauthlib_version}
Provides: bundled(python3-%{ruamelyaml}) = %{ruamelyaml_version}
Provides: bundled(python3-%{setuptools}) = %{setuptools_version}
%description kubevirt
Fence agent for KubeVirt platform.
%files kubevirt
%{_sbindir}/fence_kubevirt
%{_mandir}/man8/fence_kubevirt.8*
# bundled libraries
%{_usr}/lib/%{name}/support/kubevirt

%package lpar
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM LPAR
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description lpar
Fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%files lpar
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*

%package mpath
License: GPLv2+ and LGPLv2+
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: device-mapper-multipath
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description mpath
Fence agent for SCSI persistent reservation over
Device Mapper Multipath.
%files mpath
%{_sbindir}/fence_mpath
%{_datadir}/cluster/fence_mpath_check*
%{_mandir}/man8/fence_mpath.8*

%ifarch x86_64 ppc64le
%package openstack
License: GPLv2+ and LGPLv2+
Summary: Fence agent for OpenStack's Nova service
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-requests
%else
Requires: python-requests
%endif
Requires: fence-agents-common = %{version}-%{release}
Obsoletes: ha-openstack-support <= %{version}-%{release}
%description openstack
Fence agent for OpenStack's Nova service.
%files openstack
%{_sbindir}/fence_openstack
%{_mandir}/man8/fence_openstack.8*
%endif

%package redfish
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Redfish
Requires: fence-agents-common >= %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-requests
%else
Requires: python-requests
%endif
Obsoletes: fence-agents < 3.1.13
%description redfish
The fence-agents-redfish package contains a fence agent for Redfish
%files redfish
%defattr(-,root,root,-)
%{_sbindir}/fence_redfish
%{_mandir}/man8/fence_redfish.8*

%package rhevm
License: GPLv2+ and LGPLv2+
Summary: Fence agent for RHEV-M
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rhevm
Fence agent for RHEV-M via REST API.
%files rhevm
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%package rsa
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM RSA II
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsa
Fence agent for IBM RSA II devices that are accessed
via telnet or SSH.
%files rsa
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*

%package rsb
License: GPLv2+ and LGPLv2+
Summary: Fence agent for Fujitsu RSB
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsb
Fence agent for Fujitsu RSB devices that are accessed
via telnet or SSH.
%files rsb
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%package sbd
License: GPLv2+ and LGPLv2+
Summary: Fence agent for SBD (storage-based death)
Requires: sbd
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description sbd
Fence agent for SBD (storage-based death).
%files sbd
%{_sbindir}/fence_sbd
%{_mandir}/man8/fence_sbd.8*

%package scsi
License: GPLv2+ and LGPLv2+
Summary: Fence agent for SCSI persistent reservations
Requires: sg3_utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description scsi
Fence agent for SCSI persistent reservations.
%files scsi
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

# skipped from allfenceagents
%package virsh
License: GPLv2+ and LGPLv2+
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients /usr/bin/virsh
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description virsh
Fence agent for virtual machines that are accessed via SSH.
%files virsh
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware-rest
License: GPLv2+ and LGPLv2+
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description vmware-rest
Fence agent for VMWare with REST API.
%files vmware-rest
%{_sbindir}/fence_vmware_rest
%{_mandir}/man8/fence_vmware_rest.8*

%package vmware-soap
License: GPLv2+ and LGPLv2+
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description vmware-soap
Fence agent for VMWare with SOAP API v4.1+.
%files vmware-soap
%{_sbindir}/fence_vmware_soap
%{_mandir}/man8/fence_vmware_soap.8*

%package wti
License: GPLv2+ and LGPLv2+
Summary: Fence agent for WTI Network power switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description wti
Fence agent for WTI network power switches that are accessed
via telnet or SSH.
%files wti
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%ifarch s390x
%package zvm
License: GPLv2+ and LGPLv2+
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common = %{version}-%{release}
%description zvm
Fence agent for IBM z/VM over IP.
%files zvm
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*
%endif

# fence-virt

%ifarch x86_64
%package -n fence-virt
Summary: A pluggable fencing framework for virtual machines
Requires(post):	systemd-sysv %{systemd_units}
Requires(preun):	%{systemd_units}
Requires(postun):	%{systemd_units}
%description -n fence-virt
Fencing agent for virtual machines.
%files -n fence-virt
%doc agents/virt/docs/*
%{_sbindir}/fence_virt
%{_sbindir}/fence_xvm
%{_mandir}/man8/fence_virt.*
%{_mandir}/man8/fence_xvm.*

%package -n fence-virtd
Summary: Daemon which handles requests from fence-virt
%description -n fence-virtd
This package provides the host server framework, fence_virtd,
for fence_virt.  The fence_virtd host daemon is resposible for
processing fencing requests from virtual machines and routing
the requests to the appropriate physical machine for action.
%files -n fence-virtd
%{_sbindir}/fence_virtd
%{_unitdir}/fence_virtd.service
%config(noreplace) %{_sysconfdir}/fence_virt.conf
%dir %{_libdir}/fence-virt
%{_libdir}/fence-virt/vsock.so
%{_mandir}/man5/fence_virt.conf.*
%{_mandir}/man8/fence_virtd.*

%package -n fence-virtd-multicast
Summary:  Multicast listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-multicast
Provides multicast listener capability for fence-virtd.
%files -n fence-virtd-multicast
%{_libdir}/fence-virt/multicast.so

%package -n fence-virtd-serial
Summary:  Serial VMChannel listener for fence-virtd
Requires: libvirt >= 0.6.2
Requires: fence-virtd
%description -n fence-virtd-serial
Provides serial VMChannel listener capability for fence-virtd.
%files -n fence-virtd-serial
%{_libdir}/fence-virt/serial.so

%package -n fence-virtd-tcp
Summary:  TCP listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-tcp
Provides TCP listener capability for fence-virtd.
%files -n fence-virtd-tcp
%{_libdir}/fence-virt/tcp.so

%package -n fence-virtd-libvirt
Summary:  Libvirt backend for fence-virtd
Requires: libvirt >= 0.6.0
Requires: fence-virtd
%description -n fence-virtd-libvirt
Provides fence_virtd with a connection to libvirt to fence
virtual machines.  Useful for running a cluster of virtual
machines on a desktop.
%files -n fence-virtd-libvirt
%{_libdir}/fence-virt/virt.so

%package -n fence-virtd-cpg
Summary:  CPG/libvirt backend for fence-virtd
Requires: corosynclib
Requires: fence-virtd
%description -n fence-virtd-cpg
Provides fence_virtd with a connection to libvirt to fence
virtual machines. Uses corosync CPG to keep track of VM
locations to allow for non-local VMs to be fenced when VMs
are located on corosync cluster nodes.
%files -n fence-virtd-cpg
%{_libdir}/fence-virt/cpg.so
%endif

%changelog
* Thu Jan 18 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-62
- bundled urllib3: fix CVE-2023-45803
  Resolves: RHEL-18139
- bundled pycryptodome: fix CVE-2023-52323
  Resolves: RHEL-20917
- bundled jinja2: fix CVE-2024-22195
  Resolves: RHEL-21345

* Wed Jan  3 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-61
- fence_zvmip: document required user permissions in metadata/manpage
  Resolves: RHEL-14344

* Mon Oct 23 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-60
- all agents: update metadata in non-I/O agents to Power or Network
  fencing
  Resolves: RHEL-14030

* Wed Oct 11 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-57
- bundled urllib3: fix CVE-2023-43804
  Resolves: RHEL-11999

* Wed Sep 27 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-56
- fence_scsi: fix registration handling if ISID conflicts
  Resolves: RHEL-5396
- bundled certifi: fix CVE-2023-37920
  Resolves: RHEL-9446

* Thu Aug  3 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-55
- bundled dateutil: fix tarfile CVE-2007-4559
  Resolves: rhbz#2217902
- fence_ipmilan: fix typos in metadata
  Resolves: rhbz#2224267

* Tue Jul 11 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-48
- fence_ibm_powervs: performance improvements
  Resolves: rhbz#2221643

* Tue Jun 20 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-47
- fence_azure_arm: add Stack Hub support
  Resolves: rhbz#2211930

* Thu May  4 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-46
- fence_scsi: detect devices in shared VGs
  Resolves: rhbz#2187327

* Wed May  3 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-45
- fence_aws: add --skip-race-check parameter to allow running outside
  of AWS network
  Resolves: rhbz#2183162

* Thu Jan 26 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-43
- fence_vmware_soap: set login_timeout lower than default
  pcmk_monitor_timeout (20s) to remove tmp dirs
  Resolves: rhbz#2122944

* Tue Jan 24 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-42
- fencing/fence_wti: add --plug-separator to be able to avoid
  characters that are in node name(s)
  Resolves: rhbz#2152107

* Fri Jan 13 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-41
- fence_scsi: skip key generation during validate-all action
  Resolves: rhbz#2160480

* Fri Dec  2 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-40
- fence_virtd: add info about multiple uuid/ip entries to manpage

  Resolves: rhbz#2149655

* Tue Nov 22 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-39
- fence_virtd: warn if config or key file(s) are not mode 600

  Resolves: rhbz#2144531

* Tue Nov  8 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-37
- Upgrade bundled python-oauthlib
  Resolves: rhbz#2128564

* Mon Oct 31 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-36
- fence_virtd: add link to uri examples and uri w/socket path
  example for when VMS are run as non-root user to manpage
  Resolves: rhbz#2138823

* Tue Oct 25 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-35
- fence_ibm_powervs: improve defaults
  Resolves: rhbz#2136191

* Wed Oct 12 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-34
- fence_lpar: only output additional output info on DEBUG level
  Resolves: rhbz#2134015

* Wed Oct  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-33
- fence_virt: add note that reboot-action doesnt power on nodes that
  are powered off
  Resolves: rhbz#2132008

* Fri Sep  9 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-32
- add azure-identity and dependencies
  Resolves: rhbz#2121546

* Tue Aug 16 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-31
- fence_ibm_vpc: add token cache support
  Resolves: rhbz#2111998

* Tue Aug 16 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-30
- fence_openstack: add support for reading config from clouds.yaml
  and openrc
  Resolves: rhbz#2041933, rhbz#2041935

* Wed Jun 22 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-27
- fence_ibm_powervs: add support for proxy, private API servers and
  get token via API key
  Resolves: rhbz#2093216

* Wed Jun  1 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-26
- fence_ibm_vpc: add proxy support
  Resolves: rhbz#2092385

* Tue May 31 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-25
- all agents: unify ssl parameters to avoid having to use --ssl when
  using --ssl-secure/--ssl-insecure for some agents
  Resolves: rhbz#2072420

* Tue May 17 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-24
- fence_apc/fence_ilo_moonshot: add missing "import logging"
  Resolves: rhbz#2086559

* Thu May  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-23
- fence_ibm_vpc: remove unused instance parameter and make limit
  optional
  Resolves: rhbz#2081235

* Fri Apr 29 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-22
- fence_gce: update fence agent
  Resolves: rhbz#2079889

* Wed Apr  6 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-21
- fence_lpar: refactor to avoid duplicate code
  Resolves: rhbz#2065114

* Wed Mar 30 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-20
- fence_azure_arm: fix sovereign cloud and MSI support
  Resolves: rhbz#2010652

* Mon Mar  7 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-19
- fence_ibm_vpc: new fence agent
  Resolves: rhbz#2061321

* Fri Feb 11 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-18
- fence_zvmip: add SSL/TLS support
  Resolves: rhbz#2022334

* Mon Feb  7 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-17
- fence_ibm_powervs: new fence agent
  Resolves: rhbz#2042496

* Mon Jan 17 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-15
- fence_kubevirt: new fence agent
  Resolves: rhbz#2000954

* Tue Jan 11 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-14
- fence_openstack: add --ssl-insecure
  Resolves: rhbz#2029791

* Thu Dec  2 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-13
- fence_amt_ws: fix "or" causing dead code
  Resolves: rhbz#2010709

* Tue Aug 31 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-9
- Only build fence-virt subpackages for x86_64 arch
  Resolves: rhbz#1965988

* Tue Aug 31 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-8
- OpenStack agents: add dependency
  Resolves: rhbz#1857247

* Wed Aug 25 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-7
- remove suds dependency
  Resolves: rhbz#1989149

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 4.10.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 26 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-2
- new upstream release
  Resolves: rhbz#1984803

* Wed Jul  7 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-5
- Remove "BuildArch: noarch" for arch-specific subpackages
  Resolves: rhbz#1979827

* Fri Jun  4 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-1
- Rebase and add fence-virt subpackages
  Resolves: rhbz#1965988

* Tue May 18 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-10
- remove pexpect dependency
  Resolves: rhbz#1961551

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 4.7.1-9
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 23 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-8
- cloud agents: only build for x86_64

* Thu Mar  4 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-5
- update HA cloud support package

* Mon Feb 15 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-4
- create HA cloud support package

* Thu Feb 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-3
- add aliyun subpackage
- fence-agents-mpath: add missing fence_mpath_check*

* Mon Feb  8 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.1-1
- new upstream release

* Wed Dec  9 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-1
- new upstream release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.5.2-1
- new upstream release
- added openstack subpackage
- spec improvements based on upstream spec-file

* Tue Sep 24 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.5.1-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.4.0-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.3.3-2
- fence-agents-scsi: add missing fence-agents-common dependency

* Mon Dec  3 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.3.3-1
- new upstream release

* Fri Oct  5 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.3.0-1
- new upstream release

* Wed Sep 19 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-6
- Fix missing fence-agents-all subpackage after spec improvements

* Wed Aug 22 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-5
- Python 3: fix has_key() issues

* Mon Aug 20 2018 Jan Pokorný <jpokorny+rpm-booth@fedoraproject.org> - 4.2.1-4
- mark non-compiled packages properly as noarch, restructure excludes
- move azure_fence.py and XenAPI.py to respective subpackages from -common
- sanitize allfenceagents internally defined enumeration
- sanitize BuildRequires with respect to packaging guidelines
- bytecompile native Python modules and ship these bytecodes properly
- only refer to Python binary symbolically, drop buildroot cleanup
- cleanup package summaries/descriptions, order agent subpackages properly

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-2
- fence_vmware_soap: fix python3-suds issue

* Thu May 31 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-1
- new upstream release

* Fri May 25 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-2
- fence_scsi: fix Python 3 encoding issue

* Thu May 17 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-1
- new upstream release

* Thu Feb 15 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-1
- new upstream release
- fence_vmware_soap / fence_ovh: use Python 2 till python3-suds bug
  is fixed

* Fri Feb  9 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.0-2
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.24-14
- Cleanup no longer needed Python 2 dependencies

* Tue Nov 07 2017 Troy Dawson <tdawson@redhat.com> - 4.0.24-13
- Cleanup spec file conditionals

* Tue Aug 29 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-12
- fence-agents-common: remove fence_scsi_check files
- fence-scsi: add "fence_scsi_check_hardreboot"

* Thu Aug  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-10
- fence_zvm: fix "uintptr_t" undeclared

* Thu Aug  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-9
- Fix encoding for pexpect with Python 3.6
  Resolves: rhbz#1473908

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-5
- Fix to build in Python 3 only environment

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.24-4
- Rebuild for Python 3.6

* Wed Sep 21 2016 Marek Grac <mgrac@redhat.com> - 4.0.24-4
- Remove Obsoletes that are no longer valid

* Fri Sep  2 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-2
- fence-agents-common: add dependency on python3-pycurl

* Fri Aug 26 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-1
- new upstream release

* Wed Jul 13 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-2
- fix build issue on s390

* Tue Jul 12 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-1
- new upstream release
- new package fence-agents-amt-ws
- new package fence-agents-compute
- new package fence-agents-drac
- new package fence-agents-hds-cb
- new package fence-agents-mpath
- new package fence-agents-sanbox2
- new package fence-agents-sbd
- new package fence-agents-vbox
- new package fence-agents-vmware
- new package fence-agents-xenapi

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Marek Grac <mgrac@redhat.com> - 4.0.20-1
- new upstream release
- new package fence-agents-rcd-serial

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.16-1
- new upstream release

* Mon Feb 09 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-1
- new upstream release

* Thu Jan 08 2015 Marek Grac <mgrac@redhat.com> - 4.0.14-1
- new upstream release
- new packages fence-agents-zvm and fence-agents-emerson

* Thu Oct 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.12-1
- new upstream release
- new package fence-agents-ilo-ssh

* Wed Aug 27 2014 Marek Grac <mgrac@redhat.com> - 4.0.10
- new upstream release
- new package fence-agents-ilo-moonshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.9
- new upstream release
- new package fence-agents-pve

* Mon Apr 07 2014 Marek Grac <mgrac@redhat.com> - 4.0.8-1
- new upstream release
- new package fence-agents-raritan

* Wed Feb 26 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-3
- requires a specific version of fence-agents-common

* Mon Feb 17 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-2
- new upstream release
- changed dependancy from nss/nspr to gnutls-utils

* Fri Jan 10 2014 Marek Grac <mgrac@redhat.com> - 4.0.4-4
- new upstream release
- new package fence-agents-amt

* Mon Oct 07 2013 Marek Grac <mgrac@redhat.com> - 4.0.4-3
- new upstream release
- new package fence-agents-netio

* Tue Sep 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.3-1
- new upstream release
- new packages fence-agents-brocade and fence-agents-ovh

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.0.1-2
- Perl 5.18 rebuild

* Mon Jul 01 2013 Marek Grac <mgrac@redhat.com> - 4.0.1-1
- new upstream release

* Mon Jun 24 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-5
- fence-agents-all should provide fence-agent for clean update path

* Wed Apr 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-4
- minor changes in spec file

* Thu Mar 21 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-3
- minor changes in spec file

* Mon Mar 18 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-2
- minor changes in spec file

* Mon Mar 11 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-1
- new upstream release
- introducing subpackages


