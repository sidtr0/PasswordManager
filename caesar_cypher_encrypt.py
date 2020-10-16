import random
def CaeserEncrypt(enter):
    key = random.randrange(1, 93)
    result = ""
    enter = list(enter)
    for i in enter:
        if i == 'a':
            alphabet = 1

        if i == 'b':
            alphabet = 2

        if i == 'c':
            alphabet = 3

        if i == 'd':
            alphabet = 4

        if i == 'e':
            alphabet = 5

        if i == 'f':
            alphabet = 6

        if i == 'g':
            alphabet = 7

        if i == 'h':
            alphabet = 8

        if i == 'i':
            alphabet = 9

        if i == 'j':
            alphabet = 10

        if i == 'k':
            alphabet = 11

        if i == 'l':
            alphabet = 12

        if i == 'm':
            alphabet = 13

        if i == 'n':
            alphabet = 14

        if i == 'o':
            alphabet = 15

        if i == 'p':
            alphabet = 16

        if i == 'q':
            alphabet = 17

        if i == 'r':
            alphabet = 18

        if i == 's':
            alphabet = 19

        if i == 't':
            alphabet = 20

        if i == 'u':
            alphabet = 21

        if i == 'v':
            alphabet = 22

        if i == 'w':
            alphabet = 23

        if i == 'x':
            alphabet = 24

        if i == 'y':
            alphabet = 25

        if i == 'z':
            alphabet = 26

        if i == 'A':
            alphabet = 27

        if i == 'B':
            alphabet = 28

        if i == 'C':
            alphabet = 29

        if i == 'D':
            alphabet = 30

        if i == 'E':
            alphabet = 31

        if i == 'F':
            alphabet = 32

        if i == 'G':
            alphabet = 33

        if i == 'H':
            alphabet = 34

        if i == 'I':
            alphabet = 35

        if i == 'J':
            alphabet = 36

        if i == 'K':
            alphabet = 37

        if i == 'L':
            alphabet = 38

        if i == 'M':
            alphabet = 39

        if i == 'N':
            alphabet = 40

        if i == 'O':
            alphabet = 41

        if i == 'P':
            alphabet = 42

        if i == 'Q':
            alphabet = 43

        if i == 'R':
            alphabet = 44

        if i == 'S':
            alphabet = 45

        if i == 'T':
            alphabet = 46

        if i == 'U':
            alphabet = 47

        if i == 'V':
            alphabet = 48

        if i == 'W':
            alphabet = 49

        if i == 'X':
            alphabet = 50

        if i == 'Y':
            alphabet = 51

        if i == 'Z':
            alphabet = 52

        if i == '1':
            alphabet = 53
        
        if i == '2':
            alphabet = 54
        
        if i == '3':
            alphabet = 55

        if i == '4':
            alphabet = 56

        if i == '5':
            alphabet = 57
        
        if i == '6':
            alphabet = 58

        if i == '7':
            alphabet = 59

        if i == '8':
            alphabet = 60

        if i == '9':
            alphabet = 61
        
        if i == '0':
            alphabet = 62

        if i == '`':
            alphabet = 63

        if i == '~':
            alphabet = 64

        if i == '!':
            alphabet = 65

        if i == '@':
            alphabet = 66

        if i == '#':
            alphabet = 67

        if i == '$':
            alphabet = 68

        if i == '%':
            alphabet = 69

        if i == '^':
            alphabet = 70

        if i == '&':
            alphabet = 71

        if i == '*':
            alphabet = 72

        if i == '(':
            alphabet = 73

        if i == ')':
            alphabet = 74

        if i == '-':
            alphabet = 75

        if i == '_':
            alphabet = 76

        if i == '{':
            alphabet = 77

        if i == '[':
            alphabet = 78

        if i == '}':
            alphabet = 79

        if i == ']':
            alphabet = 80

        if i == '=':
            alphabet = 81

        if i == '+':
            alphabet = 82

        if i == '\\':
            alphabet = 83

        if i == '|':
            alphabet = 84

        if i == ':':
            alphabet = 85

        if i == ';':
            alphabet = 86

        if i == '\'':
            alphabet = 87

        if i == '\"':
            alphabet = 88

        if i == ',':
            alphabet = 89

        if i == '<':
            alphabet = 90

        if i == '.':
            alphabet = 91

        if i == '>':
            alphabet = 92

        if i == '/':
            alphabet = 93

        if i == '?':
            alphabet = 94

        if i == ' ':
            result += ' '

        alphabet = int(alphabet) + int(key)
            
        if alphabet > 94:
            alphabet = alphabet - 94

        if alphabet == 1:
            result += 'a'


        if alphabet == 2:
            result += 'b'

        if alphabet == 3:
            result += 'c'

        if alphabet == 4:
            result += 'd'

        if alphabet == 5:
            result += 'e'

        if alphabet == 6:
            result += 'f'

        if alphabet == 7:
            result += 'g'

        if alphabet == 8:
            result += 'h'

        if alphabet == 9:
            result += 'i'

        if alphabet == 10:
            result += 'j'

        if alphabet == 11:
            result += 'k'

        if alphabet == 12:
            result += 'l'

        if alphabet == 13:
            result += 'm'

        if alphabet == 14:
            result += 'n'

        if alphabet == 15:
            result += 'o'

        if alphabet == 16:
            result += 'p'

        if alphabet == 17:
            result += 'q'

        if alphabet == 18:
            result += 'r'

        if alphabet == 19:
            result += 's'

        if alphabet == 20:
            result += 't'

        if alphabet == 21:
            result += 'u'

        if alphabet == 22:
            result += 'v'

        if alphabet == 23:
            result += 'w'

        if alphabet == 24:
            result += 'x'

        if alphabet == 25:
            result += 'y'

        if alphabet == 26:
            result += 'z'

        if alphabet == 27:
            result += 'A'

        if alphabet == 28:
            result += 'B'

        if alphabet == 29:
            result += 'C'

        if alphabet == 30:
            result += 'D'

        if alphabet == 31:
            result += 'E'

        if alphabet == 32:
            result += 'F'

        if alphabet == 33:
            result += 'G'

        if alphabet == 34:
            result += 'H'

        if alphabet == 35:
            result += 'I'

        if alphabet == 36:
            result += 'J'

        if alphabet == 37:
            result += 'K'

        if alphabet == 38:
            result += 'L'

        if alphabet == 39:
            result += 'M'

        if alphabet == 40:
            result += 'N'

        if alphabet == 41:
            result += 'O'

        if alphabet == 42:
            result += 'P'

        if alphabet == 43:
            result += 'Q'

        if alphabet == 44:
            result += 'R'

        if alphabet == 45:
            result += 'S'

        if alphabet == 46:
            result += 'T'

        if alphabet == 47:
            result += 'U'

        if alphabet == 48:
            result += 'V'

        if alphabet == 49:
            result += 'W'

        if alphabet == 50:
            result += 'X'

        if alphabet == 51:
            result += 'Y'

        if alphabet == 52:
            result += 'Z'

        if alphabet == 53:
            result += '1'

        if alphabet == 54:
            result += '2'
        
        if alphabet == 55:
            result+= '3'

        if alphabet == 56:
            result += '4'

        if alphabet == 57:
            result += '5'

        if alphabet == 58:
            result += '6'

        if alphabet == 59:
            result += '7'

        if alphabet == 60:
            result += '8'

        if alphabet == 61:
            result += '9'

        if alphabet == 62:
            result += '0'

        if alphabet == 63:
            result += '`'

        if alphabet == 64:
            result += '~'

        if alphabet == 65:
            result += '!'

        if alphabet == 66:
            result += '@'

        if alphabet == 67:
            result += '#'

        if alphabet == 68:
            result += '$'

        if alphabet == 69:
            result += '%'

        if alphabet == 70:
            result += '^'

        if alphabet == 71:
            result += '&'

        if alphabet == 72:
            result += '*'

        if alphabet == 73:
            result += '('

        if alphabet == 74:
            result += ')'

        if alphabet == 75:
            result += '-'

        if alphabet == 76:
            result += '_'

        if alphabet == 77:
            result += '{'

        if alphabet == 78:
            result += '['

        if alphabet == 79:
            result += '}'

        if alphabet == 80:
            result += ']'

        if alphabet == 81:
            result += '='

        if alphabet == 82:
            result += '+'

        if alphabet == 83:
            result += '\\'

        if alphabet == 84:
            result += '|'

        if alphabet == 85:
            result += ':'

        if alphabet == 86:
            result += ';'

        if alphabet == 87:
            result += '\''

        if alphabet == 88:
            result += '\"'

        if alphabet == 89:
            result += ','

        if alphabet == 90:
            result += '<'

        if alphabet == 91:
            result += '.'

        if alphabet == 92:
            result += '>'

        if alphabet == 93:
            result += '/'

        if alphabet == 94:
            result += '?'

    result += str(key)
    return result


        
def main():
    enter = input("Enter the sentence to be encrypted: ")
    answer = CaeserEncrypt(enter)

main()