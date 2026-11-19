#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Plack
%define		pnam	Middleware-RemoveRedundantBody
Summary:	Plack::Middleware-RemoveRedundantBody - remove body for HTTP response if it's not required
Name:		perl-Plack-Middleware-RemoveRedundantBody
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/S/SW/SWEETKID/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75ba53485a1934c30028ca66db1f5e15
URL:		https://metacpan.org/dist/Plack-Middleware-RemoveRedundantBody
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Plack
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plack::Middleware::RemoveRedundantBody removes the body of an HTTP
response, if it is not required by its status code (for example 204 or
304).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Plack/Middleware/RemoveRedundantBody.pm
%{_mandir}/man3/*
