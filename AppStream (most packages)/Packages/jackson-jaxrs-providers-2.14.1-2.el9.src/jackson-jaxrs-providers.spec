%bcond_without  jp_minimal

Name:           jackson-jaxrs-providers
Version:        2.14.1
Release:        2%{?dist}
Summary:        Jackson JAX-RS providers
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-jaxrs-providers
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%if %{without jp_minimal}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(org.glassfish.jersey.containers:jersey-container-servlet)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-server)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)
%endif

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

%package -n pki-%{name}
Summary:        Jackson JAX-RS providers
Obsoletes:      %{name} < %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%if %{with jp_minimal}
Obsoletes:      jackson-jaxrs-cbor-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-smile-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-xml-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-yaml-provider < 2.10.0-1
%endif

%description -n pki-%{name}
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

%package -n pki-jackson-jaxrs-json-provider
Summary:       Jackson-JAXRS-JSON
Obsoletes:     jackson-jaxrs-json-provider < %{version}-%{release}
Conflicts:     jackson-jaxrs-json-provider < %{version}-%{release}
Provides:      jackson-jaxrs-json-provider = %{version}-%{release}

%description -n pki-jackson-jaxrs-json-provider
Functionality to handle JSON input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%if %{without jp_minimal}
%package -n pki-jackson-jaxrs-cbor-provider
Summary:       Jackson-JAXRS-CBOR
Obsoletes:     jackson-jaxrs-cbor-provider < %{version}-%{release}
Conflicts:     jackson-jaxrs-cbor-provider < %{version}-%{release}
Provides:      jackson-jaxrs-cbor-provider = %{version}-%{release}

%description -n pki-jackson-jaxrs-cbor-provider
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n pki-jackson-jaxrs-smile-provider
Summary:       Jackson-JAXRS-Smile
Obsoletes:     jackson-jaxrs-smile-provider < %{version}-%{release}
Conflicts:     jackson-jaxrs-smile-provider < %{version}-%{release}
Provides:      jackson-jaxrs-smile-provider = %{version}-%{release}

%description -n pki-jackson-jaxrs-smile-provider
Functionality to handle Smile (binary JSON) input/output for
JAX-RS implementations (like Jersey and RESTeasy) using standard
Jackson data binding.

%package -n pki-jackson-jaxrs-xml-provider
Summary:       Jackson-JAXRS-XML
Obsoletes:     jackson-jaxrs-xml-provider < %{version}-%{release}
Conflicts:     jackson-jaxrs-xml-provider < %{version}-%{release}
Provides:      jackson-jaxrs-xml-provider = %{version}-%{release}

%description -n pki-jackson-jaxrs-xml-provider
Functionality to handle Smile XML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n pki-jackson-jaxrs-yaml-provider
Summary:       Jackson-JAXRS-YAML
Obsoletes:     jackson-jaxrs-yaml-provider < %{version}-%{release}
Conflicts:     jackson-jaxrs-yaml-provider < %{version}-%{release}
Provides:      jackson-jaxrs-yaml-provider = %{version}-%{release}

%description -n pki-jackson-jaxrs-yaml-provider
Functionality to handle YAML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.
%endif

%package -n pki-%{name}-datatypes
Summary: Functionality for reading/writing core JAX-RS helper types
Obsoletes:     %{name}-datatypes < %{version}-%{release}
Conflicts:     %{name}-datatypes < %{version}-%{release}
Provides:      %{name}-datatypes = %{version}-%{release}

%description -n pki-%{name}-datatypes
Functionality for reading/writing core JAX-RS helper types.

%package -n pki-%{name}-parent
Summary: Parent for Jackson JAX-RS providers
Obsoletes:     %{name}-parent < %{version}-%{release}
Conflicts:     %{name}-parent < %{version}-%{release}
Provides:      %{name}-parent = %{version}-%{release}

%description -n pki-%{name}-parent
Parent POM for Jackson JAX-RS providers.

%package -n pki-%{name}-javadoc
Summary: Javadoc for %{name}
Obsoletes:     %{name}-javadoc < %{version}-%{release}
Conflicts:     %{name}-javadoc < %{version}-%{release}
Provides:      %{name}-javadoc = %{version}-%{release}

%description -n pki-%{name}-javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p xml/src/main/resources/META-INF/LICENSE .
cp -p xml/src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%pom_remove_plugin -r :moditect-maven-plugin
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"

# Disable jar with no-meta-inf-services classifier, breaks build
%pom_remove_plugin :maven-jar-plugin cbor
%pom_remove_plugin :maven-jar-plugin json
%pom_remove_plugin :maven-jar-plugin smile
%pom_remove_plugin :maven-jar-plugin xml
%pom_remove_plugin :maven-jar-plugin yaml
%pom_remove_plugin :maven-jar-plugin datatypes

