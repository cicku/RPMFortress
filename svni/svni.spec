Name:           svni
Version:        0.36.1
Release:        1%{?dist}
Summary:        Subversion interactive check-in wrapper
License:        GPLv3+
URL:            http://svni.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  perl
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       subversion
BuildArch:      noarch

%description
svni is a wrapper for "svn ci". It features syntax checking before checking 
in files; Giving the possibility to make a final selection of files to check 
in when entering a commit message; And showing the differences that are 
about to be checked in.

Features:
- Command-line tool
- Check syntax before committing files to the repository
- Review changes before committing
- Make last-minute changes to the list of files to be committed
- Automatically execute a script after a successful commit

%package        vim
Summary:        Vim syntax highlighting file for Subversion interactive check-in wrapper
Requires:       vim

%description    vim
This package additionally provides a vim syntax highlighting configuration.

%prep
%setup -q
sed -i 's|/usr/bin/env perl|/usr/bin/perl|g' %{name}

%build

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.1 "%{buildroot}%{_mandir}/man1/%{name}.1.gz"
install -p -D -m 644 %{name}.vim "%{buildroot}%{_datadir}/vim/vim73/syntax/%{name}.vim"

%files
%doc CHANGES COPYING example.svnirc %{name}.{html,pdf,ps}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files vim
%{_datadir}/vim/vim73/syntax/%{name}.vim

%changelog
* Fri Jun 21 2013 Christopher Meng <rpm@cicku.me> - 0.36.1-1
- Fix the manpage errors.

* Tue Sep 18 2012 Christopher Meng <rpm@cicku.me> - 0.36-1
- Initial Package.
