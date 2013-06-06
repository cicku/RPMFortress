%global rev a3c3b8077cbe

Name:              hg-git
Version:           0.4.0
Release:           1%{?dist}
Summary:           Mercurial Plugin for Communicating with Git Servers
License:           GPLv2+
Url:               http://hg-git.github.io
Source0:           https://bitbucket.org/durin42/%{name}/get/%{version}.tar.bz2

BuildArch:         noarch
BuildRequires:     mercurial
BuildRequires:     python2-devel
BuildRequires:     python-dulwich
BuildRequires:     python-setuptools
Requires:          mercurial
Requires:          python-dulwich

%description
This is the Hg-Git plugin for Mercurial, adding the ability to push and pull
to/from a Git server repository from Hg. This means you can collaborate on Git
based projects from Hg, or use a Git server as a collaboration point for a team
with developers using both Git and Hg. It can also convert commits/changesets 
losslessly from one system to another, so you can push via an Hg repository 
and another Hg client can pull it and their changeset node ids will be 
identical - Mercurial data does not get lost in translation.

%prep
%setup -q -n durin42-%{name}-%{rev}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc COPYING DESIGN.txt README.md TODO.txt
%{python_sitelib}/hggit/
%{python_sitelib}/hg_git-0.4.0-py2.7.egg-info/

%changelog
* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me> - 0.4.0-1
- Initial Package.
