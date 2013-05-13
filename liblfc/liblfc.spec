%global oname lfc

Name:              liblfc
Version:           1.4.1
Release:           1%{?dist}
Summary:           Lemke Foundation Classes
License:           GPLv2

URL:               http://www.lemke-it.com/litexec?request=publfc&user=&lang=en
Source0:           http://www.lemke-it.com/%{oname}-%{version}.tar.gz

%description
This class library contains several powerful c++ base classes for 
encapsulation of low level operating system calls and library functions. 
The following classes are included:
AESCrypt, Base64Coder, BigDecimal, BigInteger, Bitmap, Chain, CommandExecuter,
Crypt, Datetime, Exception, File, GetLongOpt, GetOpt, Host, ListT, Logger, 
Matcher, NanoTimer, Net, NetHandler, Process, Semaphore, SetT, SharedMemory, 
Sleeper, StackT, SigHandler, Thread, ThreadLock, Timer, Tokenizer, TreeT.

%package           devel
Summary:	   Development files for %{name}
Requires:	   %{name} = %{version}-%{release}

%description	   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}
%configure --disable-static

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.a' -exec rm -f {} ';'
ln -s /usr/lib/liblfc.so.1 %{buildroot}/usr/lib/liblfc.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
/usr/lib/*.so.*

%files devel
%doc COPYING
%{_includedir}/%{oname}/*
/usr/lib/*.so

%changelog
* Mon May 06 2013 Christopher Meng <rpm@cicku.me> - 1.4.1-1
- Initial Package.
