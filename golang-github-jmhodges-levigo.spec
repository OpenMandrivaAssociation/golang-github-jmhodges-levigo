# http://github.com/jmhodges/levigo

%global goipath         github.com/jmhodges/levigo
%global commit          253793d7b92ea4d3a5e2e4368691c52e70f2c6fc


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.15%{?dist}
Summary:        Go wrapper for LevelDB
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: leveldb-devel >= 1.7

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.git253793d
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20140826git253793d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git253793d
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git253793d
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git253793d
- Update to spec-2.1
  related: #1250488

* Tue Aug 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git253793d
- Add missing deps on leveldb-devel
  resolves: #1250488

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git253793d
- Update spec file to spec-2.0
  resolves: #1250488

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git253793d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git253793d
- First package for Fedora

