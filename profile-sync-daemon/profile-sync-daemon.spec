%global aname psd

Name:         profile-sync-daemon 
Version:      5.36
Release:      1%{?dist}
Summary:      Offload browser profiles to RAM for speed a wear reduction
License:      MIT
URL:          https://github.com/graysky2/profile-sync-daemon 
Source0:      https://github.com/graysky2/%{name}/archive/v%{version}.tar.gz

BuildArch:    noarch
Requires:     rsync

%description
Symlinks and syncs browser profiles to RAM via tmpfs which will reduce HDD/SDD
calls and speed-up browsers.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install-systemd-all DESTDIR=%{buildroot}

%post
# http://fedoraproject.org/wiki/PackagingDrafts/ScriptletSnippets
# clean install is where $1 == 1
if [ $1 -eq 1 ]; then 
setsebool -P rsync_full_access 1 >/dev/null 2>&1 || :
fi
# upgrade is where $1 == 2

%preun
# http://fedoraproject.org/wiki/PackagingDrafts/ScriptletSnippets
# clean unisntall is where $1 == 0
if [ $1 -eq 0 ]; then
	if [ -f /run/psd ]; then
		systemctl stop psd.service
	fi
setsebool -P rsync_full_access 0 >/dev/null 2>&1 || :
fi
# upgrade is where $1 == 1

%files
%doc CHANGELOG MIT
%config(noreplace) %{_sysconfdir}/%{aname}.conf
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_unitdir}/%{aname}*.*

%changelog
* Wed Jun 05 2013 Christopher Meng <rpm@cicku.me> - 5.36-1
- New upstream release.

* Wed May 29 2013 Christopher Meng <rpm@cicku.me> - 5.35-1
- Initial Package.
