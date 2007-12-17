Summary:	Reactive Autonomous Blackhole List (RABL) client
Name:		rabl_client
Version:	1.0.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.nuclearelephant.com/projects/rabl/
Source0:	http://www.nuclearelephant.com/projects/rabl/sources/%{name}-%{version}.tar.bz2

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
