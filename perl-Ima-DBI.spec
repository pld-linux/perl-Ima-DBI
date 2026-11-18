#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	Ima
%define		pnam	DBI
Summary:	Ima::DBI - database connection caching and organization
Summary(pl.UTF-8):	Ima::DBI - organizacja i buforowanie połączenia z bazą danych
Name:		perl-Ima-DBI
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PERRIN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3c5c0b1fe509556ca35f08aae91b3f5
URL:		http://search.cpan.org/dist/Ima-DBI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
%endif
Requires:	perl-DBIx-ContextualFetch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ima::DBI attempts to organize and facilitate caching and more efficient
use of database connections and statement handles.

%description -l pl.UTF-8
Ima::DBI próbuje zorganizować i ułatwić buforowanie oraz bardziej
wydajne wykorzystanie połączeń z bazą danych i uchwytów do
komunikatów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Ima
%{perl_vendorlib}/Ima/DBI.pm
%{_mandir}/man3/*
