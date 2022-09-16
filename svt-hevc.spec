%global real_name SVT-HEVC

Name:           svt-hevc
Version:        1.5.1
Release:        3%{?dist}
Summary:        Scalable Video Technology for HEVC Encoder
License:        BSD-2-Clause-Patent
URL:            https://github.com/OpenVisualCloud/%{real_name}
ExclusiveArch:  x86_64

Source0:        %{url}/archive/v%{version}/%{real_name}-%{version}.tar.gz
# Build GStreamer plugin from tree directly:
Patch0:         %{name}-gst.patch
Patch1:         %{url}/commit/952d4b3b7ee29ee82d09c3803ec0e2217ae5f4b8.patch
Patch2:         %{url}/commit/a7422886a66b74a27324ac43b26ba2ae3dc67c04.patch

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.8
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.8
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.8
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.8
BuildRequires:  yasm

%description
The Scalable Video Technology for HEVC Encoder (SVT-HEVC Encoder) is an HEVC
compliant encoder library core that achieves excellent density/quality
tradeoffs, and is highly optimized for Intel® Xeon™ Scalable Processor and Xeon™
D processors.

%package        libs
Summary:        %{name} libraries

%description    libs
The Scalable Video Technology for HEVC Encoder (SVT-HEVC Encoder) libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n     gstreamer1-%{name}
Summary:        GStreamer 1.0 %{real_name} plug-in
Requires:       gstreamer1-plugins-base%{?_isa} >= 1.8

%description -n gstreamer1-%{name}
This package provides an %{real_name} based GStreamer plug-in.

%prep
%autosetup -p1 -n %{real_name}-%{version}

%build
# Do not use 'Release' build or it hardcodes compiler settings:
%cmake -DCMAKE_BUILD_TYPE='Fedora'
%cmake_build

pushd gstreamer-plugin
export LIBRARY_PATH="$PWD/../Bin/Fedora:$LIBRARY_PATH"
%meson
%meson_build
popd

%install
%cmake_install
pushd gstreamer-plugin
%meson_install
popd

%files
%{_bindir}/SvtHevcEncApp

%files libs
%license LICENSE.md
%doc README.md Docs
%{_libdir}/libSvtHevcEnc.so.1*

%files devel
%{_includedir}/svt-hevc
%{_libdir}/libSvtHevcEnc.so
%{_libdir}/pkgconfig/SvtHevcEnc.pc

%files -n gstreamer1-%{name}
%{_libdir}/gstreamer-1.0/libgstsvthevcenc.so

%changelog
* Fri Sep 16 2022 Simone Caronni <negativo17@gmail.com> - 1.5.1-3
- Add upstream patches.
- Clean up SPEC file and split it depending on branch.

* Sun Oct 24 2021 Simone Caronni <negativo17@gmail.com> - 1.5.1-2
- Do not build Gstreamer plugin on Fedora 35+.

* Sat Jul 24 2021 Simone Caronni <negativo17@gmail.com> - 1.5.1-1
- Update to 1.5.1.

* Thu Nov 26 2020 Simone Caronni <negativo17@gmail.com> - 1.5.0-1
- First build, make it build also on CentOS/RHEL 7 with rebased GStreamer.
