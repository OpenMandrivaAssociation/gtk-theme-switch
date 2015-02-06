%define name gtk-theme-switch

Summary: 	Switch GTK themes on the fly
Name: 		%{name}
Version: 	1.0.1
Release: 	10
Source0: 	gtk-theme-switch-1.0.1.tar.bz2
Patch1:		gtkts.patch
URL: 		http://www.muhri.net/nav.php3?node=gts
License: 	GPL
Group: 		Graphical desktop/GNOME
BuildRoot:      %{_builddir}/%{name}-buildroot
BuildRequires: 	pkgconfig(gtk+)

%description
Tiny GTK app to let you switch GTK1 themes on the fly.  Very handy if you 
are running Gnome2, which has no GUI to change GTK1 themes.  
NOTE: The binary is just called "switch".

%prep
%setup
%patch1

%build
%make
%install
install -d $RPM_BUILD_ROOT/usr
install -d $RPM_BUILD_ROOT/usr/share
install -d $RPM_BUILD_ROOT/usr/lib
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/share/man/man1
install -d $RPM_BUILD_ROOT/usr/lib/menu
install switch $RPM_BUILD_ROOT/usr/bin
install switch.1 $RPM_BUILD_ROOT/usr/share/man/man1/gtk-theme-switch.1

# menu
mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=switch
Icon=other_configuration
Categories=Settings;
Name=GTK Theme Switch
Comment=Change GTK1 Theme
EOF


%if %mdkversion < 200900
%post 
%{update_menus}
%endif


%if %mdkversion < 200900
%postun 
%{clean_menus}
%endif

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%{_bindir}/switch
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-*.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2011.0
+ Revision: 619283
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2010.0
+ Revision: 429341
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 246711
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 132226
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot
- import gtk-theme-switch


* Fri May 12 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-4mdk
- Fix buildrequires to stop iurt spam

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 1.0.1-3mdk
- rebuild

* Tue Jan 16 2003 Laurent Culioli <laurent@pschit.net> 1.0.1-2mdk
- rebuild

* Tue Jul 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- wrap too long description
- fix mandir location
- fix menu entry (section & default icon)
- from Austin Acton <aacton@yorku.ca> :
	- initial package creation for MDK 8.2+
