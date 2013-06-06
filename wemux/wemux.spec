%global commit 9bff23720d09a910dacad101c18d0f4512ae375a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wemux
Version:        2.2.0
Release:        1%{?dist}
Summary:        A tool help improve multi-user terminal multiplexing
License:        MIT
URL:            https://github.com/zolrath/wemux
Source0:        https://github.com/zolrath/wemux/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

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
%setup -q -n %{name}-%{commit}
sed -i 's|/usr/local||g' %{name}

%build

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf

%check

%files
%doc MIT-LICENSE README.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}

%changelog
* Wed Mar 27 2013 Christopher Meng <rpm@cicku.me> - 2.2.0-1
- Initial Package.
