from fpdf import FPDF
import random



# -------------------------------------------------------------------------------- # 
def Data(Name):
    # FONTS
    font = 'Times'
    fontSize = 8

    # Table
    table_border = 1
    table_spacing = 2

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
    pdf.write(10, txt='berechne Absatzsynchron')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border, Data)
    pdf.write(10, txt='\n')

    pdf.write(10, txt='berechne mit dem Ziellagerbestand')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border, Data)
    pdf.write(10, txt='\n')

    pdf.write(10, txt='berechte mit der Zielreichweite')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border, Data)
    pdf.write(10, txt='\n')



    pdf.add_page()
    pdf.write(10, txt='Lösung: Absatzsynchron')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border,PrüfDatenAbsatzsynchron(Data))
    pdf.write(10, txt='\n')

    pdf.write(10, txt='Lösung: Ziellagerbestand')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border,PrüfDatenZiellagerbestand(Data))
    pdf.write(10, txt='\n')

    pdf.write(10, txt='Lösung: Zielreichweite')
    pdf.write(10, txt='\n')
    pdf = DruckTablle(table_spacing, pdf,table_border,PrüfDatenZielreichweite(Data))
    pdf.write(10, txt='\n')

    # -------------------------------------------------- #
    # output of PDF
    outputName = Name + '' + '.pdf'
    pdf.output(outputName)

    return data

def DruckTablle(table_spacing, pdf, table_border, data):
    col_width = pdf.w / 9
    row_height = pdf.font_size
    for row in data:
        for cell in row:
            pdf.cell(col_width, row_height*table_spacing, txt=str(cell), border=table_border)
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
    # Lagerbestand "        "
    data.append(['Lagerbestand'])
    for i in range(Zeilen):
        data[5].append("            ")


    return data

# Absatz = 1
# Produktion = 2
# Ziellagerbestand = 3
# Zielreichweite = 4
# Lagerbestand = 5

def PrüfDatenAbsatzsynchron(data):
    data[2] = ['Produktion']
    # Zeile 2
    # Absatzsynchron Produktion = Absatz
    for i in range(1,7):
        data[2].append(data[1][i])

    return data

def PrüfDatenZielreichweite(data):
    data[2] = ['Produktion']

    data[5] = ['Lagerbestand']
    # Zeile 2
    # Absatzsynchron Produktion = Absatz * Zielreichweite/Arbeitstage + Absatz - Lagerbestand
    for i in range(1,7):
        Absatz = int(data[1][i])
        Zielreichweite = int(data[4][i])
        Arbeitstage = 20
        if (i == 1):
            Lagerbestand = 0
        else:
            Lagerbestand = float(data[5][i-1])
            Lagerbestand = int(Lagerbestand)

        temp = (Absatz * Zielreichweite / Arbeitstage + Absatz - Lagerbestand) / 1
        temp = int(temp)
        data[2].append(str(temp))

        temp2 = (temp - Absatz) / 1
        data[5].append(str(temp2))

    return data

def PrüfDatenZiellagerbestand(data):
    data[2] = ['Produktion']

    data[5] = ['Lagerbestand']
    # Zeile 2
    # Ziellagerbestand Produktion = Absatz-Lagerbestand + Ziellagerbestand
    for i in range(1,7):
        Absatz = int(data[1][i])
        if (i == 1):
            Lagerbestand = 0
        else:
            Lagerbestand = float(data[5][i - 1])
            Lagerbestand = int(Lagerbestand)

        Ziellagerbestand = int(data[3][i])

        temp = (Absatz - Lagerbestand + Ziellagerbestand) / 1
        data[2].append(str(temp))

        temp2 = Ziellagerbestand
        data[5].append(str(temp2))

    return data
    








if __name__ == "__main__":
    Name = 'Test'
    Data(Name)    
    


