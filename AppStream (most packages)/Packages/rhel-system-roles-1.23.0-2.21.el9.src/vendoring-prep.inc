# Untar vendored collection tarballs to corresponding directories
for file in %{SOURCE801} %{SOURCE901} %{SOURCE902}; do
    if [[ "$(basename $file)" =~ ([^-]+)-([^-]+)-(.+).tar.gz ]]; then
        ns=${BASH_REMATCH[1]}
        name=${BASH_REMATCH[2]}
        ver=${BASH_REMATCH[3]}
        mkdir -p .external/$ns/$name
        pushd .external/$ns/$name > /dev/null
        tar xfz "$file"
        popd > /dev/null
    fi
done
