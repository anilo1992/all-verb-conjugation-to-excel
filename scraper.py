from bs4 import BeautifulSoup
import xlsxwriter
import time
import requests
import random

wb = xlsxwriter.Workbook('Python/Verben/verben.xlsx')
wb_customFont = wb.add_format()
wb_customFont.set_font_name('Roboto')

f_verben = open('Python/Verben/alle-verben.txt', 'r', encoding='utf-8')
verben = f_verben.readlines()

urls = [f"https://{url}/{verb}[:-1]" for verb in verben] # Beispiel-URL
random.shuffle(urls)

print(urls)

for url_count, url in enumerate(urls): # für jedes Verb läuft ein Zähler, damit jede Konjugation eines Verb in einer neuen Zeile geschrieben wird
    print(f'Verb {url_count+1}/{len(htmls)}')
    r = requests.get(url, cookie{id: value})
    soup = BeautifulSoup(r.text, 'html.parser')
    for title_count, title in enumerate(soup.find_all(element, html_class)):
        try: # try-Block notwendig, weil add_worksheet() nur einmal die Tabellenblätter erstellen soll
            wb.add_worksheet(soup.find_all(element, html_class)[title_count].get(attribute)) # erstellt für jede Zeitform ein eigenes Tabellenblatt
            verbsListing = [li.text.lower() for li in soup.find_all('ul', 'wrap-verbs-listing')[title_count]]
            for conjugation_count, verb in enumerate(verbsListing):
                wb.get_worksheet_by_name(soup.find_all(element, html_class)[title_count].get(attribute)).write(url_count, conjugation_count+1, verb, wb_customFont)
                wb.get_worksheet_by_name(soup.find_all(element, html_class)[title_count].get(attribute)).autofit()
        except:
            verbsListing = [li.text.lower() for li in soup.find_all('ul', 'wrap-verbs-listing')[title_count]]
            for conjugation_count, verb in enumerate(verbsListing):
                wb.get_worksheet_by_name(soup.find_all(element, html_class)[title_count].get(attribute)).write(url_count, conjugation_count+1, verb, wb_customFont)
                wb.get_worksheet_by_name(soup.find_all(element, html_class)[title_count].get(attribute)).autofit()
wb.close()

print('Die Excel-Datei wurde erstellt!')    
