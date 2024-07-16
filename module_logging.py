"""
Le module logging en Python est un module puissant et flexible pour gérer les logs de votre application.
Il permet de capturer des informations de diagnostic ou d'exécution, ce qui est crucial pour le débogage,
la surveillance et la maintenance des applications. Voici une vue d'ensemble du module logging,
de ses concepts clés et de la manière de l'utiliser.

"""

# Il peut afficher 5 types de messages

"""
DEBUG : Messages de débogage, souvent détaillés et utilisés pour diagnostiquer des problèmes.

INFO : Messages informatifs, confirmant que les choses fonctionnent comme prévu.

WARNING : Messages d'avertissement indiquant qu'il y a eu un problème, ou quelque chose d'inattendu, mais l'exécution continue.

ERROR : Messages d'erreur indiquant un problème plus sérieux, mais où l'exécution continue.

CRITICAL : Messages critiques indiquant une erreur grave qui pourrait empêcher le programme de continuer à s'exécuter.

"""

import logging

logging.debug("Lafonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")