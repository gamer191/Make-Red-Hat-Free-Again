#!/usr/bin/bash
MDADM=/sbin/mdadm
DEVNAME=$1

export $(${MDADM} --examine --export ${DEVNAME})
if [ -z "${MD_UUID}" ]; then
     exit 1
fi

UUID_LINK=$(readlink /dev/disk/by-id/md-uuid-${MD_UUID})
MD_DEVNAME=${UUID_LINK##*/}
export $(${MDADM} --detail --export /dev/${MD_DEVNAME})
if [ -z "${MD_METADATA}" ] ; then
     exit 1
fi
 
${MDADM} --manage /dev/${MD_DEVNAME} --re-add ${DEVNAME} --verbose  
