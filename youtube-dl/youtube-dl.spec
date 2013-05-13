Name:           youtube-dl
Version:        2013.05.07
Release:        1%{?dist}
Summary:        Small command-line program to download videos from YouTube
Group:          Applications/Multimedia
License:        Public Domain
URL:            http://youtube-dl.org
Source0:        http://youtube-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python >= 2.6
# Used in Makefile to generate youtube-dl
BuildRequires:  zip
# Used to generate manpage
BuildRequires:  pandoc
BuildRequires:  python >= 2.6

%description
Small command-line program to download videos from YouTube.

%prep
%setup -cqTn %{name}-%{version}
gzip -dc %{SOURCE0} | tar --strip-components=1 -xvvf -

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT" PREFIX="%{_prefix}" MANDIR="%{_mandir}"
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/bash_completion.d/%{name}

%changelog
* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 2013.05.07-1
- Update to new release

* Thu Apr 18 2013 Till Maas <opensource@till.name> - 2013.04.18-1
- Update to new release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.01.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Till Maas <opensource@till.name> - 2013.01.13-1
- Update to new release

* Sun Jan 06 2013 Matěj Cepl <mcepl@redhat.com> - 2013.01.02-1
- Update to new release (fix #880270)

* Tue Oct 23 2012 Till Maas <opensource@till.name> - 2012.10.09-1
- Update to new release
- Update BR: add pandoc
- install make target

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2012.09.27-3
- Add BR: python >= 2.6

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2012.09.27-2
- Use noreplace for config file
- Add BR: zip

* Tue Oct  2 2012 Tim Landscheidt <tim@tim-landscheidt.de> - 2012.09.27-1
- Bump Python requirement to 2.6.
- Update to new release and GitHub tarballs.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.02.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Till Maas <opensource@till.name> - 2012.02.27-1
- Update to new release

* Thu Jan 26 2012 Till Maas <opensource@till.name> - 2011.12.08-3
- Provide --prefer-free-formats in %%{_sysconfdir}/%%{name}.conf (RH #757577)
  (Patch by Jan Kratochvil)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.12.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Till Maas <opensource@till.name> - 2011.12.08-1
- Update to new release

* Thu Dec 08 2011 Till Maas <opensource@till.name> - 2011.11.23-1
- Update to new release (fixed Red Hat Bug #758679)

* Fri Oct 21 2011 Till Maas <opensource@till.name> - 2011.10.19-1
- Update to latest release

* Thu Aug 04 2011 Till Maas <opensource@till.name> - 2011.08.04-1
- Update to latest release to adjust to backend changes (Red Hat Bug
  #728378)

* Fri May 13 2011 Till Maas <opensource@till.name> - 2011.03.29-1
- Update to latest release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.01.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Till Maas <opensource@till.name> - 2010.01.30-1
- Update to latest release

* Sun Dec 12 2010 Till Maas <opensource@till.name> - 2010.12.09-1
- Update to latest release to adjust with youtube changes

* Sat Nov 06 2010 Till Maas <opensource@till.name> - 2010.10.24-1
- Update to latest release
- Adjust to new upstream location at github instead of bitbucket
- add -p to install
- remove index.html

* Thu Oct 07 2010 Till Maas <opensource@till.name> - 2010.10.03-1
- Update to latest release

* Thu Aug 05 2010 Till Maas <opensource@till.name> - 2010.08.04-1
- Update to latest release

* Fri Jul 23 2010 Till Maas <opensource@till.name> - 2010.07.22-1
- Update to latest release

* Thu Jul 15 2010 Till Maas <opensource@till.name> - 2010.07.14-1
- Update to latest release

* Mon Jun 07 2010 Till Maas <opensource@till.name> - 2010.06.06-1
- Update to latest release

* Thu Apr 29 2010 Till Maas <opensource@till.name> - 2010.04.04-1
- Update to latest release to fix some download issues RH #582372

* Fri Oct 09 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-2
- Small fix in %%prep

* Sun Sep 27 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-1
- Update to 2009.09.13
- License change to Public Domain

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 26 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2008.01.24-1
- Update to v2008.01.24
- Add polish summary and description.

* Wed Jan 02 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-5
- Correct install.
- Correct documentation.

* Sat Dec 29 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-4
- Correct requires.
- Add documentation.

* Sun Dec 23 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-3
- Correct version tag.

* Fri Dec 14 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-2
- Update to v2007.10.12, correct license and update summary.

* Sun Dec 9 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-1
- First release
