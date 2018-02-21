import unittest
# from . import


def ceasar_cypher(text, key):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    text = text.lower()
    letters_len = len(letters)
    if key >= letters_len:
        key = key % letters_len
    for letter in text:
        if letter == " ":
            result += letter
            continue
        index = letters.index(letter)
        ceasar_index = index + key
        if ceasar_index > letters_len:
            ceasar_index -= letters_len 
        result += letters[ceasar_index]
    return result

class TestCypher(unittest.TestCase):

    def test_simple(self):
        resultado = ceasar_cypher("hola", 2)
        self.assertEqual(resultado, "jqnc")
    
    def test_edge_case(self):
        resultado = ceasar_cypher("zorro", 2)
        self.assertEqual(resultado, "bqttq")

    def test_key_is_bigger_or_equal_than_letters(self):
        resultado = ceasar_cypher("hola", 26)
        self.assertEqual(resultado, "hola")

    def test_upper_letters(self):
        resultado = ceasar_cypher("HOLA", 2)
        self.assertEqual(resultado, "jqnc")
    
    def test_cypher_spaces(self):
        resultado = ceasar_cypher("h o l a", 2)
        self.assertEqual(resultado, "j q n c")

if __name__ == '__main__': # Guard
    unittest.main()
