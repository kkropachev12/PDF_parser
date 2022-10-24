import time


from convertor import convertor
from meraki import meraki


if __name__ == '__main__':

    for i in range(22):
        s = time.time()
        print(i)

        file_name = f'Meraki{i}'

        convertor(file_name)
        try:
            meraki(file_name)
        except ValueError as ex:
            convertor(file_name)
            try:
                meraki(file_name)
            except:
                """Send this file to company as unconvertable"""
                print(f"Can't convert {file_name} properly")
        print(time.time() - s)
