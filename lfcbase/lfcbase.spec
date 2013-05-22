%global _hardened_build 1

Name:              lfcbase
Version:           1.5.4
Release:           2%{?dist}
Summary:           Lemke Foundation Classes
License:           GPLv3+

URL:               http://www.lemke-it.com/litexec?request=publfc&user=&lang=en
Source0:           http://www.lemke-it.com/%{name}-%{version}.tar.gz

%description
This class library contains several powerful c++ base classes for 
encapsulation of low level operating system calls and library functions. 
The following classes are included:
AESCrypt, Base64Coder, BigDecimal, BigInteger, Bitmap, Chain, CommandExecuter,
Crypt, Datetime, Exception, File, GetLongOpt, GetOpt, Host, ListT, Logger, 
Matcher, NanoTimer, Net, NetHandler, Process, Semaphore, SetT, SharedMemory, 
Sleeper, StackT, SigHandler, Thread, ThreadLock, Timer, Tokenizer, TreeT.

%package           devel
Summary:           Development files for %{name}
Requires:	   %{name}%{?_isa} = %{version}-%{release}

%description	   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%configure --disable-static
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
make check

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%doc samples/*.cc
%{_includedir}/%{name}/
%{_libdir}/*.so

%changelog
* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 1.5.4-2
- Fix the license problem.

* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 1.5.4-1
- New release.

* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 1.5.3-1
- New release.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.5.2-1
- New release.

* Mon May 06 2013 Christopher Meng <rpm@cicku.me> - 1.4.1-1
- Initial Package.
