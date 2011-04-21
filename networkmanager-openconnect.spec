%define nm_version          0.8.3.997
%define dbus_version        1.1
%define gtk2_version        2.10.0
%define openconnect_version 3.01

Summary:   NetworkManager VPN integration for openconnect
Name:      networkmanager-openconnect
Version:   0.8.4
Release:   %mkrel 1
License:   GPLv2+
Group:     System/Base
URL:       http://www.gnome.org/projects/NetworkManager/
Source:    http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/0.8/NetworkManager-openconnect-%{version}.tar.bz2
Patch1: NetworkManager-openconnect-0.8.3.995-format-not-literal.patch
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libnm-util-devel >= %{nm_version}
BuildRequires: libnm-glib-devel >= %{nm_version}
BuildRequires: libnm-glib-vpn-devel >= %{nm_version}
BuildRequires: libGConf2-devel
BuildRequires: gnomeui2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libglade2.0-devel
BuildRequires: libpng-devel
BuildRequires: intltool gettext
BuildRequires: openconnect-static-devel
Requires: gtk2             >= %{gtk2_version}
Requires: dbus             >= %{dbus_version}
Requires: NetworkManager   >= %{nm_version}
Requires: openconnect      >= %{openconnect_version}
Obsoletes: openconnect-nm-auth-dialog
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -q -n NetworkManager-openconnect-%{version}
%patch1 -p1

%build
%configure2_5x --disable-static --with-gnome --with-authdlg
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/libnm-openconnect-properties.la

%find_lang NetworkManager-openconnect

%clean
rm -rf %{buildroot}

%pre
%{_sbindir}/groupadd -r nm-openconnect &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d / -M \
                     -c 'NetworkManager user for OpenConnect' \
                     -g nm-openconnect nm-openconnect &>/dev/null || :

%files -f NetworkManager-openconnect.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_libdir}/NetworkManager/lib*.so*
%{_libdir}/nm-openconnect-auth-dialog
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_datadir}/gnome-vpn-properties/openconnect

