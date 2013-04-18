%global _unpackaged_files_terminate_build 0

Name:               ora2pg
Version:            11.1
Release:            1%{?dist}
Summary:            Oracle to PostgreSQL database schema converter

License:            GPLv3+
URL:                http://ora2pg.darold.net

Source0:            http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildArch:          noarch

BuildRequires:      perl

Requires:           perl(DBD::Pg)
Requires:           perl(DBD::Oracle)
Requires:           perl(DBI) 
Requires:           perl(String::Random)
Requires:           perl(IO::Compress::Base)
Requires:           perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Ora2Pg is a free tool used to migrate an Oracle database to a PostgreSQL compatible schema. It connects your
Oracle database, scan it automaticaly and extracts its structure or data, it then generates SQL scripts that you can
load into your PostgreSQL database.

Ora2Pg can be used from reverse engineering Oracle database to huge enterprise database migration or simply to replicate
some Oracle data into a PostgreSQL database. It is really easy to used and doesn't need any Oracle database knowledge than
providing the parameters needed to connect to the Oracle database.

%prep
%setup -q

%build
# Make Perl and Ora2Pg distrib files
%{__perl} Makefile.PL \
    INSTALLDIRS=vendor \
    QUIET=1 \
    CONFDIR=%{_sysconfdir} \
    DOCDIR=%{_docdir}/%{name}-%{version} \
    DESTDIR=%{buildroot} < /dev/null
%{__make}

%install
install -p -D -m 755 %{buildroot}/%{_bindir}
install -p -D -m 755 %{buildroot}/%{_sysconfdir}/%{name}


# Make distrib files
make install \
	DESTDIR=%{buildroot}

install -p -D -m 644 doc/%{name}.3 %{buildroot}/%{_mandir}/man3/%{name}.3

%files
%doc changelog README LICENSE
%{_bindir}/%{name}
%{_mandir}/man3/%{name}.3*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{perl_vendorlib}/Ora2Pg/PLSQL.pm
%{perl_vendorlib}/Ora2Pg.pm

%changelog
* Thu Apr 18 2013 Christopher Meng <rpm@cicku.me>
- Initial Package.
