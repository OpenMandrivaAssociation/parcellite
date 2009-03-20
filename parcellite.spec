%define name parcellite
%define version 0.9
%define release %mkrel 1 

Name:           %{name} 
Summary:        Lightweight GTK+ clipboard manager.
Version:        %{version} 
Release:        %{release} 
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:            http://parcellite.sourceforge.net/

Group:          Graphical desktop/GNOME 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL 
BuildRequires:  intltool
BuildRequires:  libgtk+2.0_0-devel >= 2.10.0
Requires:       libgtk+2.0_0 >= 2.10.0

%description
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped down, basic-features-only clipboard manager with a small memory footprint for those who like simplicity.


%prep 
%setup -q

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
%{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_mandir}/man1/%{name}.1*


%post
%update_desktop_database

%postun
%clean_desktop_database


