%define upstream_name	 Gtk2-CV
%define upstream_version 1.56

%define _requires_exceptions perl(Gtk2::CV::Jobber::Client::)

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 3

Summary:	A fast gtk+ image viewer modeled after xv
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	gtkspell-devel
BuildRequires:	glitz-devel
BuildRequires:  jpeg-devel
BuildRequires:  libmagic-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(Glib) > 1.00
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
# not automatically found:
Requires:	perl-Gtk2-PodViewer

%description
CV is a fast gtk+ image viewer modeled after xv.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 
perl -pi -e 's/PetRenamer/PatRenamer/' lib/Gtk2/CV/Plugin/PatRenamer.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2*
%{perl_vendorarch}/auto/Gtk2
