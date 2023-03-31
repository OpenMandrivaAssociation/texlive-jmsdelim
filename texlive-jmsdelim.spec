Name:		texlive-jmsdelim
Version:	62630
Release:	2
Summary:	A package for compositional delimiter sizing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jmsdelim
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmsdelim.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmsdelim.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmsdelim.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Correctly sizing delimiters is very difficult, particularly in
well-architected documents: a correctly engineered mathematical
document will include macros for all operations, and these
macros necessarily will include delimiters (such as
parentheses). However, the correct size for the delimiter
cannot be chosen ahead of time, because it will depend on the
arguments; two options are available: Provide optional
arguments to each notation macro for choosing delimiter sizes.
This is nearly intractable to do in practice. Ignore delimiter
sizes. With jmsdelim we offer an alternative: the correct
delimiter sizes can be set at the leaf nodes of a mathematical
expression, and magically bubble upward through the delimiters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/jmsdelim
%{_texmfdistdir}/tex/latex/jmsdelim
%doc %{_texmfdistdir}/doc/latex/jmsdelim

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
