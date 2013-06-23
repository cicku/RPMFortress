Name:              dhcpy6d
Version:           0.2
Release:           2%{?dist}
Summary:           DHCPv6 server daemon
License:           GPLv2
URL:               http://dhcpy6d.ifw-dresden.de
Source0:           http://%{name}.ifw-dresden.de/files-%{name}/%{name}-%{version}.tar.gz
Source1:           %{name}.service

BuildArch:         noarch
BuildRequires:     python2-devel python-setuptools
BuildRequires:     systemd
Requires:          MySQL-python
Requires:          python-dns
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Dhcpy6d delivers IPv6 addresses for DHCPv6 clients, which can be identified 
by DUID, hostname or MAC address as in the good old IPv4 days. It allows 
easy dualstack transition, addresses may be generated randomly, by range, 
by arbitrary ID or MAC address. Clients can get more than one address, 
leases and client configuration can be stored in databases and DNS can be 
updated dynamically.

%prep
%setup -q
sed -i 's|!/usr/bin/env python|!/usr/bin/python|g' %{name}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} \
            --install-scripts=%{_sbindir} --root=%{buildroot}
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 644 etc/logrotate.d/%{name} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%post
if [ ! -f %{_localstatedir}/log/%{name}.log ]
    then
    /usr/bin/touch %{_localstatedir}/log/%{name}.log
fi
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc %{_defaultdocdir}/*
%dir %{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_localstatedir}/lib/%{name}/volatile.sqlite
%{_sbindir}/%{name}
%{python_sitelib}/dhcpy6/
%{python_sitelib}/*.egg-info
%{_unitdir}/%{name}.service
%exclude %{_localstatedir}/log/%{name}.log

%changelog
* Fri Jun 21 2013 Christopher Meng <rpm@cicku.me> - 0.2-2
- Put daemon files into sbin.
- Rewrite the systemd file.
- Fix typo in description.

* Tue Jun 04 2013 Christopher Meng <rpm@cicku.me> - 0.2-1
- New upstream release.

* Thu May 09 2013 Christopher Meng <rpm@cicku.me> - 0.1.3-1
- Initial Package.
