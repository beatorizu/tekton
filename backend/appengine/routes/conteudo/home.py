# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    class Conteudo(object):
        def __init__(self, titulo, desc):
            self.desc = desc
            self.titulo = titulo

    conteudos = [Conteudo('あ/ア ','Hiragana/Katakana'),Conteudo('数','Números'),Conteudo('色','Cores'),Conteudo('食べ物','Comida'),Conteudo('動物','Animais'),Conteudo('形容詞','Adjetivos'),Conteudo('拝啓','Saudações'),Conteudo('家族','Família'),Conteudo('職業','Profissões'),Conteudo('日付','Data'),Conteudo('時間','Hora'),Conteudo('副詞','Advérbio')]
    contexto = {'conteudos':conteudos}
    return TemplateResponse(contexto)

