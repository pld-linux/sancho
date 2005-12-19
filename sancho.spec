
# TODO:
# libgcc_s.so.1 in private dir added to ld.so.conf is asking for trouble;
#   should use system libgcc_s.so.1 >= ? (to check)
# is system libgcj not sufficient?
%define		_ver	0.9.4
%define		_pver	52-linux-gtk
%define		no_install_post_strip	1
Summary:	Graphical user interface for p2p cores
Summary(pl):	Interfejs graficzny dla p2p
Name:		sancho
Version:	0.9.4.52
Release:	1
License:	CPL
Group:		X11/Applications/Networking
Source0:	http://sancho-gui.sourceforge.net/dl/tmp94/%{name}-%{_ver}-%{_pver}.tar.bz2
# Source0-md5:	20bec0ee74dd0e3acfaa86f2a65d6817
Source1:	%{name}.desktop
URL:		http://sancho-gui.sourceforge.net/
Requires:	glibc >= 6:2.3.5-7.6
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sancho is a GUI that connects to a p2p core application. Power users
that use p2p applications usually choose one that has core/GUI
separation. Sancho provides an easy to use, powerful, and configurable
GUI, currently supporting the GUI protocol of the popular mldonkey
core.

%description -l pl
Sancho to graficzny interfejs ³±cz±cy siê z aplikacj± p2p.
Zaawansowani u¿ytkownicy u¿ywaj±cy aplikacji p2p zwykle wybieraj±
takie z rozdzielonym rdzeniem i interfejsem graficznym. Sancho
dostarcza ³atwy w u¿yciu, potê¿ny i konfigurowalny interfejs
graficzny, aktualnie obs³uguj±cy protokó³ GUI popularnego rdzenia
mldonkey.

%prep
%setup -q -n %{name}-%{_ver}-%{_pver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir}}

install sancho-bin $RPM_BUILD_ROOT%{_bindir}/sancho
install lib/libgcc_s.so.1 $RPM_BUILD_ROOT%{_libdir}/%{name}
install lib/libgcj.so.6.0.0 $RPM_BUILD_ROOT%{_libdir}/%{name}
install lib/libswt-*-3212.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install distrib/sancho*.properties $RPM_BUILD_ROOT%{_datadir}/%{name}
install distrib/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo '%{_libdir}/%{name}' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%{name}.conf

%clean
# rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc distrib/AUTHORS distrib/ChangeLog distrib/README distrib/LICENSE.txt
/etc/ld.so.conf.d/*.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
