%define xsessiondir %{_datadir}/xsessions

Name:           ratpoison
Version:        1.4.0
Release:        3%{?dist}
Summary:        Minimalistic window manager
Group:          Applications/Productivity
License:        GPL
URL:            http://www.nongnu.org/ratpoison/
Source0:        http://savannah.nongnu.org/download/ratpoison/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %{fedora} <= 4 
BuildRequires:  xorg-x11-devel, readline-devel
%else
BuildRequires: libX11-devel, readline-devel, libXtst-devel
%endif
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
Ratpoison is a simple window manager that relies solely on keyboard input as
opposed to keyboard and mouse input.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{xsessiondir}
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{xsessiondir}/
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/allwindows.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/clickframe.pl
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/genrpbindings
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpshowall.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpws
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/split.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%defattr(-,root,root,-)
%{_bindir}/ratpoison
%{_bindir}/rpws
%doc %{_datadir}/doc/ratpoison/
%{_infodir}/ratpoison.info.gz
%{_mandir}/man1/ratpoison.1.gz
%{_datadir}/ratpoison/
%{_datadir}/xsessions/ratpoison.desktop

%changelog
* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-3
- Permissions fixes

* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-2
- install-info fixup
- BuildRequires fixup

* Fri Apr  7 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-1
- Bumped to 1.4.0-1 from 1.3.0-2
- Conditional BuildRequires for FC4-- versus FC5++
- Various fixes per bugzilla review

* Mon Mar 13 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-2
- Added ratpoison.desktop file

* Sun Feb 19 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-1
- Initial specfile build for FE(4)
