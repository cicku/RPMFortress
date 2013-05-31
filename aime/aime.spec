%global libname libaime

Name:            aime
Version:         5.20130520
Release:         1%{?dist}
Summary:         An application embeddable programming language interpreter
License:         GPLv3+
URL:             http://aime-embedded.sourceforge.net/
Source0:         http://downloads.sourceforge.net/project/aime-embedded/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

%description
aime is a programming language, with a C like syntax, intended for application
extending purposes. The aime collection comprises the language description, an
application embeddable interpreter (libaime), the interpreter C interface
description and a standalone interpreter. Many examples on how the interpreter
can be used (embedded in an application) are also available, together with 
some hopefully useful applications, such as expression evaluators.

%package         devel
Summary:         Development files for %{name}
Requires:	 %{name}%{?_isa} = %{version}-%{release}

%description     devel
The %{name}-devel package contains header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.a' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{libname}.info %{_infodir}/dir || :

%preun
/sbin/install-info --delete %{_infodir}/%{libname}.info %{_infodir}/dir || :

%files
%doc COPYING README TODO
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/%{libname}.info*

%files devel
%{_includedir}/%{name}.h

%changelog
* Fri May 31 2013 Christopher Meng <rpm@cicku.me> - 5.20130520-1
- Initial Package.
