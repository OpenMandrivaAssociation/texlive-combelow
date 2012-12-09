# revision 18462
# category Package
# catalog-ctan /macros/latex/contrib/combelow
# catalog-date 2010-05-24 13:39:10 +0200
# catalog-license lppl1.3
# catalog-version 0.99f
Name:		texlive-combelow
Version:	0.99f
Release:	2
Summary:	Typeset "comma-below" letters, as in Romanian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combelow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combelow.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.99f-2
+ Revision: 750380
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.99f-1
+ Revision: 718103
- texlive-combelow
- texlive-combelow
- texlive-combelow
- texlive-combelow

