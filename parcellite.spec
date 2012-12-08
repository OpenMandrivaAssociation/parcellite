%define version 1.0.2
%define prerel rc5

Name:           parcellite
Summary:        Lightweight GTK+ clipboard manager
Version:        %{version}
Release:        %{?prerel:0.%{prerel}.}3
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{?prerel}.tar.gz
#Source with correct pot file. You may use it for translate and make lang patch
Source1:	parcellite_po.tar.gz
Patch0:		parcellite-ru.patch
Patch1:		parcellite-1.0.2rc5-rosa-glib.patch
URL:            http://parcellite.sourceforge.net/

Group:          Graphical desktop/GNOME 
License:        GPLv3+
BuildRequires:  intltool
BuildRequires:  gtk+2-devel >= 2.10.0

%description
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small memory footprint
for those who like simplicity.

%prep 
%setup -q -a1 -n %{name}-%{version}%{?prerel}
%patch0 -p0
%patch1 -p1

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
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/*


%changelog
* Mon Oct 10 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.2rc5-2mdv2012.0
+ Revision: 704008
- fix requires from x86_64 libs in 32 bit builds

* Sun Oct 09 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.2rc5-1
+ Revision: 703949
- 1.0.2rc5
 * Fixed the primary deselect and file cut/paste issue.
 * Fix bugs introduced in clipboard code selection.
 * Applied FSF Address change patch from Andrew Starr-Bochicchio, Debian.
 * Changed history limit to 1000.

* Thu Aug 11 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.2rc3-1
+ Revision: 694043
- New version 1.0.2rc3. Fix error and add new options, such as whitespace trim.

* Mon May 02 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.2rc2-1
+ Revision: 661420
- new release 1.0.2rc2

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2mdv2011.0
+ Revision: 614474
- the mass rebuild of 2010.1 packages

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 485097
- update to new version 0.9.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 0.9.1-1mdv2009.1
+ Revision: 359137
- version 0.9.1

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 0.9-1mdv2009.1
+ Revision: 359136
- Fix summary, description, license, BuildRequires
- import parcellite package from Charles-Henri d'Adh?\195?\169mar (#46775)


* Sat Jan 03 2009 Charles-Henri d'Adhémar <cdadhemar@gmail.com> 0.9-1mdv
- First release

