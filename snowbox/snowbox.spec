Name:              snowbox
Version:           2.0.1
Release:           1%{?dist}
Summary:           A POP3 server written in Go

License:           GPLv3+
URL:               https://kiza.eu/software/snowbox/
Source0:           https://kiza.eu/media/software/snowbox/%{name}-%{version}.tar.gz
Source1:           %{name}.service

BuildRequires:     gcc-go
BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Snowbox is a POP3 server written in Go.

Features:
- Written in a secure language
- APOP authentication
- SSL support
- IPv6
- Small codebase (800 lines)
- Easy setup

%prep
%setup -q
gzip %{name}.8
sed -i 's|/usr/local|%{_prefix}|g' Makefile
sed -i 's|go build|gccgo|g' Makefile

%build
make %{?_smp_mflags}

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 600 config %{buildroot}%{_sysconfdir}/%{name}/config
install -p -D -m 600 user.auth %{buildroot}%{_sysconfdir}/%{name}/user.auth
install -p -D -m 644 %{name}.8.gz %{buildroot}%{_mandir}/man8/%{name}.8.gz
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc AUTHOR changelog COPYING README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/user.auth 
%{_bindir}/%{name}
%{_mandir}/man8/*.8*
%{_unitdir}/%{name}.service

%changelog
* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 2.0.1-1
- Initial Package.
