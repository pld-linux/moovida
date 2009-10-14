%define		module_name	elisa
Summary:	Media center
Summary(pl.UTF-8):	Centrum multimedialne
Name:		moovida
Version:	1.0.7
Release:	2
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
# Source0-md5:	976c548c5c46bd217117be73e21c3374
URL:		http://www.moovida.com/
BuildRequires:	python-TwistedCore >= 8.0.0
BuildRequires:	python-gstreamer >= 0.10.9
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	gstreamer-plugins-good >= 0.10.10-1
Requires:	libvisual-plugins >= 0.4
#Requires:	python-PIL
Requires:	python-TwistedCore >= 8.0.0
Requires:	python-TwistedCore-ssl >= 8.0.0
Requires:	python-TwistedWeb >= 8.0.0
Requires:	python-TwistedWeb2 >= 8.0.0
Requires:	python-pycairo
Requires:	python-cssutils >= 0.9.5.1
#Requires:	python-encutils
#Requires:	python-gstreamer >= 0.10.9
Requires:	python-pygtk-gtk >= 2.0
Requires:	python-pigment >= 0.3.12
#Requires:	python-pygobject
#Requires:	python-pymetar
Requires:	python-setuptools
Requires:	python-simplejson
Requires:	python-sqlite
Suggests:	gstreamer-plugins-bad
Suggests:	gstreamer-plugins-ugly
Suggests:	gstreamer-ffmpeg
Suggests:	moovida-plugins-good
Suggests:	moovida-plugins-bad
Suggests:	moovida-plugins-ugly
Suggests:	python-coherence
Suggests:	python-gpod
Suggests:	python-dbus
Suggests:	python-xdg
Suggests:	xdg-user-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elisa is a project to create an open source cross platform media
center solution.

%description -l pl.UTF-8
Elisa jest projektem stworzenia wieloplatformowego centrum
multimedialnego o otwartych źródłach.

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/plugins

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
In order to have Moovida user interface, install moovida-plugins-bad.
EOF

%files
%defattr(644,root,root,755)
# COPYING contains just some notes, LICENSE.GPL includes excemption clause 
%doc AUTHORS COPYING FAQ* LICENSE.* NEWS README FIRST_RUN
%attr(755,root,root) %{_bindir}/%{module_name}*
%{py_sitescriptdir}/%{module_name}
%{py_sitescriptdir}/%{module_name}*.egg-info
%{py_sitescriptdir}/%{module_name}*.pth
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-mobile.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/dbus-1/services/com.fluendo.%{module_name}.service
%{_mandir}/man1/%{name}*
