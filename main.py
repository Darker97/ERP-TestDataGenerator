from fpdf import FPDF
import random



# -------------------------------------------------------------------------------- # 
def Data(Name):
    # FONTS
    font = 'Times'
    fontSize = 10

    # Table
    table_border = 4
    table_spacing = 3

    Zeilen = 6

    # -------------------------------------------------- #
    data = NormData(Zeilen)

    pdf = FPDF()
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font(font, size=fontSize)

    # -------------------------------------------------- #
    # insert the Tables
    Data = NormData(Zeilen)
    pdf = DruckTablle(pdf,table_border, Data)

    pdf.write(10, txt='Absatzsynchron')
    pdf.write(10, txt='\n\n')
    pdf = DruckTablle(pdf,table_border,PrüfDatenAbsatzsynchron(Data))

    pdf.write(10, txt='Ziellagerbestand')
    pdf.write(10, txt='\n\n')
    pdf = DruckTablle(pdf,table_border,PrüfDatenZiellagerbestand(Data))

    pdf.write(10, txt='Zielreichweite')
    pdf.write(10, txt='\n\n')
    pdf = DruckTablle(pdf,table_border,PrüfDatenZielreichweite(Data))

    # -------------------------------------------------- #
    # output of PDF
    outputName = Name + '' + '.pdf'
    pdf.output(outputName)

    return data

def DruckTablle(pdf, table_border, data):
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    table_spacing = table_spacing
    for row in data:
        for cell in row:
            pdf.cell(col_width, row_height*table_spacing, txt=cell, border=table_border)
        pdf.ln(row_height*table_spacing)
    return pdf

def NormData(Zeilen):
    data =  [
                ['Datum','09.12','10.12','11.12','10.12','11.12','12.12']
            ]
    # -------------------------------------------------------------------------------- # 
    # Absatz 100, 200
    data.append(['Absatz'])
    for i in range(Zeilen):
        data[1].append(str(random.randint(100,200)))

    # -------------------------------------------------------------------------------- # 
    # Produktion "        "
    data.append(['Produktion'])
    for i in range(Zeilen):
        data[2].append("            ")
    # -------------------------------------------------------------------------------- # 
    # Ziellagerbestand 10,30
    data.append(['Ziellagerbestand'])
    for i in range(Zeilen):
        data[3].append(str(random.randint(10,30)))
    # -------------------------------------------------------------------------------- # 
    # Zielreichweite 5,30
    data.append(['Zielreichweite'])
    for i in range(Zeilen):
        data[4].append(str(random.randint(5,30)))
    # -------------------------------------------------------------------------------- # 
    return data

# Absatz = 1
# Produktion = 2
# Ziellagerbestand = 3
# Zielreichweite = 4

def PrüfDatenAbsatzsynchron(data):
    data[2] = ['Produktion']
    # Zeile 2
    # Absatzsynchron Produktion = Absatz
    for i in range(1,6):
        data[2].append(data[1][i])

    return data

def PrüfDatenZielreichweite(data):
    data[2] = ['Produktion']
    # Zeile 2
    # Absatzsynchron Produktion = Absatz * Zielreichweite/Arbeitstage + Absatzmenge - Lagerbestand
    for i in range(1,6):
        # TODO: FORMEL
        temp = 0
        data[2].append(temp)

    return data

def PrüfDatenZiellagerbestand(data):
    data[2] = ['Produktion']
    # Zeile 2
    # Ziellagerbestand Produktion = Absatz-Lagerbestand + Ziellagerbestand
    for i in range(1,6):
        # TODO: FORMEL
        temp = 0
        data[2].append(temp)

    return data
    








if __name__ == "__main__":
    Name = 'Test'
    


