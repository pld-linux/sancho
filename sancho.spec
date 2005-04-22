
# TODO:
# libgcc_s.so.1 in private dir added to ld.so.conf is asking for trouble;
#   should use system libgcc_s.so.1 >= ? (to check)
# is system libgcj not sufficient?
%define		_pver	37-linux-fox
Summary:	Graphical user interface for p2p cores
Summary(pl):	Interfejs graficzny dla p2p
Name:		sancho
Version:	0.9.4
Release:	2.1
License:	CPL
Group:		X11/Applications/Networking
Source0:	http://sancho-gui.sourceforge.net/dl/tmp94/%{name}-%{version}-%{_pver}.tar.bz2
# Source0-md5:	f4dbc54657155dc8e9bef20211024713
Source1:	%{name}.desktop
URL:		http://sancho-gui.sourceforge.net/
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sancho is a GUI that connects to a p2p core application. Power users
that use p2p applications usually choose one that has core/GUI
separation. Sancho provides an easy to use, powerful, and configurable
GUI, currently supporting the GUI protocol of the popular mldonkey
core.

%description -l pl
Sancho to graficzny interfejs ��cz�cy si� z aplikacj� p2p.
Zaawansowani u�ytkownicy u�ywaj�cy aplikacji p2p zwykle wybieraj�
takie z rozdzielonym rdzeniem i interfejsem graficznym. Sancho
dostarcza �atwy w u�yciu, pot�ny i konfigurowalny interfejs
graficzny, aktualnie obs�uguj�cy protok� GUI popularnego rdzenia
mldonkey.

%prep
%setup -q -n %{name}-%{version}-%{_pver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir}}

install sancho-bin $RPM_BUILD_ROOT%{_bindir}/sancho
install lib/libgcc_s.so.1 $RPM_BUILD_ROOT%{_libdir}/%{name}
install lib/libgcj.so.6.0.0 $RPM_BUILD_ROOT%{_libdir}/%{name}
install lib/libswt-fox-3000r4.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install distrib/sancho*.properties $RPM_BUILD_ROOT%{_datadir}/%{name}
install distrib/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if ! grep -qs '^%{_libdir}/%{name}$' /etc/ld.so.conf ; then
	echo "%{_libdir}/%{name}" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
umask 022
if [ "$1" = '0' ]; then
	grep -v '^%{_libdir}/%{name}$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc distrib/AUTHORS distrib/ChangeLog distrib/README distrib/LICENSE.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