# Replace jakarta-ws-rs with jboss-jaxrs-2.0-api
%pom_change_dep javax.ws.rs:javax.ws.rs-api org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec

# Add missing deps to fix java.lang.ClassNotFoundException during tests
%pom_add_dep com.google.guava:guava:18.0:test datatypes cbor json smile xml yaml
%pom_add_dep org.ow2.asm:asm:5.1:test cbor json smile xml yaml

# Circular dep?
%pom_remove_dep org.jboss.resteasy:resteasy-jackson2-provider json
rm json/src/test/java/com/fasterxml/jackson/jaxrs/json/resteasy/RestEasyProviderLoadingTest.java

%if %{with jp_minimal}
# Disable extra test deps
%pom_remove_dep org.glassfish.jersey.core:
%pom_remove_dep org.glassfish.jersey.containers:
# Disable extra providers
%pom_disable_module cbor
%pom_disable_module smile
%pom_disable_module xml
%pom_disable_module yaml
%endif

%build
%if %{with jp_minimal}
%mvn_build -s -f
%else
%mvn_build -s
%endif

%install
%mvn_install

%files -n pki-%{name} -f .mfiles-jackson-jaxrs-base
%doc README.md release-notes/*
%license LICENSE NOTICE

%files -n pki-jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider
%if %{without jp_minimal}
%files -n pki-jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider
%files -n pki-jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider
%files -n pki-jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider
%files -n pki-jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider
%endif

%files -n pki-%{name}-datatypes -f .mfiles-jackson-datatype-jaxrs
%license LICENSE NOTICE

%files -n pki-%{name}-parent -f .mfiles-jackson-jaxrs-providers
%license LICENSE NOTICE

%files -n pki-%{name}-javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Nov 23 2022 Chris Kelley <ckelley@redhat.com> - 2.14.1-1
- Update to version 2.14.1
- Resolves: #2070122

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.11.4-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 30 2021 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.11.4-6
- Replace jakarta-ws-rs with jboss-jaxrs-2.0-api

* Wed Apr 28 2021 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.11.4-5
- Add Obsoletes and Conflicts

* Thu Apr 22 2021 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.11.4-4
- Rename subpackages to pki-jackson

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.11.4-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Fabio Valentini <decathorpe@gmail.com> - 2.11.4-1
- Update to version 2.11.4.

* Wed Oct 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.3-1
- Update to version 2.11.3.

* Sat Aug 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.2-1
- Update to version 2.11.2.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.11.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jul 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.1-1
- Update to version 2.11.1.

* Mon May 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.0-1
- Update to version 2.11.0.

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.4-1
- Update to version 2.10.4.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.3-1
- Update to version 2.10.3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.2-1
- Update to version 2.10.2.

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.10.1-1
- Update to version 2.10.1.

* Tue Nov 12 2019 Alexander Scheel <ascheel@redhat.com> - 2.10.0-2
- Minimize build dependencies.

* Sun Oct 27 2019 Fabio Valentini <decathorpe@gmail.com> - 2.10.0-1
- Update to version 2.10.0.
- Build with minimized dependencies.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Mat Booth <mat.booth@redhat.com> - 2.9.8-1
- Update to latest upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-4
- Allow conditional building of modules that have extra deps

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-1
- Update to latest upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 2.7.6-1
- update to 2.7.6

* Fri Jun 24 2016 gil cattaneo <puntogil@libero.it> 2.6.7-1
- update to 2.6.7

* Thu May 26 2016 gil cattaneo <puntogil@libero.it> 2.6.6-1
- update to 2.6.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 gil cattaneo <puntogil@libero.it> 2.6.3-1
- update to 2.6.3

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5.0-1
- update to 2.5.0

* Sat Sep 20 2014 gil cattaneo <puntogil@libero.it> 2.4.2-1
- update to 2.4.2

* Wed Jul 09 2014 gil cattaneo <puntogil@libero.it> 2.4.1-2
- enable jackson-jaxrs-cbor-provider

* Fri Jul 04 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- update to 2.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.2-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Jul 17 2013 gil cattaneo <puntogil@libero.it> 2.2.2-1
- update to 2.2.2
- renamed jackson-jaxrs-providers

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.1.5-1
- update to 2.1.5

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 2.1.0-1
- update to 2.1.0
- renamed jackson2-jaxrs-json-provider

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 2.0.5-1
- initial rpm
