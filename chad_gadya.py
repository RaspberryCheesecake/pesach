# Another famous quadratic-growth song from the Haggadah

animals = ["le gadya", "le shunra", "le khalba", "le chutra", "le nura",\
           "le maya", "le tora", "le shochet", "le malakh ha mavet",\
           "ha Kadosh Baruch Hu"]

actions = ["de akhlah", "de nashakh", "de hikkah", "de saraf", "de shatah", \
           "de kavah", "de shatah", "de shachat", "de shachat", "ve shachat"]

def chad_gadya(n):
    if n > 9:
        n = 9 # can't go higher than ha-Kadosh Baruch Hu
        
    refrain = "Chad Gadya"
    my_father = "Dizabin Abba"
    price = " bitrei zuzei"

    if n <= 0:
        print animals[0]
        print my_father + price
        print refrain + ", " + refrain
        
    else:
        print animals[n]
        print actions[n-1]
        chad_gadya(n-1)


def sing_chad_gadya():
    for i in range (0, 9):
        print "Ve ata ..."
        chad_gadya(i)
        print "\n"


if __name__ == "__main__":
    sing_chad_gadya()
