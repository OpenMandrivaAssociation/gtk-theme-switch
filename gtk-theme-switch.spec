%define name gtk-theme-switch
%define version 1.0.1
%define release %mkrel 4

Summary: 	Switch GTK themes on the fly
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	gtk-theme-switch-1.0.1.tar.bz2
Patch1:		gtkts.patch
URL: 		http://www.muhri.net/nav.php3?node=gts
License: 	GPL
Group: 		Graphical desktop/GNOME
BuildRoot:      %{_builddir}/%{name}-buildroot
BuildRequires: 	gtk+1.2-devel

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
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="switch" icon="other_configuration.png" needs="X11" section="Configuration/Other" title="GTK Theme Switch" longtitle="Change GTK1 Theme"
EOF


%post 
%{update_menus}


%postun 
%{clean_menus}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%{_bindir}/switch
%{_mandir}/man1/*
%{_menudir}/*

