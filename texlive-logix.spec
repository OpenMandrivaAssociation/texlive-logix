%global tl_name logix
%global tl_revision 63688

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	Supplement to the Unicode math symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/logix
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Unicode font with over 4,000 symbols to
supplement the Unicode math symbols. It is compatible with and
complements the AMS STIX2 math fonts, but focuses on new symbols and
symbol variants more suited to work in logic.

