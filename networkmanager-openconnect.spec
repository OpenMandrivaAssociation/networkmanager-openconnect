%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for openconnect
Name:		networkmanager-openconnect
Version:	1.2.6
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/%{url_ver}/NetworkManager-openconnect-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openconnect)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnm)
Requires:	gtk+3
Requires:	dbus
Requires:	NetworkManager
Requires:	openconnect
Obsoletes:	openconnect-nm-auth-dialog

%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -qn NetworkManager-openconnect-%{version}
%autopatch -p1

%build
%configure \
	--disable-static \
	--with-gnome \
	--with-authdlg \
	--enable-more-warnings=no \
	--with-gtkver=3
%make

%install
%makeinstall_std

%find_lang NetworkManager-openconnect

%pre
%{_sbindir}/groupadd -r nm-openconnect &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d / -M \
                     -c 'NetworkManager user for OpenConnect' \
                     -g nm-openconnect nm-openconnect &>/dev/null || :

%files -f NetworkManager-openconnect.lang
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf
%{_libdir}/NetworkManager/lib*.so*
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_datadir}/gnome-vpn-properties/openconnect
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_datadir}/appdata/network-manager-openconnect.metainfo.xml
