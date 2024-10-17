Summary:	Lightweight GTK+ clipboard manager
Name:		parcellite
Version:	1.2.1
Release:	1
Group:		Graphical desktop/GNOME 
License:	GPLv3+
Url:		https://parcellite.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{?prerel}.tar.gz
#Source with correct pot file. You may use it for translate and make lang patch
Source1:	parcellite_po.tar.gz
#Patch0:		parcellite-ru.patch
#Patch1:		parcellite-1.0.2rc5-rosa-glib.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small memory footprint
for those who like simplicity.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog TODO
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------

%prep 
%setup -qn %{name}-%{version}%{?prerel} -a1
%autopatch -p1

rm -rf debian
cd src
rm -f *.o
cd ..

%build 
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

