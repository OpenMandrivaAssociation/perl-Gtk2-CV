%define upstream_name	 Gtk2-CV
%define upstream_version 1.56

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Gtk2::CV::Jobber::Client(.*)\\)'
%else
%define _requires_exceptions perl(Gtk2::CV::Jobber::Client::)
%endif

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A fast gtk+ image viewer modeled after xv
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	gtkspell-devel
BuildRequires:	glitz-devel
BuildRequires:	jpeg-devel
BuildRequires:	magic-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(Glib) > 1.00
BuildRequires:	perl-devel

# not automatically found:
Requires:	perl(Gtk2::PodViewer)

%description
CV is a fast gtk+ image viewer modeled after xv.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 
perl -pi -e 's/PetRenamer/PatRenamer/' lib/Gtk2/CV/Plugin/PatRenamer.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2*
%{perl_vendorarch}/auto/Gtk2


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.560.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Funda Wang <fwang@mandriva.org>
    - bump rel
    - rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.560.0-1mdv2011.0
+ Revision: 594462
- update to new version 1.56

* Fri Jan 29 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.550.0-3mdv2011.0
+ Revision: 497910
- remove extra requires

* Wed Jan 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.550.0-2mdv2010.1
+ Revision: 497158
- fix typo in a plugin

* Wed Jan 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.550.0-1mdv2010.1
+ Revision: 497004
- update to 1.55

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 1.540.0-2mdv2010.0
+ Revision: 419814
- rebuild for new libjpeg v7

* Fri Jul 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.540.0-1mdv2010.0
+ Revision: 399302
- update to 1.54 for real this time
- using %%perl_convert_version
- fixed license & buildrequires fields

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2010.0
+ Revision: 370127
- update to new version 1.54

* Wed Jul 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.3-1mdv2009.0
+ Revision: 233036
- new version

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-1mdv2008.1
+ Revision: 159935
- new version

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2008.1
+ Revision: 152214
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2008.1
+ Revision: 112505
- update to new version 1.5

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdv2008.0
+ Revision: 47638
- update to new version 1.4


* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdv2007.0
+ Revision: 96805
- fix build dependencies
- new version
- Import perl-Gtk2-CV

* Sun Apr 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdk
- New release 1.2

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1-2mdk
- Fix BuildRequires

* Thu Nov 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdk
- New release 1.1

* Thu Oct 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- fix url
- fix group
- fix directory ownership
- drop explicit gtk+2 dependency

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-3mdk
- Add buildrequires

* Sat Jul 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.15-2mdk
- fix requires

* Fri May 20 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.15-1mdk
- initial release

