Name:              darkhttpd
Version:           1.9
Release:           2%{?dist}
Summary:           A secure, lightweight, fast, single-threaded HTTP/1.1 server
License:           BSD

URL:               http://unix4lyfe.org/darkhttpd/
Source0:           http://unix4lyfe.org/%{name}/%{name}-%{version}.tar.bz2
Source1:           %{name}.service
Source2:           %{name}.sysconfig

%description
darkhttpd is a secure, lightweight, fast, single-threaded HTTP/1.1 server.

Features:
Simple to set up.
Single binary, no other files, no installation needed.
Standalone, doesn't need inetd or ucspi-tcp.
No messing around with config files - all you have to specify is the www root.
Written in C - efficient and portable.
Small memory footprint.
Event loop, single threaded - no fork() or pthreads.
Generates directory listings.
Supports HTTP GET and HEAD requests.
Supports Range / partial content.
Supports If-Modified-Since.
Supports Keep-Alive connections.
Can serve 301 redirects based on Host header.
Uses sendfile() on FreeBSD, Solaris and Linux.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%files
%doc README
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 1.9-2
- Add systemd support.

* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 1.9-1
- Initial Package.
