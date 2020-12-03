from docx import Document
from run_tools import split_run_by
from docx.enum.text import WD_COLOR_INDEX


d = Document('test1.docx')

par = d.paragraphs[0]
run = par.runs[1]

new_runs = split_run_by(par, run, (1, 2))
new_runs[0].font.highlight_color = WD_COLOR_INDEX.RED
new_runs[1].font.highlight_color = WD_COLOR_INDEX.YELLOW
new_runs[2].font.highlight_color = WD_COLOR_INDEX.GREEN

d.save('test1-highlightened.docx')
