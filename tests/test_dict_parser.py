from unittest import TestCase

from doculabs.samon.environment import Environment
from doculabs.samon.parser.json import DictParser


class DictParserTest(TestCase):
    def test_first(self):
        tmpl = {'tagName': 'body', 'attrs': {}, 'children': ['\n        ', {'tagName': 'DS-CHAPTER', 'attrs': {'style': 'width: 170mm; display: block;', 'b:valami': 'document.ugyfelnev'}, 'children': ['\n            ', {'tagName': 'DS-HEADERS', 'attrs': {}, 'children': ['\n                ', {'tagName': 'DS-HEADER', 'attrs': {'page-sequence': 'all'}, 'children': ['\n                    ', {'tagName': 'IMG', 'attrs': {'src': 'assets/img/cib_logo.png', 'style': 'width: 48mm; margin-top: 10mm;'}, 'children': []}, '\n                ']}, '\n            ']}, '\n            ', {'tagName': 'DS-BODY', 'attrs': {'style': 'border: 1px solid black;'}, 'children': ['\n                ', {'tagName': 'DS-TEXTBOX', 'attrs': {'style': 'width: 100%; margin: 1mm 0;'}, 'children': ['\n                    ', {'tagName': 'H3', 'attrs': {}, 'children': ['Tisztelt ', {'tagName': 'DS-VAR', 'attrs': {'b:text': 'document.ugyfelnev'}, 'children': ['[Ügyfélnév]']}, '! ']}, '\n                    ', {'tagName': 'P', 'attrs': {'style': 'margin-top: 1cm;'}, 'children': ['\n                        Ezúton értesítjük, hogy a ', {'tagName': 'DS-VAR', 'attrs': {'b:text': 'document.szerzodesszam'}, 'children': ['[Szerződésszám]']}, ' számon nyilvántartott szerződése\n                        ', {'tagName': 'B', 'attrs': {}, 'children': [{'tagName': 'DS-VAR', 'attrs': {'b:text': 'document.szerzodes_lejarat_datum'}, 'children': ['[Szerződés lejárat dátum]']}, ' napon lejár.']}, '\n                        ', {'tagName': 'BR', 'attrs': {}, 'children': []}, 'Kérjük keresse fel bankfiókunkat.\n                    ']}, '\n                ']}, '\n            ']}, '\n            ', {'tagName': 'DS-FOOTERS', 'attrs': {}, 'children': ['\n                ', {'tagName': 'DS-FOOTER', 'attrs': {'page-sequence': 'all'}, 'children': ['\n                    ', {'tagName': 'DIV', 'attrs': {'class': 'page_n_of_m'}, 'children': []}, '\n                    ', {'tagName': 'DIV', 'attrs': {'style': 'border-top: 0.8pt solid black; width: 100%; padding-top: 2pt;'}, 'children': ['\n                        ', {'tagName': 'B', 'attrs': {}, 'children': ['\n                            CIB Bank Zrt. CIB Bank Ltd.\n                        ']}, '\n                        H-1027 Budapest, Medve utca 4–14. H-1995 Budapest Telefon: (06 1) 423 1000 Fax: (06 1) 489\n                        6500 Nyilvántartó cégbíróság: Fővárosi Törvényszék Cégbírósága Cégjegyzékszám: Cg. 01-10-041004 Adószám: 10136915-4-44\n                        CSASZ: 17781028-5-44 Csoport közösségi adószám: HU17781028 Tőzsdetagság: Budapesti Értéktőzsde Zrt. Tevékenységi\n                        engedély száma: 957/1997/F, III/41. 044-10/2002. BIC (SWIFT) kód: CIBHHUHB\n                    ']}, '\n                    ', {'tagName': 'IMG', 'attrs': {'src': 'assets/img/intesa_logo.png', 'style': 'width: 48mm; float: right; margin-top: -3mm;'}, 'children': []}, '\n                ']}, '\n            ']}, '\n        ']}, '\n    ']}
        parser = DictParser(environment=Environment(loader=None))
        template = parser.parse(tmpl, template_name='test')
        # print(template.root_element.children)

        #import sys
        #template.as_xml(io=sys.stdout, newline='\n', start_indent=2)