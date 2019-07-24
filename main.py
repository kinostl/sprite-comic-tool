from pgmagick import Image, CompositeOperator as co, DrawableText

script="""#Sonic says Hello
%kinostl
snow
---
sonic: Hello MG!
sonic, eating: This is my food.
---
sonic, scared: Don't hurt me.
"""

split_script = script.split('---')

comic_info = split_script[0].split('\n')
title = comic_info[0].strip()
author = comic_info[1].strip()
background = comic_info[2].strip()

del split_script[0]
panels=[]
for panel in split_script:
    lines=[]
    line_inputs = list(filter(None,panel.split('\n')))
    for line_input in line_inputs:
        split_line_input = line_input.split(':')
        actor = split_line_input[0]
        line = split_line_input[1]
        if "," in actor:
            split_actor = actor.split(",")
            actor = split_actor[0]
            attitude = split_actor[1]
        else:
            attitude = "neutral"
        lines.append({
            "actor": actor.strip(),
            "attitude": attitude.strip(),
            "line": line.strip()
        })
    panels.append(lines)

num = 0
for panel in panels:
    bg = Image('backgrounds/{}.png'.format(background))
    line_num=1
    for line in panel:
        actor = Image('sprites/{}/{}.png'.format(line['actor'],line['attitude']))
        draw_line = DrawableText(20*line_num, 95, line['line'])
        bg.composite(actor, 20*line_num, 100, co.OverCompositeOp)
        bg.draw(draw_line)
        line_num = line_num+4
    bg.write('output{}.png'.format(num))
    num = num+1