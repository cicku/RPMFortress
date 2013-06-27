Name:           mylvmbackup
Version:        0.14
Release:        1%{?dist}
Summary:        Utility for creating MySQL backups via LVM snapshots
License:        GPLv2
URL:            http://www.lenzg.net/mylvmbackup/
Source0:        http://www.lenzg.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  perl
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

%description
mylvmbackup is a tool for quickly creating full physical backups of a MySQL 
server's data files. To perform a backup, mylvmbackup obtains a read lock on 
all tables and flushes all server caches to disk, makes an LVM snapshot of 
the volume containing the MySQL data directory, and unlocks the tables again. 
The snapshot process takes only a small amount of time. When it is done, the 
server can continue normal operations, while the actual file backup proceeds.

%prep
%setup -q
sed -i 's|/usr/bin/install|/usr/bin/install -p|g' Makefile

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}

%files
%doc ChangeLog COPYING CREDITS README TODO
%dir %{_datadir}/%{name}
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_datadir}/%{name}/*.pm
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Tue Jun 25 2013 Christopher Meng <rpm@cicku.me> - 0.14-1
- Rebuild for Fedora
