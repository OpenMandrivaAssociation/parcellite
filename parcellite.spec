%define prerel rc5

Summary:	Lightweight GTK+ clipboard manager
Name:		parcellite
Version:	1.0.2
Release:	%{?prerel:0.%{prerel}.}3
Group:		Graphical desktop/GNOME 
License:	GPLv3+
Url:		http://parcellite.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{?prerel}.tar.gz
#Source with correct pot file. You may use it for translate and make lang patch
Source1:	parcellite_po.tar.gz
Patch0:		parcellite-ru.patch
Patch1:		parcellite-1.0.2rc5-rosa-glib.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small memory footprint
for those who like simplicity.

%prep 
%setup -qn %{name}-%{version}%{?prerel} -a1
%autopatch -p1

rm -rf debian
cd src
rm -f *.o
cd ..

%build 
%configure2_5x
make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.1*

