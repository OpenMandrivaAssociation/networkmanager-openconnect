%define nm_version          0.9.6.0
%define dbus_version        1.1
%define openconnect_version 3.01
%define gtk3_version        3.0

Summary:	NetworkManager VPN integration for openconnect
Name:		networkmanager-openconnect
Version:	0.9.6.2
Release:	2
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/NetworkManager-openconnect-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: intltool
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(libpng15)
BuildRequires: pkgconfig(openconnect)
BuildRequires: pkgconfig(gconf-2.0)
Requires: gtk+3             >= %{gtk3_version}
Requires: dbus
Requires: NetworkManager   >= %{nm_version}
Requires: openconnect      >= %{openconnect_version}
Obsoletes: openconnect-nm-auth-dialog

%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -qn NetworkManager-openconnect-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-gnome \
	--with-authdlg \
	--enable-more-warnings=no \
    --with-gtkver=3
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/libnm-openconnect-properties.la

%find_lang NetworkManager-openconnect

%pre
%{_sbindir}/groupadd -r nm-openconnect &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d / -M \
                     -c 'NetworkManager user for OpenConnect' \
                     -g nm-openconnect nm-openconnect &>/dev/null || :

%files -f NetworkManager-openconnect.lang
%doc AUTHORS ChangeLog COPYING
%{_libdir}/NetworkManager/lib*.so*
%{_libdir}/nm-openconnect-auth-dialog
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_datadir}/gnome-vpn-properties/openconnect



%changelog
* Thu Aug 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.6.2-1
+ Revision: 813348
- update to new version 0.9.6.2
- update to new version 0.9.6.0

* Fri Feb 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.2.0-1
+ Revision: 780661
- added patches 0 & 1 to fix build
- moved to build 0.9.2.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - 0.8.6.0
    - 0.9.2.0

* Thu Apr 21 2011 Funda Wang <fwang@mandriva.org> 0.8.4-1
+ Revision: 656406
- disable warnings
- bump req
- new verison 0.8.4

* Tue Mar 15 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 0.8.3.995-3
+ Revision: 645114
- P0: really build authentication dialogue (GIT)
- P1: fix format not literal warning
- BR openconnect-static-devel for authentication library

* Tue Mar 15 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 0.8.3.995-2
+ Revision: 644985
- obsoletes openconnect-nm-auth-dialog

* Sat Mar 05 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 0.8.3.995-1
+ Revision: 642111
- update to 0.8.4-beta1

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-2mdv2011.0
+ Revision: 603025
- dependency on openconnect-nm-auth-dialog

* Wed Nov 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 598377
- import networkmanager-openconnect

