%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)}}
Name:		mod_spdy
Version:	1
Release:	1%{?dist}
Summary:	A SPDY module for the Apache HTTP server
License:	ASL 2.0
URL:		https://code.google.com/p/mod-spdy/
Source0:	mod_spdy-%{version}.tar.bz2
Source1:	spdy.conf
Source2:	01-spdy.conf

BuildRequires:	httpd-devel >= 2.2, pkgconfig
Provides: mod-spdy = %{version}
Requires: httpd >= 2.2, libstdc++ >= 4.1.2, httpd-mmn = %{_httpd_mmn}

%description
mod_spdy is an experimental implementation of the SPDY protocol that aims to provide SPDY support in the Apache HTTPD server.

%prep
%setup -q
cp -p %{SOURCE1} spdy.conf
cp -p %{SOURCE2} 01-spdy.conf

%build
cd src
chmod 755 ./build/gyp_chromium
make BUILDTYPE=Release
sh build_modssl_with_npn.sh

%install
install -m 755 -d %{buildroot}/etc %{buildroot}/usr/lib64/httpd/modules/
install -D -m 644 spdy.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/spdy.conf
install -D -m 644 01-spdy.conf %{buildroot}%{_sysconfdir}/httpd/conf.modules.d/01-spdy.conf
strip src/out/Release/libmod_spdy.so
cp src/out/Release/libmod_spdy.so "%{buildroot}/usr/lib64/httpd/modules/mod_spdy.so"
cp src/mod_ssl.so "%{buildroot}/usr/lib64/httpd/modules/mod_ssl_with_npn.so"

%files
%defattr(-,root,root,-)
/usr/lib64/httpd/modules/mod_spdy.so
/usr/lib64/httpd/modules/mod_ssl_with_npn.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/spdy.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/01-spdy.conf

%changelog
* Fri Mar 22 2012 Michal Piotrowski <michal@eventhorizon.pl> 0.1
- Initial release
