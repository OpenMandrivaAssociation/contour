Name: contour
Version: 0.3.12.262
Release: 1
Source0: https://github.com/contour-terminal/contour/archive/refs/tags/v%{version}.tar.gz
# libunicode really doesn't like being a system library (conflicts with ICU)
Source1: https://github.com/contour-terminal/libunicode/archive/refs/tags/v0.2.1.tar.gz
Patch0: https://github.com/contour-terminal/contour/commit/782fb7248d6fe643e7163bf57b0bcef50a81a8f7.patch
Patch1: contour-0.3.12.262-compile.patch
Summary: Contour Terminal Emulator
URL: https://contour-terminal.org/
License: Apache-2.0
Group: System/X11
BuildRequires: cmake ninja
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Catch2)
BuildRequires: cmake(libunicode)
BuildRequires: cmake(microsoft.gsl)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: range-v3-devel
BuildRequires: pkgconfig(yaml-cpp)

%description

%prep
%autosetup -p1
# Adapt to newer Catch2
find . -name "*.cpp" -o -name "*.h" |xargs sed -i -e 's,catch2/catch.hpp,catch2/catch_all.hpp,'
%cmake \
	-DCONTOUR_QT_VERSION=6 \
	-DCMAKE_CXX_STANDARD=17 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license %{_datadir}/contour/LICENSE.txt
%{_bindir}/contour
%{_datadir}/applications/org.contourterminal.Contour.desktop
%dir %{_datadir}/contour
%doc %{_datadir}/contour/README.md
%{_datadir}/contour/shell-integration
%{_datadir}/icons/hicolor/*/apps/org.contourterminal.Contour.*
%{_datadir}/kservices5/ServiceMenus/org.contourterminal.Contour.OpenHere.desktop
%{_datadir}/kservices5/ServiceMenus/org.contourterminal.Contour.RunIn.desktop
%{_datadir}/metainfo/org.contourterminal.Contour.metainfo.xml
%{_datadir}/terminfo/c/contour
%{_datadir}/terminfo/c/contour-latest
