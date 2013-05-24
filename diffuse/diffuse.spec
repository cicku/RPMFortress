Name:             diffuse
Version:          0.4.7
Release:          1%{?dist}
Summary:          A graphical tool for merging and comparing text files

Group:            Development/Tools
License:          GPLv2+
URL:              http://diffuse.sourceforge.net/
Source0:          http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:    desktop-file-utils scrollkeeper
BuildRequires:    gettext
Requires:         python >= 2.4, pygtk2 >= 2.10
Requires(post):   scrollkeeper
Requires(postun): scrollkeeper
BuildArch:        noarch

%description
Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line matching and directly edit files. Diffuse can
also retrieve revisions of files from Bazaar, CVS, Darcs, Git, Mercurial,
Monotone, Subversion, and SVK repositories for comparison and merging.

%prep
%setup -q
sed -i 's|/usr/local/|/usr/|g' install.py

%build

%install
%{__python} install.py --destdir=%{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
update-desktop-database &> /dev/null || :

%postun
scrollkeeper-update -q || :
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/diffuse.desktop
%{_datadir}/gnome/help/diffuse/*/diffuse.xml
%{_datadir}/omf/diffuse/diffuse-*.omf
%{_datadir}/pixmaps/diffuse.png
%config(noreplace) %{_sysconfdir}/diffuserc
%{_mandir}/man*/*
%{_mandir}/*/man*/*
%dir %{_datadir}/gnome/help/diffuse
%dir %{_datadir}/gnome/help/diffuse/*
%dir %{_datadir}/omf/diffuse

%changelog
* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 0.4.7-1
- New version.
- Redefine the install step.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Jon Levell <fedora@coralbark.net> - 0.4.5-1
- Update to 0.4.5 upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 10 2010 Jon Levell <fedora@coralbark.net> - 0.4.3-1
- Update to 0.4.3 upstream release

* Thu Sep 17  2009 Jon Levell <fedora@coralbark.net> - 0.4.0-1
- Update to new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 4  2009 Jon Levell <fedora@coralbark.net> - 0.3.4-1
- Update to new upstream release (patch no longer needed)

* Tue Jun 30 2009 Jon Levell <fedora@coralbark.net> - 0.3.3-1
- Update to latest upstream release
- Add patch provided by upstream 

* Tue Mar 10 2009 Jon Levell <fedora@coralbark.net> - 0.3.1-1
- Update to latest upstream release

* Wed Feb 11 2009 Jon Levell <fedora@coralbark.net> - 0.2.15-4
- Validate the .desktop file
- Use the prescribed forms for scrollkeeper/update-desktop-database
- Clean up the unowned directories

* Sat Jan 24 2009 Jon Levell <fedora@coralbark.net> - 0.2.15-3
- Fix typos in formatting of changelog
- Fix buildroot in line with packaging guidelines
- Updated defattr with default directory permissions

* Wed Jan 21 2009 Jon Levell <fedora@coralbark.net> - 0.2.15-2
- Use macros in file paths
- patch .desktop file to add trailing semi-colons
- updated URL/source/group

* Tue Jan 20 2009 Jon Levell <fedora@coralbark.net> - 0.2.15-1
- clean buildroot on install
- conditional use scrollkeeper/update-desktop-database
- updated release/license as per Fedora guidelines
- first version submitted to Fedora

* Sun Apr 27 2008 Derrick Moser <derrick_moser@yahoo.com>
- created initial diffuse package
