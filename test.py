from docx import Document
from run_tools import *
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import RGBColor


d = Document('test1.docx')

par = d.paragraphs[0]
run = par.runs[1]

new_runs = split_run_by(par, run, (1, 2))
new_runs[0].font.highlight_color = WD_COLOR_INDEX.RED
new_runs[1].font.highlight_color = WD_COLOR_INDEX.YELLOW
new_runs[2].font.highlight_color = WD_COLOR_INDEX.GREEN

d.save('test1-highlightened.docx')

another_run = insert_run_at_position(par, 2, 'e')
copy_run_format(run, another_run)
another_run.font.highlight_color = WD_COLOR_INDEX.PINK

d.save('test1-highlightened-bear.docx')

to_run = insert_run_before(par, run, 'to')
copy_run_format(run, to_run)
to_run.font.highlight_color = WD_COLOR_INDEX.BLACK
to_run.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

d.save('test1-highlightened-tobear.docx')
