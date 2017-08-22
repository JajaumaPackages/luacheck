%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define debug_package %{nil}

Name:           luacheck
Version:        0.20.0
Release:        1%{?dist}
Summary:        A static analyzer and a linter for Lua

License:        MIT
URL:            https://github.com/mpeterv/luacheck
Source0:        https://github.com/mpeterv/luacheck/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       lua-filesystem
Requires:       lua

%description
Luacheck is a command-line tool for linting and static analysis of Lua code. It
is able to spot usage of undefined global variables, unused local variables and
a few other typical problems within Lua programs.

%prep
%setup -q -n luacheck-%{version}


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{luapkgdir}

install -p -m 755 bin/luacheck.lua %{buildroot}%{_bindir}/luacheck
cp -a src/luacheck %{buildroot}%{luapkgdir}


%files
%doc README.md
%license LICENSE
%{_bindir}/luacheck
%{luapkgdir}/luacheck/


%changelog
* Tue Aug 22 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.20.0-1
- Update to latest upstream release

* Fri May 13 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.15.0-1
- Public release
