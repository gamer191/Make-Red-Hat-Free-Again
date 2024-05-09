# maps the source file to the roles that use that file
# value can be string or space delimited list of strings
# role name `__collection` means - do not vendor into
# role, just vendor directly into the collection
declare -A plugin_map=(
  [ansible/posix/plugins/modules/selinux.py]=selinux
  [ansible/posix/plugins/modules/seboolean.py]=selinux
  [ansible/posix/plugins/modules/mount.py]=storage
  [ansible/posix/plugins/modules/rhel_facts.py]=__collection
  [ansible/posix/plugins/modules/rhel_rpm_ostree.py]=__collection
  [ansible/posix/plugins/module_utils/mount.py]=storage
  [community/general/plugins/modules/ini_file.py]="tlog ad_integration"
  [community/general/plugins/modules/modprobe.py]=ha_cluster
  [community/general/plugins/modules/redhat_subscription.py]=rhc
  [community/general/plugins/modules/rhsm_release.py]=rhc
  [community/general/plugins/modules/rhsm_repository.py]=rhc
  [community/general/plugins/modules/seport.py]=selinux
  [community/general/plugins/modules/sefcontext.py]=selinux
  [community/general/plugins/modules/selogin.py]=selinux
  [containers/podman/plugins/modules/podman_container_info.py]=podman
  [containers/podman/plugins/modules/podman_image.py]=podman
  [containers/podman/plugins/modules/podman_play.py]=podman
  [containers/podman/plugins/modules/podman_secret.py]=podman
  [containers/podman/plugins/module_utils/podman/common.py]=podman
)

declare -a modules mod_utils collection_plugins
declare -A dests
# vendor in plugin files - fix documentation, fragments
for src in "${!plugin_map[@]}"; do
  roles="${plugin_map["$src"]}"
  if [ "$roles" = __collection ]; then
    collection_plugins+=("$src")
  else
    case "$src" in
    */plugins/modules/*) srcdir=plugins/modules; subdir=library; modules+=("$src") ;;
    */plugins/module_utils/*) srcdir=plugins/module_utils; mod_utils+=("$src") ;;
    */plugins/action/*) srcdir=plugins/action ;;
    esac
  fi
  for role in $roles; do
    if [ "$role" = __collection ]; then
      dest="%{collection_build_path}/plugins${src/#*plugins/}"
      dests["$dest"]=__collection
    else
      case "$src" in
      */plugins/module_utils/*) subdir="module_utils/${role}_lsr" ;;
      esac
      dest="$role/${src/#*${srcdir}/${subdir}}"
      dests["$dest"]="$role"
    fi
    destdir="$(dirname "$dest")"
    if [ ! -d "$destdir" ]; then
      mkdir -p "$destdir"
    fi
    cp -pL ".external/$src" "$dest"
    sed -e ':a;N;$!ba;s/description:\n\( *\)/description:\n\1- WARNING: Do not use this plugin directly! It is only for role internal use.\n\1/' \
      -e '/^extends_documentation_fragment:/,/^[^ -]/{/^extends/d;/^[ -]/d}' \
      -i "$dest"
  done
done

# remove the temporary .external directory after vendoring
rm -rf .external

# fix python imports to point from the old name to the new name
for dest in "${!dests[@]}"; do
  role="${dests["$dest"]}"
  for module in "${modules[@]}"; do
    python_name="$(dirname "$module")"
    python_name="${python_name////[.]}"
    sed -e "s/ansible_collections[.]${python_name}[.]/ansible.modules./" -i "$dest"
  done
  for mod_util in "${mod_utils[@]}"; do
    # some mod_utils have subdirs, some do not
    split=(${mod_util//// })
    python_name="ansible_collections[.]${split[0]}[.]${split[1]}[.]plugins[.]module_utils[.]"
    sed -e "s/${python_name}/ansible.module_utils.${role}_lsr./" -i "$dest"
  done
  for plugin in "${collection_plugins[@]}"; do
    python_name="$(dirname "$plugin")"
    dest_python_name="%{collection_namespace}/%{collection_name}/plugins${python_name/#*plugins/}"
    src_python_name="ansible_collections.${python_name////[.]}"
    dest_python_name="ansible_collections.${dest_python_name////.}"
    sed -e "s/${src_python_name}/${dest_python_name}/" -i "$dest"
  done
done

# Replacing "linux-system-roles.rolename" with "rhel-system-roles.rolename" in each role
# Replacing "fedora.linux_system_roles." with "redhat.rhel_system_roles" in each role
# This is for the "roles calling other roles" case
# for podman, change the FQCN - using a non-FQCN module name doesn't seem to work,
# even for the legacy role format
for rolename in %{rolenames}; do
    find "$rolename" -type f -exec \
         sed -e "s/linux-system-roles[.]${rolename}\\>/%{roleinstprefix}${rolename}/g" \
             -e "s/fedora[.]linux_system_roles[.]/%{collection_namespace}.%{collection_name}./g" \
             -e "s/containers[.]podman[.]/%{collection_namespace}.%{collection_name}./g" \
             -e "s/community[.]general[.]/%{collection_namespace}.%{collection_name}./g" \
             -e "s/ansible[.]posix[.]/%{collection_namespace}.%{collection_name}./g" \
             -i {} \;
done
