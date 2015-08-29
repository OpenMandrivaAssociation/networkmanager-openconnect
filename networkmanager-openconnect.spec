%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for openconnect
Name:		networkmanager-openconnect
Version:	1.0.2
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
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openconnect)
BuildRequires:	pkgconfig(libsecret-unstable)
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
%apply_patches

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
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%{_libdir}/NetworkManager/lib*.so*
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_datadir}/gnome-vpn-properties/openconnect

