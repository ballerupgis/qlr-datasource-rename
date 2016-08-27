# qlr-datasource-rename
Løber igennem mapper med QLR-filer og ændre host i datasource. Kan f.eks. bruges hvis data i postgres migreres til en ny server, hvorved forbindelsesoplysningerne skal ændres i QLR-filerne.

Kør kommandoen:
'''
$ python3 qlr_replace.py <ROOTDIR> <NEWHOST>
'''
Der laves ikke backup, så tag evt. kopi af data i tilfælde af fejl.


kilde http://stackoverflow.com/a/20593644 og http://stackoverflow.com/a/19587581
