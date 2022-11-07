Name:       bibata-test
Version:    2.0.2
Release:    5%{?dist}
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
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
# let's skip this for now