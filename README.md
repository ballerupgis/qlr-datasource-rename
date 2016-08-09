# qlr-datasource-rename
Løber igennem mapper med QLR-filer og ændre host i datasource. Kan f.eks. bruges hvis data i postgres migreres til en ny server, hvorved forbindelsesoplysningerne skal ændres i QLR-filerne.

OBS: ændre alle 'host=hostname', så kan måske skade filerne, hvis dette fremgår andre steder som ikke har noget med datasource at gøre (nok ikke så sandsyligt). 

kilde http://stackoverflow.com/a/20593644 og http://stackoverflow.com/a/19587581
