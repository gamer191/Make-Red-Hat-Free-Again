%{?nodejs_find_provides_and_requires}
%global npm_name nodemon

# Disable until dependencies are met
%global enable_tests 0

Name:          nodejs-%{npm_name}
Version:       2.0.20
Release:       3%{?dist}
Summary:       Simple monitor script for use during development of a node.js app
License:       MIT
URL:           https://www.npmjs.com/package/nodemon
Source0:       %{npm_name}-v%{version}-bundled.tar.gz

Patch1:        0001-deps-glob-parent-Resolve-ReDoS-vulnerability-from-CV.patch

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm

ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Simple monitor script for use during development of a node.js app.

For use during development of a node.js based application.

nodemon will watch the files in the directory in which nodemon
was started, and if any files change, nodemon will automatically
restart your node application.

nodemon does not require any changes to your code or method of
development. nodemon simply wraps your node application and keeps
an eye on any files that have changed. Remember that nodemon is a
replacement wrapper for node, think of it as replacing the word "node"
on the command line when you run your script.

%prep
%autosetup -p1 -n package

%build

# nothing to do
# tarball is bundled in --production mode, so no need to prune

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr doc bin lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/nodemon.js %{buildroot}%{_bindir}/nodemon

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
npm run test
%endif

%files
%doc doc README.md
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/nodemon

%changelog
* Mon Mar 27 2023 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.20-3
- Patch bundled glob-parent
- Resolves: CVE-2021-35065

* Thu Dec 08 2022 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.20-2
- Record CVE fixed in the current or previous upstream versions
- Resolves: CVE-2021-44906

* Fri Nov 18 2022 Jan Staněk <jstanek@redhat.com> - 2.0.20-1
- Rebase to 2.0.20
  Resolves: CVE-2022-3517

* Wed Aug 31 2022 Jan Staněk <jstanek@redhat.com> - 2.0.19-1
- Rebase to 2.0.19
  Resolves: CVE-2022-33987 rhbz#2073156 CVE-2021-33502 CVE-2021-3807 CVE-2020-28469
  Resolves: CVE-2020-7788

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.3-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 22 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.3-5
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.3-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 01 2020 Honza Horak <hhorak@redhat.com> - 2.0.3-1
- Update to 2.0.3

* Mon Aug 13 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.18.3-1
- Resolves: #1615413
- Updated
- bundled

* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.11.0-2
- rh-nodejs8 rebuild

* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.11.0-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.1-6
- rebuilt

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 1.8.1-5
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 1.8.1-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.8.1-1
- Initial package
