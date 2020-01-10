
%define stable stable

Name:           libbluedevil
Version:        2.1
Release:        1%{?dist}
Summary:        A Qt wrapper for bluez

License:        LGPLv2+
URL:            https://projects.kde.org/projects/playground/libs/libbluedevil 

%if 0%{?snap}
# git archive --format=tar --remote=git://anongit.kde.org/libbluedevil bluez5  --prefix=libbluedevil-%{version}/ | xz ...
Source0:        libbluedevil-%{version}-%{snap}.tar.xz
%else
Source0: http://download.kde.org/%{stable}/libbluedevil/%{version}%{?pre:-%{pre}}/src/libbluedevil-%{version}%{?pre:-%{pre}}.tar.xz
%endif

## upstream patches
Patch1: 0001-Adapter-Add-back-alias-and-setAlias-for-binary-compa.patch
Patch2: 0002-Delete-adapter-only-after-all-devices-from-the-adapt.patch
Patch3: 0003-Only-delete-adapter-when-removed-from-m_adapters-has.patch

ExcludeArch:    s390 s390x

BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  pkgconfig(QtCore) pkgconfig(QtDBus)

Requires:       bluez >= 5

%description
%{name} is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -n libbluedevil-%{version}%{?pre:-%{pre}} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libbluedevil.so.2*

%files devel
%doc HACKING
%{_includedir}/bluedevil/
%{_libdir}/libbluedevil.so
%{_libdir}/pkgconfig/bluedevil.pc


%changelog
* Mon May 25 2015 Jan Grulich <jgrulich@redhat.com> - 2.1-1
- Re-base to 2.1 (sync with F21)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.9.2-5
- Mass rebuild 2013-12-27

* Wed Jun 19 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.2-4
- ExcludeArch: s390 s390x (#975736)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Rex Dieter <rdieter@fedoraproject.org> 1.9.2-1
- 1.9.2

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> 1.9.1-1
- 1.9.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-0.2.20110502git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 02 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.9-0.1
- update to pre-release snapshot of 1.9

* Mon Mar 28 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.8.1-1
- update to 1.8.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.8-3
- update to 1.8-1 (respin?)

* Wed Sep 29 2010 jkeating - 1.8-2
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.8-1
- update to 1.8

* Fri Aug 13 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.7-1
- initial package
