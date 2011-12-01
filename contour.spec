Name:    contour
Summary: A new and innovative usage paradigm for mobile devices
Version: 0.1.1
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/active/1.0/src/%{name}-%version.tar.bz2

Patch0:  contour-0.1.1-fix-mobility-include.patch

BuildRequires: kdebase4-workspace-devel
BuildRequires: libqt-mobility-devel

%description
A new and innovative usage paradigm for mobile devices

%files
%_kde_bindir/contour
%_kde_libdir/kde4/*.so
%_kde_appsdir/contour
%_kde_appsdir/plasma/packages/org.kde.contour.recommendations
%_kde_appsdir/plasma/services/recommendations.operations
%_kde_datadir/autostart/contour.desktop
%_kde_services/*.desktop
%_kde_servicetypes/*.desktop

#----------------------------------------------------------------------

%package devel
Summary: %{name} development files
Group: Development/Other
Requires: %name = %EVRD

%description devel
%name development files.

%files devel
%_datadir/cmake/Contour

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

