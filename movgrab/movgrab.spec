Name:              movgrab
Version:           1.2.1
Release:           1%{?dist}
Summary:           An online video downloader in console
URL:               https://sites.google.com/site/columscode/home/movgrab
License:           GPLv3

Source0:           https://sites.google.com/site/columscode/files/%{name}-%{version}.tar.gz

%description
movgrab is a downloader for all those pesky sites that insist you use a big 
fat browser that runs flash in order to see their content.

Features:
Command-line application.
No dependancies.
HTTP Proxy server support.
Write download to std-out to feed into another application.
Progress display while downloading.
Fork into background.

%prep
%setup -q

%build
%configure --enable-largefiles
sed -i 's/$(prefix)//' Makefile*
make %{?_smp_flags}

%install
make install DESTDIR=%{buildroot}

%files
%doc CHANGES LICENCE README Docs/*
%{_bindir}/%{name}

%changelog
* Tue Apr 30 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-1
- Initial Package.
