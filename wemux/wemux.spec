Name:           wemux
Version:        3.1.0
Release:        1%{?dist}
Summary:        A tool help improve multi-user terminal multiplexing
License:        MIT
URL:            http://github.com/zolrath/wemux
Source0:        https://github.com/downloads/zolrath/%{name}/%{name}-%{version}.tar.gz

Requires:       tmux
BuildArch:      noarch

%description
wemux enhances tmux to make multi-user terminal multiplexing both easier 
and more powerful. It allows users to host a wemux server and have clients 
join in either:

Mirror Mode gives clients (another SSH user on your machine) read-only access 
to the session, allowing them to see you work, or

Pair Mode allows the client and yourself to work in the same 
terminal (shared cursor)

Rogue Mode allows the client to pair or work independently in another 
window (separate cursors) in the same tmux session.

It features multi-server support as well as user listing and notifications 
when users attach/detach.

%prep
%setup -q
sed -i 's|/usr/local||g' %{name}
gzip man/%{name}.1

%build

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf
install -p -D -m 644 man/%{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%check

%files
%doc MIT-LICENSE README.md
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Mar 27 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-1
- Initial Package.
