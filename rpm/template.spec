Name:           ros-melodic-plotjuggler
Version:        1.8.4
Release:        0%{?dist}
Summary:        ROS plotjuggler package

Group:          Development/Libraries
License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       ros-melodic-ros-type-introspection
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-rosbag-storage
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-rostime
Requires:       ros-melodic-topic-tools
BuildRequires:  binutils-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-ros-type-introspection
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-rosbag-storage
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-rostime
BuildRequires:  ros-melodic-topic-tools

%description
PlotJuggler: juggle with data

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Sep 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.4-0
- Autogenerated by Bloom

* Fri Aug 24 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.3-0
- Autogenerated by Bloom

* Sun Aug 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.2-0
- Autogenerated by Bloom

* Sat Aug 18 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.1-0
- Autogenerated by Bloom

* Fri Aug 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.0-0
- Autogenerated by Bloom

* Sun Aug 12 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.3-0
- Autogenerated by Bloom

* Fri Aug 10 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.2-0
- Autogenerated by Bloom

* Sun Jul 22 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.1-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.0-0
- Autogenerated by Bloom

