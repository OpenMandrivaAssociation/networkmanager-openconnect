%define nm_version          0.9.2.0
%define dbus_version        1.1
%define openconnect_version 3.01

Summary:	NetworkManager VPN integration for openconnect
Name:		networkmanager-openconnect
Version:	0.9.6.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/NetworkManager-openconnect-%{version}.tar.xz
# ca8a39d1bb999ba98ead45e53041fc3ea28ecd5c 
Patch0:	NetworkManager-openconnect-0.9.2.0-fix-headers-usage.patch
# c6d92c3e64898ea62789def04b86752dec904326
Patch1:	NetworkManager-openconnect-0.9.2.0-drop-g_thread_init.patch
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(libpng15)
BuildRequires: pkgconfig(openconnect)
Requires: gtk+3
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
	--enable-more-warnings=no
%make

%install
rm -rf %{buildroot}
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

