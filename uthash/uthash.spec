Name:            uthash
Version:         1.9.8
Release:         1%{?dist}
Summary:         A hash table for C structures
License:         BSD
URL:             http://troydhanson.github.io/uthash
Source0:         http://prdownloads.sourceforge.net/uthash/uthash-%{version}.tar.gz
BuildRequires:   glibc-devel

%description
Any C structure can be stored in a hash table using uthash. Just add a
UT_hash_handle to the structure and choose one or more fields in your structure
to act as the key. Then use these macros to store, retrieve or delete items
from the hash table. 

%prep
%setup -q

%build

%install
install -d "%{buildroot}%{_includedir}"
cp -pa src/*.h "%{buildroot}%{_includedir}/"

%check
cd tests
make %{?_smp_mflags}

%files
%doc LICENSE README.md doc/ChangeLog.txt
%{_includedir}/*.h

%changelog
* Sat Jun 01 2013 Christopher Meng <rpm@cicku.me> - 1.9.8-1
- Initial Package.
