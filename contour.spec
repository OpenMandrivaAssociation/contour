Summary:	A context sensitive user interface for Plasma Active
Name:		contour
Version:	0.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/Plasma/Active/Contour
Source0:	http://download.kde.org/stable/active/3.0/src/%{name}-%{version}.tar.xz
Patch0:		qtmobility.diff
Patch1:		contour-0.1.1-find-qtmobility.patch
Patch100:	changeset_rd5306e452fd64f8bcb2dab6d5cef770584131486.diff
Patch101:	changeset_r688e2a2ce823d99e5ca1def1861fdf7591603cf2.diff
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-runtime-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(NetworkManagerQt)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(soprano)
Requires:	kdebase4-runtime

%description
Contour contributes a new usage paradigm using adaptive activities and
intelligent recommendations. Contour creates a context-sensitive user
interface that adapts to current context, current activities and behavioral
patterns of the user.

Contour is part of Plasma Active project.

%files
%{_kde_bindir}/contour
%{_kde_libdir}/kde4/*.so
%{_kde_appsdir}/contour
%{_kde_appsdir}/plasma/packages/org.kde.contour.recommendations
%{_kde_appsdir}/plasma/services/recommendations.operations
%{_kde_datadir}/autostart/contour.desktop
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#----------------------------------------------------------------------------

%package devel
Summary:	%{name} development files
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
%{name} development files.

%files devel
%{_datadir}/cmake/Contour

#----------------------------------------------------------------------------

%prep
%setup -q

# FindQtMobility is under review for inclusion to kdelibs, not needed
# by any other package
# TODO: remove once included in kdelibs
%patch0 -p1
%patch1 -p1 -b .find-qtmobility

# Upstream patches
%patch100 -p1 -b .makefile
%patch101 -p1 -b .notifier

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

