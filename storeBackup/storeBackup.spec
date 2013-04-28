Name:              storeBackup
Version:           3.3.1
Release:           1%{?dist}
Summary:           A very space efficient disk-to-disk backup suite 

Url:               http://storebackup.org
License:           GPLv3+

Source0:           http://download.savannah.gnu.org/releases/%{name}/%{name}-3.3.1.tar.bz2

BuildArch:         noarch

Requires:          bzip2
Requires:          coreutils
Requires:          e2fsprogs
Requires:          perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

AutoReq:           no

%description 
storeBackup is a backup utility that stores files on other disks. 
It's able to compress data, and recognize copying and moving of files 
and directories (deduplication), and unifies the advantages of 
traditional full and incremental backups. It can handle big image files 
with block-wise changes efficiently. Depending on its contents, 
every file is stored only once on disk. Tools for analyzing 
backup data and restoring are provided. Once archived, files 
are accessible by mounting file systems (locally, or via Samba or NFS). 
It is easy to install and configure. Additional features are 
backup consistency checking, offline backups, and replication of backups.

%prep
%setup -q -n %{name}

sed -i 's|/usr/bin/env perl|/usr/bin/perl|g' bin/*

%build

%install
mv bin/%{name}.pl bin/%{name}
install -d %{buildroot}%{_libdir}/
install -d %{buildroot}%{_bindir}/
cp -r bin/* %{buildroot}%{_bindir}/
cp -r lib/* %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 man/man1/*.1 %{buildroot}%{_mandir}/man1
ln -s %{_mandir}/man1/%{name}.pl.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/* cron-storebackup
%{_mandir}/man1/*.1*
%{_libdir}/*
%{_bindir}/*

%changelog
* Sat Apr 27 2013 Christopher Meng <rpm@cicku.me> - 3.3.1-1
- Initial Package.
