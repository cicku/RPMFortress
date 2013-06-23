%global _hardened_build 1

Name:           sstp-client
Version:        1.0.9
Release:        1%{?dist}
Summary:        Secure Socket Tunneling Protocol (SSTP) Client
License:        GPLv2+
Url:            http://sstp-client.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
Requires:       libevent
Requires:       openssl
Requires:       ppp

%description
This is a client for the Secure Socket Tunneling Protocol, SSTP. It can be 
used to establish a SSTP connection to a Windows Server.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README TODO USING *.example
%{_sbindir}/sstpc
%{_libdir}/*.so
%{_libdir}/pppd/2.4.5/sstp-pppd-plugin.so
%{_mandir}/man8/sstpc.8*

%files devel
%{_includedir}/sstp-client/
%{_libdir}/pkgconfig/sstp-client-1.0.pc

%changelog
* Sun Feb 03 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-1
- Initial Package.
