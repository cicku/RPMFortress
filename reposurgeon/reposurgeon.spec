Name:               reposurgeon
Version:            2.32
Release:            1%{?dist}
Summary:            SCM Repository Manipulation Tool
URL:                http://www.catb.org/~esr/reposurgeon/
Source:             http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.gz

License:            BSD

BuildArch:          noarch
BuildRequires:      make
BuildRequires:      xmlto
Requires:           python
# not actually required, but to make the build fail if it isn't
# available on the target dist.
#BuildRequires:      python

%description
Reposurgeon enables risky operations that version-control systems don't want to
let you do, such as editing past comments and metadata and removing commits. It
works with any version control system that can export and import git
fast-import streams, including git, hg, and bzr.

%prep
%setup -q

%build
%__make

%install
install -p -D -m 755 reposurgeon "%{buildroot}%{_bindir}/reposurgeon"
install -p -D -m 644 reposurgeon.1 "%{buildroot}%{_mandir}/man1/reposurgeon.1"

%files
%doc TODO COPYING NEWS README
%{_bindir}/reposurgeon
%doc %{_mandir}/man1/reposurgeon.1*

%changelog
* Sun Apr 07 2013 Christopher Meng <rpm@cicku.me> - 2.32-1
- Update to 2.32
