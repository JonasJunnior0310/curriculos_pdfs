from fpdf import FPDF
from fpdf import HTMLMixin
import pandas as pd

doc = pd.read_csv("./curriculos_2.csv")
doc = doc.where((pd.notnull(doc)), None)
d = 50
for index, row in doc.iterrows():
    class PDF(FPDF, HTMLMixin):
            def header(self):
                self.rect(self.x-5, self.y-5, 200, 290)
                # Arial bold 15
                self.set_font('Times', 'B', 22)
                # Title
                if self.page_no() == 1:
                    self.cell(0, 10, row['NOME'], align='C')
                # Line break
                self.ln(10)

            def footer(self):
                self.set_y(-2.5)


    info = "{}{}{}{}{}{}".format(
        str(row['NACIONALIDADE']) + ", " if row['NACIONALIDADE'] != None  
        else "",
        " " + str(row['IDADE']) + ", " if row['IDADE'] != None  
        else "",
        " " + str(row['ESTADO CIVIL']) + "\n" if row['ESTADO CIVIL'] != None
        else "",
        str(row['ENDEREÇO']) + "\n" if row['ENDEREÇO'] != None
        else "",
        "Telefone(s): " + str(row['TELEFONE']) + "\n" if row['TELEFONE'] != None
        else "",
        "Email: " + str(row['E-MAIL']) + "\n" if row['E-MAIL'] != None
        else "",
    )

    hist_escola = "{}{}{}".format(
        "<b>Grau de formação: </b>" + str(row["GRAU"]) + "<br>" if row["GRAU"] != None
        else "",
        "<b>Instituição de ensino: </b>" + str(row["INSTITUIÇÃO DE ENSINO"]) + "<br>" if row["INSTITUIÇÃO DE ENSINO"] != None
        else "",
        "<b>Status ou ano de conclusão: </b>" + str(row["STATUS OU ANO DE CONCLUSÃO"]) + "<br>" if row["STATUS OU ANO DE CONCLUSÃO"] != None
        else ""
    )

    resumo = "{}".format(
        "- " +str(row["RESUMO PROFISSIONAL"]) + "\n" if row["RESUMO PROFISSIONAL"] != None
        else "",
    )

    Exp = "{}{}{}{}{}{}".format(
        "<b>Empresa: </b>" + str(row["EMPRESA"]) + "<br>" if row["EMPRESA"] != None
        else "",
        "<b>Cargo ocupado: </b>" + str(row["CARGO OCUPADO"]) + "<br>" if row["CARGO OCUPADO"] != None
        else "",
        "<b>Principais Atividades: </b>" + str(row["PRINCIPAIS ATIVIDADES"]) + "<br>" if row["PRINCIPAIS ATIVIDADES"] != None
        else "",
        "<b>Conquistas: </b>" + str(row["PRINCIPAIS RESULTADOS E CONQUISTAS"]) + "<br>" if row["PRINCIPAIS RESULTADOS E CONQUISTAS"] != None
        else "",
        "<b>Mês/ano de início: </b>" + str(row["MÊS/ANO DE INÍCIO"]) + "<br>" if row["MÊS/ANO DE INÍCIO"] != None
        else "",
        "<b>Mês/ano de fim: </b>" + str(row["MÊS/ANO DE FIM"]) + "<br>" if row["MÊS/ANO DE FIM"] != None
        else ""
    )

    cur = "{}{}{}{}{}{}{}{}".format(
        "Cursos complementares\n\n",
        str(row["NOME DO CURSO"]) + "\n" if row["NOME DO CURSO"] != None
        else "", 
        "Instituição: " + str(row["NOME DA INSTITUIÇÃO"]) + "\n" if row["NOME DA INSTITUIÇÃO"] != None
        else "",
        "Carga horária: " + str(row["CARGA HORÁRIA 1"]) + "\n" if row["CARGA HORÁRIA 1"] != None
        else "",
        "Entidade: " + str(row["NOME DA ENTIDADE"]) + "\n" if row["NOME DA ENTIDADE"] != None
        else "",
        "Mês/ano de início: " + str(row["MÊS/ANO DE INÍCIO 2"]) + "\n" if row["MÊS/ANO DE INÍCIO 2"] != None
        else "",
        "Mês/ano de fim: " + str(row["MÊS/ANO DE FIM 2"]) + "\n" if row["MÊS/ANO DE FIM 2"] != None
        else "",
        "Atividades realizadas: " + str(row["ATIVIDADES"]) + "\n\n" if row["ATIVIDADES"] != None
        else "",
    )

    vol = "{}{}{}{}{}{}{}{}".format(
        "Trabalhos Voluntários\n\n",
        str(row["NOME DO CURSO"]) + "\n" if row["NOME DO CURSO"] != None
        else "", 
        "Instituição: " + str(row["NOME DA INSTITUIÇÃO"]) + "\n" if row["NOME DA INSTITUIÇÃO"] != None
        else "",
        "Carga horária: " + str(row["CARGA HORÁRIA 1"]) + "\n" if row["CARGA HORÁRIA 1"] != None
        else "",
        "Entidade: " + str(row["NOME DA ENTIDADE"]) + "\n" if row["NOME DA ENTIDADE"] != None
        else "",
        "Mês/ano de início: " + str(row["MÊS/ANO DE INÍCIO 2"]) + "\n" if row["MÊS/ANO DE INÍCIO 2"] != None
        else "",
        "Mês/ano de fim: " + str(row["MÊS/ANO DE FIM 2"]) + "\n" if row["MÊS/ANO DE FIM 2"] != None
        else "",
        "Atividades realizadas: " + str(row["ATIVIDADES"]) + "\n\n" if row["ATIVIDADES"] != None
        else "",
    )

    at = "{}{}{}{}{}".format(
        "Eventos\n\n",
        str(row["NOME/TÍTULO DO EVENTO"]) + "\n" if row["NOME/TÍTULO DO EVENTO"] != None
        else "",
        "Período: " + str(row["PERÍODO"]) + "\n" if row["PERÍODO"] != None
        else "",
        "Entidade Realizado: " + str(row["ENTIDADE  REALIZADORA"]) + "\n" if row["ENTIDADE  REALIZADORA"] != None
        else "",
        "Carga Horária: " + str(row["CARGA HORÁRIA 2"]) + "\n" if row["CARGA HORÁRIA 2"] != None
        else "",
    )

    objetivo = "{}".format(
        "- " + str(row["OBJETIVO"]) + "\n" if row["OBJETIVO"] != None
        else ""
    )

    # Buscando a class que é filha
    pdf = PDF(orientation ='P', format = 'A4' )
    pdf.alias_nb_pages()
    pdf.add_page('P')
    pdf.set_auto_page_break(auto=True, margin = 0.0)
    offset = pdf.x + 140
    # Setting Images
    pdf.set_font('Times',"", 10)    
    pdf.multi_cell(0, 6, info , align='C')

    pdf.set_font('Times', 'BU', 14)

    if row["OBJETIVO"] != None:
        pdf.ln(5)
        pdf.cell(0, 10, "Objetivo", align='L' )
        pdf.ln(10)
        pdf.set_font('Times', "" ,12)
        pdf.multi_cell(0, 6, objetivo, border=1)

    pdf.set_font('Times', 'BU', 14)
    
    if row["RESUMO PROFISSIONAL"] != None:
        pdf.ln(5)
        pdf.cell(0, 10, "Resumo profissional", align='L' )
        pdf.ln(10)
        pdf.set_font('Times', "" ,12)
        pdf.multi_cell(0, 6, resumo, border=1)

    pdf.ln(5)

    pdf.set_font('Times', 'BU', 14)
    pdf.cell(140, 10, "Formação Escola/Acadêmica", align='L' )
    pdf.ln(10)
    pdf.set_font('Times', "" ,12)
    top = pdf.y
    hor = pdf.x
    pdf.write_html(hist_escola)
    top_2 = pdf.y
    hor_2 = pdf.x
    pdf.rect(hor, top, 190, top_2 - top)
    
    pdf.set_font('Times', 'BU', 14)

    if row["EMPRESA"] != None:
        pdf.ln(5)
        pdf.cell(0, 10, "Experiência Profissional", align='L' )
        pdf.ln(10)
        pdf.set_font('Times', "" ,12)
        top = pdf.y
        hor = pdf.x
        pdf.write_html(Exp)
        top_2 = pdf.y
        hor_2 = pdf.x
        pdf.rect(hor, top, 190, top_2 - top)

    pdf.set_font('Times', 'BU', 14)

    if row["NOME DO CURSO"] != None or row["NOME/TÍTULO DO EVENTO"] != None:
        pdf.ln(5)
        pdf.cell(140, 10, "Informações complementares", align='L' )
        pdf.ln(10)
        pdf.set_font('Times', "" ,12)
        if row["NOME DO CURSO"] != None:
            if row["ATIVIDADES"] != "Voluntário":
                pdf.multi_cell(0, 6, cur, border=1)
                pdf.ln(3)
            else:
                pdf.multi_cell(0, 6, vol, border=1)
                pdf.ln(3)
        if row["NOME/TÍTULO DO EVENTO"] != None:
            pdf.multi_cell(0, 6, at, border=1)

    pdf.output('./curriculos_feitos/curriculo_' + str(d) + '.pdf').encode('latin-1')
    d = d + 1

