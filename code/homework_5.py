secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
                 ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
                 ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
                 ['и$ #sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
                 ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
string = ''
string_of_secret_letter = ''
for code_ in secret_letter:
    for part in code_:
        string += ' '
        for letter in part:
            if letter in small_rus:
                for one_letter in letter:
                    string += one_letter
                    result = string.capitalize()
print(result)
end_ = input('Для выхода из программы нажмите "Enter"')

