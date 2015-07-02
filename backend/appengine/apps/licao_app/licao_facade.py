# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from licao_app.licao_commands import ListLicaoCommand, SaveLicaoCommand, UpdateLicaoCommand, LicaoForm,\
    GetLicaoCommand, DeleteLicaoCommand


def save_licao_cmd(**licao_properties):
    """
    Command to save Licao entity
    :param licao_properties: a dict of properties to save on model
    :return: a Command that save Licao, validating and localizing properties received as strings
    """
    return SaveLicaoCommand(**licao_properties)


def update_licao_cmd(licao_id, **licao_properties):
    """
    Command to update Licao entity with id equals 'licao_id'
    :param licao_properties: a dict of properties to update model
    :return: a Command that update Licao, validating and localizing properties received as strings
    """
    return UpdateLicaoCommand(licao_id, **licao_properties)


def list_licaos_cmd():
    """
    Command to list Licao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLicaoCommand()


def licao_form(**kwargs):
    """
    Function to get Licao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LicaoForm(**kwargs)


def get_licao_cmd(licao_id):
    """
    Find licao by her id
    :param licao_id: the licao id
    :return: Command
    """
    return GetLicaoCommand(licao_id)



def delete_licao_cmd(licao_id):
    """
    Construct a command to delete a Licao
    :param licao_id: licao's id
    :return: Command
    """
    return DeleteLicaoCommand(licao_id)

