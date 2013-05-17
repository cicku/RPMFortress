Name:              cego
Version:           2.18.1
Release:           1%{?dist}
Summary:           A relational and transactional database
License:           GPLv2

URL:               http://www.lemke-it.com/litexec?request=pubcego&user=&lang=en
Source0:           http://www.lemke-it.com/%{name}-%{version}.tar.gz

BuildRequires:     liblfc-devel
BuildRequires:     liblfc-xml-devel
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
Requires:          %{name} = %{version}-%{release}

%description       devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%configure --disable-static

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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc doc/README COPYING TODO
%{_bindir}/*
/usr/lib/*.so.*

%files devel
%doc COPYING
%{_includedir}/%{name}/*
/usr/lib/*.so

%changelog
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
