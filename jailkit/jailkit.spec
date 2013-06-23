%global _hardened_build 1

Name:          jailkit
Version:       2.16
Release:       2%{?dist}
Summary:       A set of utilities to limit Chroot
License:       BSD and GPLv2
URL:           http://olivier.sessink.nl/jailkit/
Source0:       http://olivier.sessink.nl/%{name}/%{name}-%{version}.tar.bz2
Source1:       %{name}.service
Patch0:        jailkit_manpage_fix.patch

BuildRequires: glibc-devel
BuildRequires: libtool
BuildRequires: python

%description
Jailkit is a set of utilities to limit user accounts to specific files using
chroot() and or specific commands. Setting up a chroot shell, a shell limited
to some specific command, or a daemon inside a chroot jail is a lot easier and
can be automated using these utilities.

Jailkit is used in network security appliances from several well known
manufacturers, internet servers from several large enterprise organisations,
servers from internet service providers, as well as many smaller companies and
private users that need to secure cvs, sftp, shell or daemon processes.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{S:1}
if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_sbindir}/jk_chrootsh" > %{_sysconfdir}/shells
else
    grep -q "^%{_sbindir}/jk_chrootsh$" %{_sysconfdir}/shells || echo "%{_sbindir}/jk_chrootsh" >> %{_sysconfdir}/shells
fi

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}
if [ ! -f %{_sysconfdir}/shells ] ; then
    sed -i '/jk_chrootsh/d' %{_sysconfdir}/shells
fi

%files
%doc COPYRIGHT README.txt
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/jk_*.ini
%{_bindir}/jk_uchroot
%{_sbindir}/jk_*
%{_datadir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/jk_*.8*
%{_unitdir}/%{name}.service

%changelog
* Mon Jun 10 2013 Christopher Meng <rpm@cicku.me> - 2.16-2
- Fix error BRs.
- Add PIE support.
- Handle shells when %%post and %%postun.

* Mon May 27 2013 Christopher Meng <rpm@cicku.me> - 2.16-1
- Initial Package.
