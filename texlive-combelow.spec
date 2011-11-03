# revision 18462
# category Package
# catalog-ctan /macros/latex/contrib/combelow
# catalog-date 2010-05-24 13:39:10 +0200
# catalog-license lppl1.3
# catalog-version 0.99f
Name:		texlive-combelow
Version:	0.99f
Release:	1
Summary:	Typeset "comma-below" letters, as in Romanian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combelow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a command \cb that positions a comma below
a letter, as required (for example) in Romanian typesetting.
The command is robust, but interferes with hyphenation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/combelow/combelow.sty
%doc %{_texmfdistdir}/doc/latex/combelow/README
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.bib
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.pdf
%doc %{_texmfdistdir}/doc/latex/combelow/combelow.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
