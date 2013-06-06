Name:            nimrod
Version:         0.9.2
Release:         1%{?dist}
Summary:         A statically typed, imperative programming language
License:         MIT
URL:             http://nimrod-code.org
Source0:         http://nimrod-code.org/download/%{name}_%{version}.zip

BuildRequires:   readline-devel

%description
Nimrod is a statically typed, imperative programming language that tries to 
give the programmer ultimate power without compromises on runtime efficiency. 
This means it focuses on compile-time mechanisms in all their various forms.

Beneath a nice infix/indentation based syntax with a powerful (AST based, 
hygienic) macro system lies a semantic model that supports a soft realtime GC 
on thread local heaps. Asynchronous message passing is used between threads, 
so no "stop the world" mechanism is necessary. An unsafe shared memory heap 
is also provided for the increased efficiency that results from that model.

%package         doc
Summary:         Documentation for the %{name}
BuildArch:       noarch

%description     doc
This package contains document files for %{name}.

%prep
%setup -q -n %{name}
chmod 755 *.sh

%build
./build.sh
pushd bin/
./nimrod c -d:release ../koch
popd
./koch boot -d:release -d:useGnuReadline

%install
install -p -D -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_sysconfdir}/
install -d %{buildroot}/usr/lib/%{name}/
mv config/* %{buildroot}%{_sysconfdir}/
mv lib/* %{buildroot}/usr/lib/%{name}/

%files
%doc contributors.txt copying.txt
%config(noreplace) %{_sysconfdir}/*
/usr/lib/%{name}/
%{_bindir}/%{name}

%files doc
%doc doc/ examples/

%changelog
* Fri May 24 2013 Christopher Meng <rpm@cicku.me> - 0.9.2-1
- Initial Package.
