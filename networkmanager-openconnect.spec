%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for openconnect
Name:		networkmanager-openconnect
Version:	1.2.8
Release:	2
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/%{url_ver}/NetworkManager-openconnect-%{version}.tar.xz
Source1:	%{name}.sysusers
Patch0:		https://gitlab.gnome.org/GNOME/NetworkManager-openconnect/-/commit/205d33d370092230b104276a1d5a78cfe5e7fe80.patch
Patch1:		https://gitlab.gnome.org/GNOME/NetworkManager-openconnect/-/commit/9104cc89a879d4894c0998c8d71e42ae6b36b786.patch
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libnma)
BuildRequires:	pkgconfig(openconnect)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnm)
Requires:	gtk+3
Requires:	gtk4
Requires:	dbus
Requires:	NetworkManager
Requires:	openconnect
Obsoletes:	openconnect-nm-auth-dialog
Requires(pre):	systemd

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
	--with-gtkver=3 \
	--with-gtk4

%make_build

%install
%make_install

%find_lang NetworkManager-openconnect
install -Dm 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_package %{name}.conf %{SOURCE1}

%files -f NetworkManager-openconnect.lang
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf
%{_sysusersdir}/%{name}.conf
%{_libdir}/NetworkManager/lib*.so*
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
#{_datadir}/gnome-vpn-properties/openconnect
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_datadir}/appdata/network-manager-openconnect.metainfo.xml
