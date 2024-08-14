import pandas as pd
import json
from pprint import pprint

df = pd.read_excel('ALL IN ONE COURSE VIA YOUTUBE.xlsx', sheet_name='Python')

df_temp = df[['TITLE', 'URL', 'Instructor', 'Interview Questions']]

def get_embed_url(in_url):
    if "youtube.com" in in_url:
        in_url = in_url.replace('watch?v=', 'embed/')
    elif "youtu.be" in in_url:
        in_url = in_url.replace('youtu.be/', 'youtube.com/embed/')
    else:
        in_url = 'NA'

    return in_url

df_temp['embed_url'] = df_temp['URL'].apply(get_embed_url)
print(df_temp)

df_temp_dict = df_temp.to_dict(orient='records')
data = []
for d in df_temp_dict:
    print(d['Interview Questions'])
    if d['Interview Questions'] != 'Not Applicable':
        interview_questions = f"<a href='{d['Interview Questions']}' target='_blank'>Interview Questions</a>"
    else:
        interview_questions = 'NA'

    if d['embed_url'] != 'NA':
        embed_code = f"""<iframe class="custom_iframe" height="310" src="{d['embed_url']}" title="{d['TITLE']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
    else:
        embed_code = "NA"

    data.append({
        "TITLE": f"<a href='{d['URL']}' target='_blank'>{d['TITLE']}</a>",
        "INSTRUCTOR": d['Instructor'],
        "INTERVIEW_QUES": interview_questions,
        "EMBED_CODE": embed_code
    })
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

pprint(data)
"""

<iframe width="1004" height="565" src="https://www.youtube.com/embed/kqtD5dpn9C8" title="Python for Beginners - Learn Python in 1 Hour" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="1004" height="565" src="https://www.youtube.com/embed/_uQrJ0TkZlc" title="Python Tutorial - Python Full Course for Beginners" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

"""