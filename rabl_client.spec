Summary:	Reactive Autonomous Blackhole List (RABL) client
Name:		rabl_client
Version:	1.0.0
Release:	%mkrel 4
License:	GPL
Group:		System/Servers
URL:		http://www.nuclearelephant.com/projects/rabl/
Source0:	http://www.nuclearelephant.com/projects/rabl/sources/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Reactive Autonomous Blackhole List (RABL) client.

%prep

%setup -q

%build

%configure2_5x \
    --enable-warnings

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}

install -m0755 rabl_client %{buildroot}%{_bindir}/
install -m0644 rabl_client.conf %{buildroot}%{_sysconfdir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGE LICENSE README RELEASE.NOTES
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/rabl_client.conf
%attr(0755,root,root) %{_bindir}/rabl_client


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-4mdv2010.0
+ Revision: 433048
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-3mdv2009.0
+ Revision: 242530
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 25471
- Import rabl_client



* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- new name (was sbl_client)

* Mon Mar 14 2005 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.0-1mdk
- initial package
