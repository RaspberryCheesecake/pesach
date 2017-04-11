heb_nums = ["echad", "shni'im", "shlosha", "arba", "chamisha", "shisha",\
            "shmonah", "tish'ah", "asara", "acad asar", "shneim asar",\
            "shlosha asar"]

heb_words = ["eloheinu shebashamaim uva'aretz", "luchot ha brit",\
             "avot", "imahot", "chumshei torah", "sidrei mishnah",\
             "yemei shabatah", "yemei milah", "dibraya", "kochvaya",\
             "shivtaya", "midaya"]

def echad_mi_yodea(numbers, words):
    counter = 0
    for n in numbers:
        print "%s mi yodea?" % n
        print "%s ani yodea" % n
           
        inner_counter = counter
        while inner_counter >= 0:
            chorus = words[inner_counter]
            num = heb_nums[inner_counter]
            #  Special cases
            if "eloheinu" in chorus:
                chorus = " eloheinu " * 4 + chorus + "\n"
            if num == "shni'im":
                num = "shnei"
            print num + " " + chorus
            inner_counter -= 1
            
        counter += 1


echad_mi_yodea(heb_nums, heb_words)
