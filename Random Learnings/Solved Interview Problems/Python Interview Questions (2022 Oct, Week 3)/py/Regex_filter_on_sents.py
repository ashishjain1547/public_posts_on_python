import re 

sents = [
    "${INS1}, Watch our latest webinar about flu vaccine",
    "Do you think patients would like to go up to 250 days without an attack?",
    "Watch our latest webinar about flu vaccine",
    "??? See if more of your patients are ready for vaccine",
    "Important news for your invaccinated patients",
    "Important news for your inv?ccinated patients"
]

good_sents = []
bad_sents = []

for i in sents:
    x = re.findall("[?}{$]", i)
    if(len(x) == 0):
        good_sents.append(i)

    else:
        bad_sents.append(i)

print(good_sents)
print(bad_sents)