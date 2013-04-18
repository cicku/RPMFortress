Name:           perl-DBD-Oracle
Summary:        Oracle database driver for the DBI module
Version:        1.60
Release:        1%{?dist}
License:        GPLv2+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/P/PY/PYTHIAN/DBD-Oracle-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/DBD-Oracle/

BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(DBI)
Requires:       perl(Exporter)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Missed by the find provides script:
Provides:       perl(DBD::Oracle) = %{version}

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DBD::Oracle\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI\\)$
%{?perl_default_subpackage_tests}

%description
DBD::Oracle is a Perl module which works with the DBI module to provide
access to Oracle databases.

%prep
%setup -q -n DBD-Oracle-%{version}

%build
%{__perl} Makefile.PL -h $(ORACLE_HEADERS) -V 11.2.0.3.0
make %{?_smp_mflags}

%install
make install
#make pure_install PERL_INSTALL_ROOT=#{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes examples hints LICENSE META.json oci.def README README.help.txt README.mkdn Todo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD*
%{_mandir}/man3/*

%changelog
* Thu Apr 18 2013 Christopher Meng <rpm@cicku.me> - 1.60-1
- Initial Package.
