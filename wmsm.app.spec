Summary:	System monitor dock app
Summary(pl.UTF-8):	Aplet monitorujący system
Name:		wmsm.app
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.unetz.com/schaepe/DOCKAPPS/%{name}-%{version}.tar.bz2
# Source0-md5:	3e808aa1b433315c95321555eb63aa90
Source1:	%{name}.desktop
URL:		http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmsm.app is a system monitor for WindowMaker and other compatble
window managers.

%description -l pl.UTF-8
Monitor systemu dla WindowMakera i innych kompatybilnych zarządców
okien.

%prep
%setup -q

%build
%{__make} -C wmsm \
	CFLAGS="%{rpmcflags}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install wmsm/wmsm $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
