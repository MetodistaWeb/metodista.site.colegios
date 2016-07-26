# -*- coding: utf-8 -*-

from metodista.site.colegios.config import PROJECTNAME

import logging

logger = logging.getLogger(PROJECTNAME)


def setup(context):
    """ Descricao base da atualizacao
    """
    logger.info('Faz nada - padrao de passo de atualizacao')
