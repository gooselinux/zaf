Name: zaf
Summary: South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release: 0.3.%{upstreamid}svn.1%{?dist}
Source: zaf-0-0.1.%{upstreamid}svn.tar.bz2
Group: Applications/Text
URL: http://zaf.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

%description
South Africa hyphenation rules.

%package -n hyphen-af
Summary: Afrikaans hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-af
Afrikaans hyphenation rules.

%package -n hyphen-zu
Summary: Zulu hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-zu
Zulu hyphenation rules.

%prep
%setup -q -n zaf

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./af/hyph/hyph_af_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./zu/hyph/hyph_zu_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s hyph_af_ZA.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files -n hyphen-af
%defattr(-,root,root,-)
%doc af/CREDITS af/COPYING af/README
%{_datadir}/hyphen/hyph_af*

%files -n hyphen-zu
%defattr(-,root,root,-)
%doc zu/CREDITS zu/COPYING zu/README
%{_datadir}/hyphen/hyph_zu*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0-0.3.20080714svn.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Caolan McNamara <caolanm@redhat.com> - 0-0.1.20080714svn
- latest version

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0-0.1.20071123svn
- initial version
