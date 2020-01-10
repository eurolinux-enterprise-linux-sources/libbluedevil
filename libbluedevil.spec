
Name:           libbluedevil
Version:        1.9.2
Release:        4%{?dist}
Summary:        A Qt wrapper for bluez

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://projects.kde.org/projects/playground/libs/libbluedevil 

Source0:        ftp://ftp.kde.org/pub/kde/stable/libbluedevil/%{version}/src/libbluedevil-%{version}.tar.bz2
# git archive --format=tar --remote=git://anongit.kde.org/libbluedevil v1.9s /
# --prefix=libbluedevil-v1.9/ -o libbluedevil-v1.9.tgz
# tar xvzf libbluedevil-v1.9.tgz
# rm libbluedevil-v1.9/qt4.tag
# tar cjvf libbluedevil-v1.9-%{snapshot}.tar.bz2 libbluedevil-v1.9/
#Source0:        libbluedevil-v%{version}-%{snapshot}.tar.bz2
## match ExcludeArch for obexd and friends
ExcludeArch:    s390 s390x

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt4-devel
BuildRequires:  automoc4
BuildRequires:  cmake

Requires:       bluez

%description
%{name} is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%setup -q 


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libbluedevil.so.1*

%files devel
%defattr(-,root,root,-)
%doc HACKING
%{_includedir}/bluedevil/
%{_libdir}/libbluedevil.so
%{_libdir}/pkgconfig/bluedevil.pc


%changelog
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
