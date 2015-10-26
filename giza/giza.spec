%global globalopts GIZALIB="libgiza" PREFIX="%{_prefix}" X11DIR="%{_prefix}" CFLAGS=" -Wall -Wextra %{optflags} -fPIC" FFLAGS=" -Wall -Wextra %{optflags} -fPIC" LIBDIR="%{_libdir}"

Name:           giza
Summary:        Scientific plotting library for C/Fortran
Version:        0.9.3
Release:        1%{?dist}
License:        GPLv2+
URL:            http://giza.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-gfortran

%description
Giza is a 2D scientific plotting library built on cairo. It provides uniform
output to PDF, PS, PNG and X-Windows. It was written to replace PGPLOT.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Fix the bollocks from upstream.
sed -i -e 's|${X11DIR}/lib|${X11DIR}/%{_lib}|g;s|$(LDFLAGS)|$(LDFLAGS) %{?__global_ldflags}|g;s|$(PREFIX)/lib|%{_libdir}|g;s|cp $(SHARED_LIB_GIZA)|cp $(SHARED_LIB_GIZA_VERSION)|g'  \
       -e '/giza.mod/c \\tcp\ giza.mod\ $(DESTDIR)$(FMODDIR)'                                                                  \
       build/Makefile

sed -i 's|$(CC) -o $@ $<|$(CC) -c %{optflags} $< -o $@|g;s|$(LDFLAGS)|$(LDFLAGS) %{?_global_ldflags}|g;s|${PREFIX}/lib|%{_libdir}|g;s|-Wall|%{optflags}|g;s|-L../lib/|-L../build/|g' test/Makefile

%build
make giza %{globalopts} USE_FREETYPE="yes"

%install
mkdir -p %{buildroot}{%{_libdir},%{_includedir},%{_fmoddir}}
make installgiza %{globalopts} FMODDIR="%{_fmoddir}" DESTDIR="%{buildroot}"
cd %{buildroot}%{_libdir} && ln -sf libgiza.so.%{version} libgiza.so

find %{buildroot} -name '*.a' -delete -print

%check
#make all PREFIX="%{_prefix}" -C test
# The reason I commented them is, it requires actions from user. These tests
# are graphics based, I'm afraid we can't test now.
# But, from my machine, these tests ran fine.
#LD_LIBRARY_PATH=../build/ ./test-fortran ./test-box ./test-2D

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libgiza.so.%{version}

%files devel
%doc AUTHORS CHANGES interface/
%{_fmoddir}/giza.mod
%{_includedir}/giza*.h
%{_libdir}/libgiza.so

%changelog
* Mon Oct 26 2015 Christopher Meng <rpm@cicku.me> - 0.9.3-1
- Initial Package.
