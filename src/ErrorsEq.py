ListSepDate = ['\\','/', '-', '_', '+']
DictMat = {
           "maths" : ["math", "mathématique", "mathématiques"],
           "histoire": ["hist", "histoire géo","histoire-géo", "hist-géo", "histoire geo","histoire-geo", "hist-geo"],
           "spc": ["physique", "physiques", "physique chimie", "physique-chimie", "chimie"],
           "geo": ["géographie", "geographie", "géo"],
           "philo":["philosophie", "philosophi"],
           "isn":["informatique et sciences du numérique", "informatique et science du numériques"],
           "spemaths":["spemath", "spe maths", "spe maths", "spé mathématique","spémath", "spé maths", "spé maths","spémaths"],
           "spespc":["spephysique", "spéphysique", "spé physique", "spé physiques","spe physique", "spe physiques"],
           "anglaisg": ["anglais gauthier", "anglais mme gauthier", "anglais g"],
           "anglaisn": ["anglais navizet", "anglais mr navizet", "anglais n"],
           "espagnol": ["esp", "espagnole"],
           "si": ["sciences de l ingénieur", "science de l ingénieur"]
}

def put_in_normes(text):
    carac_to_split =[]
    l_fin = []
    for i in text:
        if i in ListSepDate and not i in carac_to_split:
                carac_to_split.append(i)

    if len(carac_to_split) >1:
        l = text.split(carac_to_split[0])
        j = carac_to_split[1]
        del carac_to_split[0]
        print(l)
        l_2 =l[1].split(j)

        del[l[1]]
        l.extend(l_2)
        l_fin = l

    else:
        l_fin = text.split(carac_to_split[0])
    print(l_fin)
    final_string = "-".join(l_fin)
    return final_string

def find_mat(mat):
    final_mat = mat
    for i in DictMat.keys():
        if mat in DictMat[i]:
            print("ok")
            final_mat = i
    return final_mat

def tri(str, tris):
    dep_f = ""
    for i in str:
        if i in tris:
            pass
        else:
            dep_f +=i
    return dep_f
