%global commit ca154d0159e5290afcd37ff27d6c0fbdd167e19f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           valama
Version:        0.1.1
Release:        1%{?dist}
Summary:        A next generation Vala IDE
License:        GPLv3+
URL:            https://github.com/Valama/valama/
Source0:        https://github.com/Valama/valama/archive/%{commit}/%{name}-%{version}-%{shortcommit}.zip

BuildRequires:  cmake
BuildRequires:  gtksourceview3-devel
BuildRequires:  libgee-devel
BuildRequires:  libxml2-devel
BuildRequires:  libgdl-devel
BuildRequires:  vala-devel
Requires:       gnome-icon-theme-symbolic
Requires:       ImageMagick
Requires:       intltool

%description
xxx

%prep
%setup -q -n %{name}-%{commit}

%build
mkdir build && cd build
%{cmake} ..
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang

%check
ctest

%files -f %{name}.lang
%doc COPYING README.md
xxx

%changelog
* Sun Jun 09 2013 Christopher Meng <rpm@cicku.me> - 0.1.1-1
- Initial Package.
