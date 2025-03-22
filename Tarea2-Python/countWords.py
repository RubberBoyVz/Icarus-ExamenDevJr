# Escribe un script en Python que lea un archivo de texto y cuente la cantidad de palabras que contiene.

def countWords(file):
    with open(file,'r') as f:
        contenido = f.read();
        palabras = contenido.split();
        return len(palabras);


file = 'lorem.txt';
wordsAmount = countWords(file);

print(str(wordsAmount) + " palabras tiene el archivo");