
# Conditional build:
%bcond_with	tests	# Perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Ima
%define		pnam	DBI
Summary:	Ima::DBI - database connection caching and organization
Summary(pl):	Ima::DBI - organizacja i buforowanie po³±czenia z baz± danych
Name:		perl-Ima-DBI
Version:	0.33
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/T/TM/TMTM/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d72cfbca2aa5e2b631020122858e3ae
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

%description -l pl
Ima::DBI próbuje zorganizowaæ i u³atwiæ buforowanie oraz bardziej
wydajne wykorzystanie po³±czeñ z baz± danych i uchwytów do
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
%dir %{perl_vendorlib}/%{pdir}
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
