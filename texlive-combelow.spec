Name:		texlive-combelow
Version:	18462
Release:	2
Summary:	Typeset "comma-below" letters, as in Romanian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/combelow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \cb that positions a comma below
a letter, as required (for example) in Romanian typesetting.
The command is robust, but interferes with hyphenation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/combelow/combelow.sty
%doc %{_texmfdistdir}/doc/latex/combelow/README
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.bib
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.pdf
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
