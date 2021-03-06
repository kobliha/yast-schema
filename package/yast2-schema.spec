#
# spec file for package yast2-schema
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-schema
Version:        3.1.5
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:	        System/YaST
License:        GPL-2.0+

Url:            https://github.com/yast/yast-schema

# Dependencies needed to build the package
BuildRequires:	trang yast2-devtools yast2-testsuite

# All packages providing RNG files for AutoYaST
# in /usr/share/YaST2/schema/autoyast/rng/*.rng
BuildRequires: autoyast2
BuildRequires: yast2
BuildRequires: yast2-add-on
BuildRequires: yast2-audit-laf
BuildRequires: yast2-auth-client
BuildRequires: yast2-auth-server
BuildRequires: yast2-bootloader
BuildRequires: yast2-ca-management
BuildRequires: yast2-country
BuildRequires: yast2-dhcp-server
BuildRequires: yast2-dns-server
BuildRequires: yast2-firewall
BuildRequires: yast2-firstboot
BuildRequires: yast2-ftp-server
BuildRequires: yast2-http-server
BuildRequires: yast2-inetd
BuildRequires: yast2-installation
BuildRequires: yast2-iscsi-client
BuildRequires: yast2-kdump
BuildRequires: yast2-mail
BuildRequires: yast2-network
BuildRequires: yast2-nfs-client
BuildRequires: yast2-nfs-server
BuildRequires: yast2-nis-client
BuildRequires: yast2-nis-server
BuildRequires: yast2-ntp-client
BuildRequires: yast2-online-update-configuration
BuildRequires: yast2-printer
BuildRequires: yast2-proxy
# Available on SLE (12) only
%if !0%{?is_opensuse}
BuildRequires: yast2-registration
%endif
# Package available for S390 only
%ifarch s390 s390x
BuildRequires: yast2-s390
%endif
BuildRequires: yast2-samba-client
BuildRequires: yast2-samba-server
BuildRequires: yast2-security
BuildRequires: yast2-services-manager
BuildRequires: yast2-sound
BuildRequires: yast2-squid
BuildRequires: yast2-sysconfig
BuildRequires: yast2-users


#!BuildIgnore: yast2-build-test

# optimization suggested by AJ:
#!BuildIgnore: tomcat5

# ignoring conflicting packages
#!BuildIgnore: yast2-branding-SLED yast2-branding-openSUSE
#!BuildIgnore: yast2-theme yast2-theme-SLED yast2-theme-openSUSE yast2-theme-SLE

# Hotfix to build a package, bnc #427684
#!BuildIgnore: xerces-j2-bootstrap libusb-0_1-4 crimson

# To speedup && to easily recover from dependency hell
#!BuildIgnore: yast2-pkg-bindings zypper libzypp yast2-gtk yast2-qt yast2-ncurses yast2-qt-pkg yast2-ncurses-pkg

# Yast packages without AutoYast support
#!BuildIgnore: yast2-country-data
#!BuildIgnore: yast2-control-center yast2-control-center-gnome yast2-control-center-qt

Summary:	YaST2 - AutoYaST Schema

%description
AutoYaST Syntax Schema

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install


%files
%defattr(-,root,root)
%dir %{yast_schemadir}/autoyast/rnc
%{yast_schemadir}/autoyast/rnc/profile.rnc
%{yast_schemadir}/autoyast/rnc/includes.rnc
%dir %{yast_schemadir}/autoyast/rng
%{yast_schemadir}/autoyast/rng/*.rng
%doc %{yast_docdir} 

