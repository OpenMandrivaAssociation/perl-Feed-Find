%define	module	Feed-Find

Name:		perl-%{module}
Version:	0.07
Release:	4
Summary:	Perl Module for Syndication feed auto-discovery
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ErrorHandler)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(URI)
BuildRequires:	perl(LWP)
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
SKIP_SAX_INSTALL=1 perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# requires network access
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Feed/Find*
%{_mandir}/*/*

%changelog
* Sat Feb 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2011.0
+ Revision: 638739
- disable tests, as they require network access
- update to new version 0.07

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.06-6mdv2011.0
+ Revision: 430439
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.06-5mdv2009.0
+ Revision: 256866
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.06-3mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.06-3mdv2007.0
+ Revision: 132931
- fix buildrequires
- Import perl-Feed-Find

* Fri Mar 02 2007 Shlomi Fish  0.06-2mdv2007.1
- changed the BuildArch to noarch.
- changed Requires to BuildRequires.

* Tue Feb 27 2007 Shlomi Fish  0.06-1mdv2007.1
- Initial release. Adapted the Cache-FastMmap spec for this one.

