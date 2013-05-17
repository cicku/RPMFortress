Name:              twcbackup
Version:           1.0.0
Release:           1%{?dist}
Summary:           A flexible, easy to configure backup software
URL:               http://space.twc.de/~stefan/twcbackup
Source0:           http://space.twc.de/~stefan/%{name}/%{name}-%{version}.tar.bz2
License:           GPLv3

BuildArch:         noarch
smokegen
Requires:          smokeqt
Requires:          perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
twcbackup is a backup software which is usually configured to run once every 
night. During this nightly backup run, it automatically determines which 
files have been changed, and adds these to the backup pool.

%prep
%setup -q

%build
%configure
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/*.1*

%changelog
* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- Initial Package.
