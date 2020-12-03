# python-docx-split-run

Some `python-docx` run manipulation, namely:
* Insert a run into paragraph at given position number
* Insert a run into paragraph before/after an existing run
* Copy run formatting
* Split existing run by indexes, while retaining formatting

Inspired by [#519](https://github.com/python-openxml/python-docx/issues/519) `python-docx` issue discussion.

Project files:
* `run_tools.py`: the actual run manipulation functions, including descriptions
* `test.py`: a simple usage example
* `test1.docx`: used by `test.py`
* `test1-highlightened.docx`, `test1-highlightened-bear.docx`, `test1-highlightened-tobear.docx`: `test.py` created output

