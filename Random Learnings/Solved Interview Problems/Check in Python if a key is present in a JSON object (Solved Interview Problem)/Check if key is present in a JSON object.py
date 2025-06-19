jsonstreng = {
    "kjoretoydataListe":
    [
        {
            "kjoretoyId": {"kjennemerke":"EK 17058","understellsnummer":"5YJXCCE29GF009633"},
            "forstegangsregistrering": {"registrertForstegangNorgeDato":"2016-09-07"},
            "kjennemerke": [
                {"fomTidspunkt":"2016-09-07T00:00:00+02:00","kjennemerke":"EK 17058","kjennemerkekategori":"KJORETOY",
                "kjennemerketype":{"kodeBeskrivelse":"Sorte tegn p- hvit bunn","kodeNavn":"Ordin-re kjennemerker","kodeVerdi":"ORDINART","tidligereKodeVerdi":[]}},{"fomTidspunkt":"2022-08-19T17:04:04.334+02:00","kjennemerke":"GTD","kjennemerkekategori":"PERSONLIG"}
            ]
        }
    ]
}

def checkIfKeyExistsInDict(in_dict, i_key):
    if(isinstance(in_dict, dict)):
        if(i_key in in_dict):
            print(i_key + " found in: " + str(in_dict))
            print()
        
        for j_key in in_dict:
            checkIfKeyExistsInDict(in_dict[j_key], i_key)
    elif(isinstance(in_dict, list)):
        for j_key in range(len(in_dict)):
            checkIfKeyExistsInDict(in_dict[j_key], i_key)

        
checkIfKeyExistsInDict(jsonstreng, "kjennemerke")