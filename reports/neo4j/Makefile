PY=python
PANDOC=pandoc

BASEDIR=$(CURDIR)
TEMPDIR=$(BASEDIR)/temp
INPUTDIR=$(BASEDIR)/source
OUTPUTDIR=$(BASEDIR)/output
STYLEDIR=$(BASEDIR)/style

pdf:
	pp -en "$(INPUTDIR)"/**.md > "$(TEMPDIR)"/merged.md
	pandoc "$(TEMPDIR)"/merged.md \
	-S \
	--standalone \
	--filter "$(BASEDIR)/pandoc-minted.py" \
	-o "$(OUTPUTDIR)/report.tex" \
	-H "$(STYLEDIR)/preamble.tex" \
	2>pandoc.log \s
	-V fontsize=12pt \
	-V papersize=a4paper \
	-V documentclass:report \
	-N \
	--verbose
	xelatex -shell-escape "$(OUTPUTDIR)/report.tex"
	mv ./report.* "$(OUTPUTDIR)"

.PHONY: pdf