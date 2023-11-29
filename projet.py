# 1 -Import et definitions des variables globales

from collections import namedtuple
import csv
import decimal





# 2 -Definition des fonctions secondaires

def read_data_to_dicts(filename):
    data = []
    with open (filename, mode="r", encoding="utf8") as f:
        for row in f:
            data.extend(f)
        f.closed
        return data

# 3 -Definition du main() qui appellent les fonctions secondaires
def main():
    #récupération du fichier
    #with open('Annual_Surface_Temperature_Change.csv','r','utf8') as f :
    #    data=f.read()            
    #f.closed

    print(read_data_to_dicts('Annual_Surface_Temperature_Change.csv'))
    
    pass

# 4 -Appel protégé du main()
if __name__ == '__main__':
    main()
