Name:               fly
Version:            2.0.1
Release:            1%{?dist}
Summary:            A Script to Create images
Url:                http://martin.gleeson.com/fly/
License:            None

BuildRequires:      freetype-devel
BuildRequires:      gd-devel
BuildRequires:      libjpeg-devel
BuildRequires:      libpng-devel

Source0:            http://martin.gleeson.net/%{name}/dist/%{name}-%{version}.tar.gz

%description
Fly is a C program that creates PNG, JPEG or GIF images on the fly from CGI and other programs. Using Thomas Boutell's gd graphics library for fast image creation, it provides a command-file interface for creating and modifying images.

%prep
%setup -q

%build
make %{?_smp_mflags} #CFLAGS="#RPM_OPT_FLAGS" CC="#__cc"

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README examples doc
%{_bindir}/%{name}

%changelog
* Wed Apr 17 2013 Christopher Meng <cickumqt@gmail.com> - 2.0.1-1
- Initial Package.
