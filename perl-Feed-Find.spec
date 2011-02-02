%define	module	Feed-Find
%define	name	perl-%{module}
%define	release	%mkrel 1
%define	version	0.07

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl Module for Syndication feed auto-discovery
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-Class-ErrorHandler perl-HTML-Parser perl-URI perl-libwww-perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Perl Module for Syndication feed auto-discovery.

Feed::Find implements feed auto-discovery for finding syndication feeds, 
given a URI. It (currently) passes all of the auto-discovery tests at 
http://diveintomark.org/tests/client/autodiscovery/ .

Feed::Find will discover the following feed formats:

RSS 0.91
RSS 1.0
RSS 2.0
Atom

%prep
%setup -q -n %{module}-%{version}

%build
SKIP_SAX_INSTALL=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Feed/Find*
%{_mandir}/*/*


