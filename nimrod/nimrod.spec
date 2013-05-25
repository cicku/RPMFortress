Name:              nimrod
Version:           0.9.2
Release:           1%{?dist}
Summary:           A statically typed, imperative programming language
License:           MIT
URL:               http://nimrod-code.org
Source0:           http://nimrod-code.org/download/%{name}_%{version}.zip

BuildRequires:     readline-devel

%description
Nimrod is a statically typed, imperative programming language that tries to 
give the programmer ultimate power without compromises on runtime efficiency. 
This means it focuses on compile-time mechanisms in all their various forms.

Beneath a nice infix/indentation based syntax with a powerful (AST based, 
hygienic) macro system lies a semantic model that supports a soft realtime GC 
on thread local heaps. Asynchronous message passing is used between threads, 
so no "stop the world" mechanism is necessary. An unsafe shared memory heap 
is also provided for the increased efficiency that results from that model.

%package           devel
Summary:           Development files for %{name}
Requires:	   %{name}%{?_isa} = %{version}-%{release}

%description       devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}
chmod 755 build.sh

%build
./build.sh

%install
mkdir -p %{buildroot}%{_bindir}
install -p -D -m 755 bin/nimrod %{buildroot}%{_bindir} bin/nimrod

# install doc directory ...
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/html
install  doc/* %{buildroot}%{_docdir}/%{name}-%{version}/html

# install examples ...
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/examples
install  examples/* %{buildroot}%{_docdir}/%{name}-%{version}/examples

# install misc files ...
install  gpl.html readme.txt contributors.txt %{buildroot}%{_docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check

%files
#%doc COPYING README TODO
#%{_bindir}/*
#%{_libdir}/*.so.*

%files devel
#%{_includedir}/%{name}/
#%{_libdir}/*.so

%changelog
* Fri May 24 2013 Christopher Meng <rpm@cicku.me> - 0.9.2-1
- Initial Package.
