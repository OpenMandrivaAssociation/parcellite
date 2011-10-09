%define name parcellite
%define version 1.0.2
%define subver rc5
%define release %mkrel 1

Name:           %{name} 
Summary:        Lightweight GTK+ clipboard manager
Version:        %{version}%{subver} 
Release:        %{release}
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
#Source with correct pot file. You may use it for translate and make lang patch
Source1:	parcellite_po.tar.gz
Patch0:		parcellite-ru.patch
URL:            http://parcellite.sourceforge.net/

Group:          Graphical desktop/GNOME 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPLv3+
BuildRequires:  intltool
BuildRequires:  gtk+2-devel >= 2.10.0

%description
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small memory footprint
for those who like simplicity.

%prep 
%setup -q -a1
%patch0 -p0

%build 
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/*

%post
%update_desktop_database

%postun
%clean_desktop_database
