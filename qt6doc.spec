#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v22
# autospec commit: 247c192
#
Name     : qt6doc
Version  : 6.9.0
Release  : 24
URL      : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtdoc-everywhere-src-6.9.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtdoc-everywhere-src-6.9.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC-BY-SA-4.0 GFDL-1.3 GPL-3.0 MIT
Requires: qt6doc-lib = %{version}-%{release}
Requires: qt6doc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6base-staticdev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
To Generate Qt Documentation:
qtdoc contains the main Qt Reference Documentation, which includes
overviews, Qt topics, and examples not specific to any Qt module.The
configuration files are located in qtdoc/doc/config and the articles in
qtdoc/doc/src. Note that QDoc is located in qttools/src/qdoc.

%package dev
Summary: dev components for the qt6doc package.
Group: Development
Requires: qt6doc-lib = %{version}-%{release}
Provides: qt6doc-devel = %{version}-%{release}
Requires: qt6doc = %{version}-%{release}

%description dev
dev components for the qt6doc package.


%package lib
Summary: lib components for the qt6doc package.
Group: Libraries
Requires: qt6doc-license = %{version}-%{release}

%description lib
lib components for the qt6doc package.


%package license
Summary: license components for the qt6doc package.
Group: Default

%description license
license components for the qt6doc package.


%prep
%setup -q -n qtdoc-everywhere-src-6.9.0
cd %{_builddir}/qtdoc-everywhere-src-6.9.0
pushd ..
cp -a qtdoc-everywhere-src-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743643147
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743643147
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6doc
cp %{_builddir}/qtdoc-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6doc/9e132ef44ef2f5e72f4e3681765591005694515e || :
cp %{_builddir}/qtdoc-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6doc/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtdoc-everywhere-src-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/qt6doc/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/qtdoc-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6doc/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtdoc-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6doc/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtdoc-everywhere-src-%{version}/doc/src/legal/licenses.qdoc %{buildroot}/usr/share/package-licenses/qt6doc/0ca06fe2f7efe4bb63167c55c5ca284e0dd42494 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/qt6/mkspecs/qtdoc_dummy_file.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/sbom/qtdoc-6.9.0.spdx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6doc/0ca06fe2f7efe4bb63167c55c5ca284e0dd42494
/usr/share/package-licenses/qt6doc/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6doc/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6doc/9e132ef44ef2f5e72f4e3681765591005694515e
/usr/share/package-licenses/qt6doc/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6doc/f26cccd93362d640ef2c05d1c52b5efe1620a9b2
