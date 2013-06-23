Name:            uthash
Version:         1.9.8
Release:         3%{?dist}
Summary:         A hash table for C structures
License:         BSD
URL:             http://troydhanson.github.io/uthash
Source0:         https://github.com/troydhanson/%{name}/archive/v%{version}.tar.gz
Patch0:          uthash-remove-failed-tests.patch

BuildArch:       noarch
Provides:        %{name}-devel = %{version}

%description
Any C structure can be stored in a hash table using uthash. Just add a
UT_hash_handle to the structure and choose one or more fields in your 
structure to act as the key. Then use these macros to store, retrieve or 
delete items from the hash table. 

%prep
%setup -q
%patch0 -p1

%build

%install
install -d %{buildroot}%{_includedir}
cp -pa src/*.h %{buildroot}%{_includedir}/

%check
cd tests
make %{?_smp_mflags}

%files
%doc LICENSE doc/*.txt
%{_includedir}/ut*.h

%changelog
* Sat Jun 15 2013 Christopher Meng <rpm@cicku.me> - 1.9.8-3
- Add virtual provide.
- Remove 2 wrong tests.

* Fri Jun 14 2013 Christopher Meng <rpm@cicku.me> - 1.9.8-2
- Remove unneeded BR and make files section more clear.

* Sat Jun 01 2013 Christopher Meng <rpm@cicku.me> - 1.9.8-1
- Initial Package.
