%global real_name SVT-HEVC

Name:           svt-hevc
Version:        1.5.1
Release:        3%{?dist}
Summary:        Scalable Video Technology for HEVC Encoder
License:        BSD-2-Clause-Patent
URL:            https://github.com/OpenVisualCloud/%{real_name}
ExclusiveArch:  x86_64

Source0:        %{url}/archive/v%{version}/%{real_name}-%{version}.tar.gz
Patch1:         %{url}/commit/952d4b3b7ee29ee82d09c3803ec0e2217ae5f4b8.patch
Patch2:         %{url}/commit/a7422886a66b74a27324ac43b26ba2ae3dc67c04.patch

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc
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

%prep
%autosetup -p1 -n %{real_name}-%{version}

%build
# Do not use 'Release' build or it hardcodes compiler settings:
%cmake -DCMAKE_BUILD_TYPE='Fedora'
%cmake_build

%install
%cmake_install

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
