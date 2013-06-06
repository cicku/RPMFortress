%global dname    clens

Name:            libclens
Version:         0.7.0
Release:         1%{?dist}
Summary:         A convenience library to aid in porting code from OpenBSD
License:         ISC
URL:             https://opensource.conformal.com/wiki/clens
Source0:         https://opensource.conformal.com/snapshots/%{dname}/%{dname}-%{version}.tar.gz

BuildRequires:   libbsd-devel

%description
clens is a convenience library to aid in porting code from OpenBSD to different
operating systems. Operating systems traditionally have different enough APIs
that porting code is painful and can litter pretty code with ugly ifdef goo.
In order to keep code readable and drastically reduce the number of ifdefs
needed, clens brings other APIs or missing functions into specific OS "focus".

%prep
%setup -q -n %{dname}-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} LOCALBASE=%{_prefix}
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%files
%{_includedir}/%{dname}/

%changelog
* Wed Jun 05 2013 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Initial Package.
