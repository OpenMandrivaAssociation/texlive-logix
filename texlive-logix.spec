Name:		texlive-logix
Version:	63688
Release:	2
Summary:	Supplement to the Unicode math symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logix
License:	ofl lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logix.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a Unicode font with over 4,000 symbols to
supplement the Unicode math symbols. It is compatible with and
complements the AMS STIX2 math fonts, but focuses on new
symbols and symbol variants more suited to work in logic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/logix
%{_texmfdistdir}/fonts/truetype/public/logix
%{_texmfdistdir}/fonts/opentype/public/logix
%doc %{_texmfdistdir}/doc/fonts/logix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
