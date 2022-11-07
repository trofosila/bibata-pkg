Name:       bibata-test
Version:    2.0.2
Release:    7%{?dist}
Summary:    Most simple RPM package
License:    GPLv3+
URL:        https://github.com/ful1e5/Bibata_Cursor
Source0:    https://github.com/ful1e5/Bibata_Cursor/releases/download/v%{version}/Bibata.tar.gz
BuildArch:  noarch

%description
This is my first RPM package, which does nothing.

%prep
%setup -c

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
%__mv Bibata-Original-Amber %{buildroot}%{_datadir}/icons
%__chmod 0755 %{buildroot}%{_datadir}/icons/Bibata-Original-Amber

%clean
%__rm -rf %{buildroot}

%files
%{_datadir}/icons/*

%changelog
# let's skip this for now