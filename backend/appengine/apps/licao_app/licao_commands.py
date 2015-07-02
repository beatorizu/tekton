# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
#from licao_app.licao_model import Licao
from tema.tema_model import Licao


class LicaoSaveForm(ModelForm):
    """
    Form used to save and update Licao
    """
    _model_class = Licao
    _include = [Licao.titulo, 
                Licao.descricao, 
                Licao.tema]


class LicaoForm(ModelForm):
    """
    Form used to expose Licao's properties for list or json
    """
    _model_class = Licao


class GetLicaoCommand(NodeSearch):
    _model_class = Licao


class DeleteLicaoCommand(DeleteNode):
    _model_class = Licao


class SaveLicaoCommand(SaveCommand):
    _model_form_class = LicaoSaveForm


class UpdateLicaoCommand(UpdateNode):
    _model_form_class = LicaoSaveForm


class ListLicaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLicaoCommand, self).__init__(Licao.query_by_creation())

