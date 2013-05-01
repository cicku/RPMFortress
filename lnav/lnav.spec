Name:              lnav
Version:           0.5.0
Release:           1%{?dist}
Summary:           A curses-based tool for viewing and analyzing log files
URL:               http://lnav.org
License:           BSD(revised)

Source:            https://dl.dropboxusercontent.com/u/70174949/%{name}-%{version}.tar.bz2

BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     bzip2-devel
BuildRequires:     ncurses-devel
BuildRequires:     openssl-devel
BuildRequires:     pcre-devel
BuildRequires:     readline-devel
BuildRequires:     sqlite-devel
BuildRequires:     zlib-devel

%description
The log file navigator, lnav, is an enhanced log file viewer that
takes advantage of any semantic information that can be gleaned from
the files being viewed, such as timestamps and log levels.  Using this
extra semantic information, lnav can do things like interleaving
messages from different files, generate histograms of messages over
time, and providing hotkeys for navigating through the file.  It is
hoped that these features will allow the user to quickly and
efficiently zero in on problems.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_flags}

%install
make install DESTDIR=%{buildroot}

%check
make test

%files
%doc LICENSE NEWS README
%{_bindir}/%{name}

%changelog
* Sat Apr 27 2013 Christopher Meng <rpm@cicku.me> - 0.5.0-1
- Initial Package.
