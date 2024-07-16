import logging
# creation d'un fichier de log pour loger nous erreus

logging.basicConfig(level=logging.ERROR,
                    filename="app.log",  # (le fichier où sera envoyer les logs )
                    filemode="w",  # le mode d'action sur le fichier, ici sera "w" (write)
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Lafonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")