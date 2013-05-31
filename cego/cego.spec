%global _hardened_build 1

Name:              cego
Version:           2.18.7
Release:           1%{?dist}
Summary:           A relational and transactional database
License:           GPLv3+
URL:               http://www.lemke-it.com/litexec?request=pubcego&user=&lang=en
Source0:           http://www.lemke-it.com/%{name}-%{version}.tar.gz

BuildRequires:     chrpath
BuildRequires:     lfcbase-devel
BuildRequires:     lfcxml-devel
BuildRequires:     libtool
BuildRequires:     ncurses-devel
BuildRequires:     readline-devel

%description
An open source implementation of a relational and transnational database 
system using an object oriented software design. It supports SQL query
requests using all common programming interfaces (C, C++, DBD, Java). 
The system architecture is multi-threaded based on POSIX threads and is 
designed for high end performance and availability.

%package           devel
Summary:           Development files for %{name}
Requires:	   %{name}%{?_isa} = %{version}-%{release}
Requires:	   lfcbase-devel%{?_isa}
Requires:	   lfcxml-devel%{?_isa}

%description       devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
autoreconf -fiv
%configure --disable-static
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

%build
make %{?_smp_mflags}

%install
pushd src
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
popd

for f in `ls %{buildroot}/tools`
do install -p -D -m 755 $f %{buildroot}%{_bindir}/$f
done

for _rpbin in %{buildroot}%{_bindir}/*
do
  chrpath --delete "${_rpbin}"
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
./checkDB base && ./checkDB gate

%files
%doc COPYING README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%changelog
* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 2.18.7-1
- New release.

* Thu May 23 2013 Christopher Meng <rpm@cicku.me> - 2.18.6-1
- New release.
- Fix the checkDB issue.

* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 2.18.5-1
- New release.

* Mon May 20 2013 Christopher Meng <rpm@cicku.me> - 2.18.4-1
- New release.

* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 2.18.3-1
- New release.

* Fri May 17 2013 Christopher Meng <rpm@cicku.me> - 2.18.2-1
- New release.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 2.18.1-1
- New release.

* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 2.18.0-1
- New release.

* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 2.17.12-1
- New release.

* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 2.17.11-1
- New version includes fixes for Fedora.

* Mon May 06 2013 Christopher Meng <rpm@cicku.me> - 2.17.10-1
- Initial Package.
