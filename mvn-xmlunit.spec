#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xmlunit
Version  : 1.5
Release  : 4
URL      : https://repo1.maven.org/maven2/xmlunit/xmlunit/1.5/xmlunit-1.5.jar
Source0  : https://repo1.maven.org/maven2/xmlunit/xmlunit/1.5/xmlunit-1.5.jar
Source1  : https://repo1.maven.org/maven2/xmlunit/xmlunit/1.5/xmlunit-1.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-xmlunit-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-xmlunit package.
Group: Data

%description data
data components for the mvn-xmlunit package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5/xmlunit-1.5.jar
/usr/share/java/.m2/repository/xmlunit/xmlunit/1.5/xmlunit-1.5.pom
