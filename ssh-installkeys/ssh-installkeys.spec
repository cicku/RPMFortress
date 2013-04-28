Name:              ssh-installkeys
Version:           1.8
Release:           1%{?dist}
Summary:           A tool for installing ssh keys on remote sites
License:           BSD
URL:               http://www.catb.org/~esr/ssh-installkeys/
Source0:           http://www.catb.org/~esr/ssh-installkeys/%{name}-%{version}.tar.gz

BuildRequires:     xmlto
Requires:          python

%description
This script tries to export ssh public keys to a specified site.  It will
walk you through generating key pairs if it doesn't find any to export.
It handles all the fiddly details like making sure local and remote
permissions are correct, and tells you what it's doing if it has to change
anything.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me> - 1.8-1
- Initial Package.
