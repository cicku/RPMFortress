Name:            pcapfix
Version:         0.7.3
Release:         1%{?dist}
Summary:         A tool for repairing corrupted pcap files
License:         GPLv3+
URL:             http://f00l.de/pcapfix
Source0:         http://f00l.de/pcapfix/%{name}-%{version}.tar.gz

%description
pcapfix is a repair tool for corrupted pcap files. It checks for an intact pcap
global header and repairs it if there are any corrupted bytes. If one is not
present, one is created and added to the beginning of the file. It then tries
to find pcap packet headers, and checks and repairs them.

%prep
%setup -q
sed -i 's|install -D|install -p -D|g' Makefile

%build
make CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot}

%files
%doc Changelog LICENSE README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jun 18 2013 Christopher Meng <rpm@cicku.me> - 0.7.3-1
- Initial package.
