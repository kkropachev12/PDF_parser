import openpyxl


from ABBYY import CloudOCR

def convertor(file_name):
    '''Converts pdf file to xlsx format (excel)'''
    ocr_engine = CloudOCR(application_id='3310c60a-f8f7-43b9-b6b4-a1fb58f35da3',
                        password='LkTD7NDTiCiHBt9hULyGO1hu')


    pdf = open(f'{file_name}.pdf', 'rb')
    file = {pdf.name: pdf}

    result = ocr_engine.process_and_download(
        file, exportFormat='xlsx', language='English')

    with open(f'{file_name}.xlsx', 'wb') as f:
        f.write(result['xlsx'].getbuffer())
