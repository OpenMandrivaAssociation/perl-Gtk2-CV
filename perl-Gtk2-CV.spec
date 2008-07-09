%define module	Gtk2-CV
%define name	perl-%{module}
%define version 1.5.3
%define up_version  1.53
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	A fast gtk+ image viewer modeled after xv
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/Gtk2/%{module}-%{up_version}.tar.gz
BuildRequires:	gtkspell-devel
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-Gtk2
BuildRequires:	perl-Glib > 1.00
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	glitz-devel
BuildRequires:  jpeg-devel
BuildRequires:  libmagic-devel
# not automatically found:
Requires:	perl-Gtk2-PodViewer
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CV is a fast gtk+ image viewer modeled after xv.

%prep
%setup -q -n %{module}-%{up_version}
find -type d -name CVS | rm -rf 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS -Os -s"

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


