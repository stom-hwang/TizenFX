Name:       csapi-multimedia
Summary:    Tizen Multimedia API for C#
Version:    1.0.26
Release:    0
Group:      Development/Libraries
License:    Apache-2.0
URL:        https://www.tizen.org
Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}.manifest

AutoReqProv: no
ExcludeArch: aarch64 %ix86

BuildRequires: dotnet-build-tools

# C# API Requires
BuildRequires: csapi-tizen-nuget
BuildRequires: csapi-application-nuget
BuildRequires: elm-sharp-nuget

%define Assemblies Tizen.Multimedia

%description
%{summary}

%dotnet_import_sub_packages

%prep
%setup -q
cp %{SOURCE1} .

%build
for ASM in %{Assemblies}; do
%dotnet_build $ASM
%dotnet_pack $ASM/$ASM.nuspec %{version}
done

%install
for ASM in %{Assemblies}; do
%dotnet_install $ASM
done

%files
%manifest %{name}.manifest
%license LICENSE
%attr(644,root,root) %{dotnet_assembly_files}
