%global fontname julietaula-montserrat
%global fontconf 61-%{fontname}
%global common_description %{expand: 
A typeface inspired by signs around the Montserrat area \
of Buenos Aires, Argentina.}

Name:		%{fontname}-fonts
Version:	7.210
Release:	6%{?dist}
# Override versioning to sync with upstream
Epoch:		1
Summary:	Sans-serif typeface inspired from Montserrat area

License:	OFL
URL:		https://github.com/JulietaUla/Montserrat
Source0:	%{url}/releases/download/v%{version}/Montserrat-%{version}.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{name}-alternates-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}-alternates.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

# Reset the old date based versioning
Obsoletes:	%{name} < 1:%{version}-%{release}


%description
%{common_description}

%package common
Summary:  Common files for %{name}
Requires: fontpackages-filesystem

%description common
%{common_description}
This package consists of files used by other %{name} packages.

%package	-n %{fontname}
Summary:	Base version of the Montserrat area inspired typeface
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n %{fontname}
%{common_description}
This package provide the base fonts.

%package 	-n %{fontname}-alternates-fonts
Summary:	A Montserrat area inspired typeface family alternate version
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n %{fontname}-alternates-fonts
%{common_description}
This package provide an alternate version of the fonts.

%package	-n %{fontname}-base-web-fonts
Summary:	Web fonts version of the Montserrat area inspired typeface
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n %{fontname}-base-web-fonts
%{common_description}
This package include essential web fonts.

%package	-n %{fontname}-extra-web-fonts
Summary:	Extra web fonts version of the Montserrat area inspired typeface
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n %{fontname}-extra-web-fonts
%{common_description}
This package includes extra web fonts.

%prep
%autosetup -c

%build


%install
install -Dpm 0644 Montserrat-%{version}/fonts/otf/*.otf -t %{buildroot}%{_fontdir}
install -m 0644 -p Montserrat-%{version}/fonts/webfonts/*.woff %{buildroot}%{_fontdir}
install -m 0644 -p Montserrat-%{version}/fonts/webfonts/*.woff2 %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Install Montserrat fonts
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

# Install MontserratAlternates fonts
install -m 0644 -p %{SOURCE2} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-alternates.conf

for fconf in %{fontconf}.conf \
	     %{fontconf}-alternates.conf ; do
	ln -s %{_fontconfig_templatedir}/$fconf \
		%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata file, Repeat for every font family
install -Dm 0644 -p %{SOURCE3} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml

%_font_pkg -f %{fontconf}.conf Montserrat-*.otf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%_font_pkg -n alternates -f %{fontconf}-alternates.conf MontserratAlternates-*.otf
%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml
%_font_pkg -n base-web Montserrat-{Regular,Light,Bold,ExtraBold,Italic}.{woff,woff2}
%_font_pkg -n extra-web Montserrat*.{woff,woff2}

%files common
%license Montserrat-%{version}/OFL.txt
%doc Montserrat-%{version}/README.md 

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:7.210-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:7.210-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Mar 05 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1:7.210-4
- Add base and extra subpackage web fonts for Design Team

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.210-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1:7.210-1
- Update to 7.210

* Wed May 13 2020 Troy Dawson <tdawson@redhat.com> - 1:7.200-9
- Minor conditional tweaks for ELN

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1:7.200-5
- Add missing epoch for dependencies rhbz#1643607
- Shorten the description

* Sat Oct 20 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-4
- Update spec file adhering to Fedora Fonts guideline rhbz#1628832

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:7.200-1
- Upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:6.002-2
- Fix obsolete tag

* Mon May 15 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:6.002-1
- Use Epoch to sync version with upstream
- Latest stable upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:20151221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-5
- Improved appstream file with fonts list

* Sun Mar 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-4
- Fixed compatibility issue with Fedora 22 and EPEL7 less

* Fri Mar 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-3
- Switched doc section to license
- Deleted oft and ttf subdirectories

* Fri Mar 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-2
- Moved appstream-util to check section

* Thu Mar 24 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-1
- Initial build
