print('\033[34mHi world!!!\033[m')
print('''︎\033[1;35m[  1  ]\033[m \033[1;3mCALCULADORA\033[m
\033[1;35m[  2  ]\033[m \033[1;3mCONVERSOR BINÁRIO\033[m
\033[1;35m[  3  ]\033[m \033[1;3mCONVERSOR DE DISTÂNCIA\033[m
\033[1;35m[  4  ]\033[m \033[1;3mCONVERSOR DE ÁREA\033[m
\033[1;35m[  5  ]\033[m \033[1;3mCONVERSOR DE TEMPERATURA\033[m
\033[1;35m[  6  ]\033[m \033[1;3mCONVERSOR DE VOLUME\033[m
\033[1;35m[  7  ]\033[m \033[1;3mCONVERSOR DE MASSA\033[m
\033[1;35m[  8  ]\033[m \033[1;3mCONVERSOR DE VELOCIDADE\033[m
\033[1;35m[  9  ]\033[m \033[1;3mCONVERSOR DE TEMPO\033[m
\033[1;35m[ 10  ]\033[m \033[1;3mSEQUÊNCIA DE FIBONACCI\033[m
\033[1;35m[ 11  ]\033[m \033[1;3mCAUCULO FATORIAL\033[m
\033[1;35m[ 12  ]\033[m \033[1;3mPROGRESSÃO ARITMÉTICA\033[m''')
n42 = int(input('Selecione a opção que deseja: '))
if n42 > 12:
    print('\033[1;3;31mMETEU ESSA DOIDÃO???\033[m')

#CALCULADORA

if n42 == 1:
    n33 = float(input('Coloque o número que deseja: '))
    print('''[ 1 ] adição
[ 2 ] subtração
[ 3 ] multiplicação
[ 4 ] divisão
[ 5 ] potenciação
[ 6 ] raiz quadrada
[ 7 ] Tabuada até 10x
[ 8 ] porcentagem''')
    n34 = int(input('selecione o tipo de conta: '))
    if n34 > 8:
        print('METEU ESSA DOIDÃO???')
    if n34 == 1:
        n35 = float(input('Agora o outro número: '))
        n36 = (n33 + n35)
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n36, '\033[m'))
    if n34 == 2:
        n35 = float(input('Agora o outro número: '))
        n37 = (n33 - n35)
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n37, '\033[m'))
    if n34 == 3:
        n35 = float(input('Agora o outro número: '))
        n38 = (n33 * n35)
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n38, '\033[m'))
    if n34 == 4:
        n35 = float(input('Agora o outro número: '))
        n39 = (n33 / n35)
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n39, '\033[m'))
    if n34 == 5:
        n35 = float(input('Agora o outro número: '))
        n40 = (n33 ** n35)
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n40, '\033[m'))
    if n34 == 6:
        n41 = (n33 ** (1 / 2))
        print('O resultado é: {}{:.2f}{}'.format('\033[1;32m', n41, '\033[m'))
    if n34 == 7:
        v1 = (n33 * 1)
        v2 = (n33 * 2)
        v3 = (n33 * 3)
        v4 = (n33 * 4)
        v5 = (n33 * 5)
        v6 = (n33 * 6)
        v7 = (n33 * 7)
        v8 = (n33 * 8)
        v9 = (n33 * 9)
        v10 = (n33 * 10)
        print('{:.1f} x 1 = {:.1f}'.format(n33, v1))
        print('{:.1f} x 2 = {:.1f}'.format(n33, v2))
        print('{:.1f} x 3 = {:.1f}'.format(n33, v3))
        print('{:.1f} x 4 = {:.1f}'.format(n33, v4))
        print('{:.1f} x 5 = {:.1f}'.format(n33, v5))
        print('{:.1f} x 6 = {:.1f}'.format(n33, v6))
        print('{:.1f} x 7 = {:.1f}'.format(n33, v7))
        print('{:.1f} x 8 = {:.1f}'.format(n33, v8))
        print('{:.1f} x 9 = {:.1f}'.format(n33, v9))
        print('{:.1f} x 10 = {:.1f}'.format(n33, v10))
    if n34 == 8:
        n35 = float(input('Agora o outro número: '))
        n93 = (n33 * n35) / 100
        print('O resultado é: {}{:.2f}%{}'.format('\033[1;32m', n93, '\033[m'))

#CONVERSOR BINÁRIO

if n42 == 2:
    n43 = int(input('Coloque o número que deseja: '))
    print('''[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
    n44 = int(input('Selecione o tipo de conversão: '))
    if n44 > 3:
        print('METEU ESSA DOIDÃO???')
    if n44 == 1:
        print('O resultado é: {}{}{}'.format('\033[1;32m', bin(n43)[2:], '\033[m'))
    if n44 == 2:
        print('O resultado é: {}{}{}'.format('\033[1;32m', oct(n43)[2:], '\033[m'))
    if n44 == 3:
        print('O resultado é: {}{}{}'.format('\033[1;32m', hex(n43)[2:], '\033[m'))

#CONVERSOR DE DISTÂNCIA

if n42 == 3:
    n45 = float(input('Coloque o número que deseja converter: '))
    print('''[ 1 ] MILÍMETROS
[ 2 ] CENTÍMETROS
[ 3 ] METROS
[ 4 ] KILOMETROS
[ 5 ] MILHAS''')
    n47 = int(input('Coverter: '))
    print('''[ 1 ] MILÍMETROS
[ 2 ] CENTÍMETROS
[ 3 ] METROS
[ 4 ] KILOMETROS
[ 5 ] MILHAS''')
    n48 = int(input('Para: '))
    if n47 > 5 or n48 > 5 or n47 == n48:
        print('METEU ESSA DOIDÃO???')
    if n47 == 1 and n48 == 2:
        n49 = n45 / 10
        print('O resultado é: {}{} cm{}'.format('\033[1;32m', n49, '\033[m'))
    if n47 == 1 and n48 == 3:
        n50 = n45 / 100
        print('O resultado é: {}{} m{}'.format('\033[1;32m', n50, '\033[m'))
    if n47 == 1 and n48 == 4:
        n51 = n45 / 1000
        print('O resultado é: {}{} km{}'.format('\033[1;32m', n51, '\033[m'))
    if n47 == 1 and n48 == 5:
        n52 = n45 * 0.0000006214
        print('O resultado é: {}{} mi{}'.format('\033[1;32m', n52, '\033[m'))
    if n47 == 2 and n48 == 1:
        n53 = n45 * 10
        print('O resultado é: {}{} mm{}'.format('\033[1;32m', n53, '\033[m'))
    if n47 == 2 and n48 == 3:
        n54 = n45 / 10
        print('O resultado é: {}{} m{}'.format('\033[1;32m', n54, '\033[m'))
    if n47 == 2 and n48 == 4:
        n55 = n45 / 100
        print('O resultado é: {}{} km{}'.format('\033[1;32m', n55, '\033[m'))
    if n47 == 2 and n48 == 5:
        n56 = n45 * 0.000006214
        print('O resultado é: {}{} mi{}'.format('\033[1;32m', n56, '\033[m'))
    if n47 == 3 and n48 == 1:
        n57 = n45 * 100
        print('O resultado é: {}{} mm{}'.format('\033[1;32m', n57, '\033[m'))
    if n47 == 3 and n48 == 2:
        n58 = n45 * 10
        print('O resultado é: {}{} cm{}'.format('\033[1;32m', n58, '\033[m'))
    if n47 == 3 and n48 == 4:
        n59 = n45 / 10
        print('O resultado é: {}{} km{}'.format('\033[1;32m', n59, '\033[m'))
    if n47 == 3 and n48 == 5:
        n60 = n45 * 0.0006214
        print('O resultado é: {}{} mi{}'.format('\033[1;32m', n60, '\033[m'))
    if n47 == 4 and n48 == 1:
        n61 = n45 * 1000
        print('O resultado é: {}{} mm{}'.format('\033[1;32m', n61, '\033[m'))
    if n47 == 4 and n48 == 2:
        n62 = n45 * 100
        print('O resultado é: {}{} cm{}'.format('\033[1;32m', n62, '\033[m'))
    if n47 == 4 and n48 == 3:
        n63 = n45 * 10
        print('O resultado é: {}{} m{}'.format('\033[1;32m', n63, '\033[m'))
    if n47 == 4 and n48 == 5:
        n64 = n45 * 0.6214
        print('O resultado é: {}{} mi{}'.format('\033[1;32m', n64, '\033[m'))
    if n47 == 5 and n48 == 1:
        n65 = n45 / 0.0000006214
        print('O resultado é: {}{} mm{}'.format('\033[1;32m', n65, '\033[m'))
    if n47 == 5 and n48 == 2:
        n66 = n45 / 0.000006214
        print('O resultado é: {}{} cm{}'.format('\033[1;32m', n66, '\033[m'))
    if n47 == 5 and n48 == 3:
        n67 = n45 / 0.0006214
        print('O resultado é: {}{} m{}'.format('\033[1;32m', n67, '\033[m'))
    if n47 == 5 and n48 == 4:
        n68 = n45 / 0.6214
        print('O resultado é: {}{} km{}'.format('\033[1;32m', n68, '\033[m'))

#CONVERSOR DE ÁREA

if n42 == 4:
    n70 = float(input('Coloque o número que deseja converter: '))
    print('''[ 1 ] ACRES
[ 2 ] HECTARES
[ 3 ] CENTÍMETROS QUADRADOS
[ 4 ] METROS QUADRADOS''')
    n69 = int(input('CONVERTER: '))
    print('''[ 1 ] ACRES
[ 2 ] HECTARES
[ 3 ] CENTÍMETROS QUADRADOS
[ 4 ] METROS QUADRADOS''')
    n71 = int(input('PARA: '))
    if n69 > 4 or n70 > 4 or n69 == n71:
        print('METEU ESSA DOIDÃO???')
    if n69 == 1 and n71 == 2:
        n72 = n70 * 0.4046856422
        print('O resultado é: {}{} ha{}'.format('\033[1;32m', n72, '\033[m'))
    if n69 == 1 and n71 == 3:
        n73 = n70 * 40468564.22
        print('O resultado é: {}{} cm²{}'.format('\033[1;32m', n73,'\033[m'))
    if n69 == 1 and n71 == 4:
        n74 = n70 * 4046.856422
        print('O resultado é: {}{} m²{}'.format('\033[1;32m', n74,'\033[m'))
    if n69 == 2 and n71 == 1:
        n75 = n70 / 0.4046856422
        print('O resultado é: {}{} ac{}'.format('\033[1;32m', n75,'\033[m'))
    if n69 == 2 and n71 == 3:
        n76 = n70 * 100000000
        print('O resultado é: {}{} cm²{}'.format('\033[1;32m', n76, '\033[m'))
    if n69 == 2 and n71 == 4:
        n77 = n70 * 10000
        print('O resultado é: {}{} m²{}'.format('\033[1;32m', n77, '\033[m'))
    if n69 == 3 and n71 == 1:
        n78 = n70 / 40468564.22
        print('O resultado é: {}{} ac{}'.format('\033[1;32m', n78, '\033[m'))
    if n69 == 3 and n71 == 2:
        n79 = n70 / 100000000
        print('O resultado é: {}{} ha{}'.format('\033[1;32m', n79, '\033[m'))
    if n69 == 3 and n71 == 4:
        n80 = n70 * 0.0001
        print('O resultado é: {}{} m²{}'.format('\033[1;32m', n80, '\033[m'))
    if n69 == 4 and n71 == 1:
        n81 = n70 * 0.0002471054
        print('O resultado é: {}{} ac{}'.format('\033[1;32m', n81, '\033[m'))
    if n69 == 4 and n71 == 2:
        n82 = n70 * 0.0001
        print('O resultado é: {}{} ha{}'.format('\033[1;32m', n82, '\033[m'))
    if n69 == 4 and n71 == 3:
        n83 = n70 * 10000
        print('O resultado é: {}{} cm²{}'.format('\033[1;32m', n83, '\033[m'))

# CONVERSOR DE TEMPERATURA

if n42 == 5:
    n84 = float(input('Selecione o número que deseja converter: '))
    print('''[ 1 ] CELSIUS
[ 2 ] FAHRENHEIT
[ 3 ] KELVIN
[ 4 ] MAMACITA''')
    n85 = int(input('CONVERTER: '))
    print('''[ 1 ] CELSIUS
[ 2 ] FAHRENHEIT
[ 3 ] KELVIN
[ 4 ] MAMACITA''')
    n86 = int(input('PARA: '))
    if n85 > 4 or n86 > 4 or n85 == n86:
        print('METEU ESSA DOIDÃO???')
    if n85 == 1 and n86 == 2:
        n87 = n84 * 1.8 + 32
        print('O resultado é: {}{} ºf{}'.format('\033[1;32m', n87, '\033[m'))
    if n85 == 1 and n86 == 3:
        n88 = n84 + 273.15
        print('O resultado é: {}{} K{}'.format('\033[1;32m', n88, '\033[m'))
    if n85 == 1 and n86 == 4:
        n997 = n84 * 1.6 + 6
        print('O resultado é: {}{} ºm{}'.format('\033[1;32m', n997, '\033[m'))
    if n85 == 2 and n86 == 1:
        n89 = (n84 - 32)/1.8
        print('O resultado é: {}{} ºc{}'.format('\033[1;32m', n89, '\033[m'))
    if n85 == 2 and n86 == 3:
        n90 = (n84 - 32)/1.8 + 273.15
        print('O resultado é: {}{} K{}'.format('\033[1;32m', n90, '\033[m'))
    if n85 == 2 and n86 == 4:
        c = ((n84 - 32)/1.8)
        n998 = c * 1.6 + 6
        print('O resultado é: {}{} ºm{}'.format('\033[1;32m', n998, '\033[m'))
    if n85 == 3 and n86 == 1:
        n91 = n84 - 273.15
        print('O resultado é: {}{} ºc{}'.format('\033[1;32m', n91, '\033[m'))
    if n85 == 3 and n86 == 2:
        n92 = 1.8 * (n84 - 273.15) + 32
        print('O resultado é: {}{} ºf{}'.format('\033[1;32m', n92, '\033[m'))
    if n85 == 3 and n86 == 4:
        n999 = 1.6 * (n84 - 273.15) + 6
        print('O resultado é: {}{} ºm{}'.format('\033[1;32m', n999, '\033[m'))
    if n85 == 4 and n86 == 1:
        n996 = (n84 - 6)/1.6
        print('O resultado é: {}{} ºc{}'.format('\033[1;32m', n996, '\033[m'))
    if n85 == 4 and n86 == 2:
        d = (n84 - 6)/1.6
        n995 = (d - 32)/1.8
        print('O resultado é: {}{} ºf{}'.format('\033[1;32m', n995, '\033[m'))
    if n85 == 4 and n86 == 3:
        e = (n84 - 6)/1.6
        n994 = e + 273.15
        print('O resultado é: {}{} ºM{}'.format('\033[1;32m', n994, '\033[m'))

# CONVERSOR DE VOLUME

if n42 == 6:
    n94 = float(input('Coloque o número que deseja converter: '))
    print('''[ 1 ] US GALÕES
[ 2 ] LITROS
[ 3 ] MILILÍTROS
[ 4 ] CENTÍMETROS CÚBICOS
[ 5 ] METROS CÚBICOS''')
    n95 = int(input('CONVERTER: '))
    print('''[ 1 ] US GALÕES
[ 2 ] LITROS
[ 3 ] MILILITROS
[ 4 ] CENTÍMETROS CÚBICOS
[ 5 ] METROS CÚBICOS''')
    n96 = int(input('PARA: '))
    if n95 > 5 or n96 > 5 or n95 == n96:
        print('METEU ESSA DOIDÃO???')
    if n95 == 1 and n96 == 2:
        n97 = n94 * 3.7854
        print('O resultado é: {}{} l{}'.format('\033[1;32m', n97, '\033[m'))
    if n95 == 1 and n96 == 3:
        n98 = n94 * 3785.41
        print('O resultado é: {}{} ml{}'.format('\033[1;32m', n98, '\033[m'))
    if n95 == 1 and n96 == 4:
        n99 = n94 * 3785.41
        print('O resultado é: {}{} cm³{}'.format('\033[1;32m', n99, '\033[m'))
    if n95 == 1 and n96 == 5:
        n100 = n94 * 0.0038
        print('O resultado é: {}{} m³{}'.format('\033[1;32m', n100, '\033[m'))
    if n95 == 2 and n96 == 1:
        n101 = n94 * 0.2642
        print('O resultado é: {}{} gal{}'.format('\033[1;32m', n101, '\033[m'))
    if n95 == 2 and n96 == 3:
        n102 = n94 * 1000
        print('O resultado é: {}{} ml{}'.format('\033[1;32m', n102, '\033[m'))
    if n95 == 2 and n96 == 4:
        n103 = n94 * 1000
        print('O resultado é: {}{} cm³{}'.format('\033[1;32m', n103, '\033[m'))
    if n95 == 2 and n96 == 5:
        n104 = n94 * 0.001
        print('O resultado é: {}{} m³{}'.format('\033[1;32m', n104, '\033[m'))
    if n95 == 3 and n96 == 1:
        n105 = n94 * 0.000264
        print('O resultado é: {}{} gal{}'.format('\033[1;32m', n105, '\033[m'))
    if n95 == 3 and n96 == 2:
        n106 = n94 * 0.001
        print('O resultado é: {}{} l{}'.format('\033[1;32m', n106, '\033[m'))
    if n95 == 3 and n96 == 4:
        n107 = n94
        print('O resultado é: {}{} cm³{}'.format('\033[1;32m', n107, '\033[m'))
    if n95 == 3 and n96 == 5:
        n108 = n94 * 0.000001
        print('O resultado é: {}{} m³{}'.format('\033[1;32m', n108, '\033[m'))
    if n95 == 4 and n96 == 1:
        n109 = n94 * 0.000264
        print('O resultado é: {}{} gal{}'.format('\033[1;32m', n109, '\033[m'))
    if n95 == 4 and n96 == 2:
        n110 = n94 * 0.001
        print('O resultado é: {}{} l{}'.format('\033[1;32m', n110, '\033[m'))
    if n95 == 4 and n96 == 3:
        n111 = n94
        print('O resultado é: {}{} ml{}'.format('\033[1;32m', n111, '\033[m'))
    if n95 == 4 and n96 == 5:
        n112 = n94 * 0.000001
        print('O resultado é: {}{} m³{}'.format('\033[1;32m', n112, '\033[m'))
    if n95 == 5 and n96 == 1:
        n113 = n94 * 264.17
        print('O resultado é: {}{} gal{}'.format('\033[1;32m', n113, '\033[m'))
    if n95 == 5 and n96 == 2:
        n114 = n94 * 1000
        print('O resultado é: {}{} l{}'.format('\033[1;32m', n114, '\033[m'))
    if n95 == 5 and n96 == 3:
        n115 = n94 * 1000000
        print('O resultado é: {}{} ml{}'.format('\033[1;32m', n115, '\033[m'))
    if n95 == 5 and n96 == 4:
        n116 = n94 * 1000000
        print('O resultado é: {}{} cm³{}'.format('\033[1;32m', n116, '\033[m'))

# CONVERSOR DE MASSA

if n42 == 7:
    n117 = float(input('Coloque o número que deseja coverter: '))
    print('''[ 1 ] MILIGRAMA
[ 2 ] DECIGRAMA
[ 3 ] GRAMA
[ 4 ] DECAGRAMA
[ 5 ] QUILOGRAMA
[ 6 ] LIBRAS''')
    n118 = int(input('CONVERTER: '))
    print('''[ 1 ] MILIGRAMA
[ 2 ] DECIGRAMA
[ 3 ] GRAMA
[ 4 ] DECAGRAMA
[ 5 ] QUILOGRAMA
[ 6 ] LIBRAS''')
    n119 = int(input('PARA: '))
    if n118 > 6 or n119 > 6 or n118 == n119:
        print('METEU ESSA DOIDÃO???')
    if n118 == 1 and n119 == 2:
        n120 = n117 / 10 / 10
        print('O resultado é: {}{} dg{}'.format('\033[1;32m', n120, '\033[m'))
    if n118 == 1 and n119 == 3:
        n121 = n117 / 10 / 10 / 10
        print('O resultado é: {}{} g{}'.format('\033[1;32m', n121, '\033[m'))
    if n118 == 1 and n119 == 4:
        n122 = n117 / 10 / 10 / 10 / 10
        print('O resultado é: {}{} dag{}'.format('\033[1;32m', n122, '\033[m'))
    if n118 == 1 and n119 == 5:
        n123 = n117 / 10 / 10 / 10 / 10 / 10 / 10
        print('O resultado é: {}{} kg{}'.format('\033[1;32m', n123, '\033[m'))
    if n118 == 1 and n119 == 6:
        n124 = n117 * 0.0000022046
        print('O resultado é: {}{} lb{}'.format('\033[1;32m', n124, '\033[m'))
    if n118 == 2 and n119 == 1:
        n125 = n117 * 10 * 10
        print('O resultado é: {}{} mg{}'.format('\033[1;32m', n125, '\033[m'))
    if n118 == 2 and n119 == 3:
        n126 = n117 / 10
        print('O resultado é: {}{} g{}'.format('\033[1;32m', n126, '\033[m'))
    if n118 == 2 and n119 == 4:
        n127 = n117 / 10 / 10
        print('O resultado é: {}{} dag{}'.format('\033[1;32m', n127, '\033[m'))
    if n118 == 2 and n119 == 5:
        n128 = n117 / 10 / 10 / 10 / 10
        print('O resultado é: {}{} kg{}'.format('\033[1;32m', n128, '\033[m'))
    if n118 == 2 and n119 == 6:
        n129 = n117 / 10 / 10 / 10 / 10 * 2.2046
        print('O resultado é: {}{} lb{}'.format('\033[1;32m', n129, '\033[m'))
    if n118 == 3 and n119 == 1:
        n130 = n117 * 10 * 10 * 10
        print('O resultado é: {}{} mg{}'.format('\033[1;32m', n130, '\033[m'))
    if n118 == 3 and n119 == 2:
        n131 = n117 * 10
        print('O resultado é: {}{} dg{}'.format('\033[1;32m', n131, '\033[m'))
    if n118 == 3 and n119 == 4:
        n132 = n117 / 10
        print('O resultado é: {}{} dag{}'.format('\033[1;32m', n132, '\033[m'))
    if n118 == 3 and n119 == 5:
        n133 = n117 / 10 / 10 / 10
        print('O resultado é: {}{} kg{}'.format('\033[1;32m', n133, '\033[m'))
    if n118 == 3 and n119 == 6:
        n134 = n117 / 10 / 10 / 10 * 2.2046
        print('O resultado é: {}{} lb{}'.format('\033[1;32m', n134, '\033[m'))
    if n118 == 4 and n119 == 1:
        n135 = n117 * 10 * 10 * 10 * 10
        print('O resultado é: {}{} mg{}'.format('\033[1;32m', n135, '\033[m'))
    if n118 == 4 and n119 == 2:
        n136 = n117 * 10 * 10
        print('O resultado é: {}{} dg{}'.format('\033[1;32m', n136, '\033[m'))
    if n118 == 4 and n119 == 3:
        n137 = n117 * 10
        print('O resultado é: {}{} g{}'.format('\033[1;32m', n137, '\033[m'))
    if n118 == 4 and n119 == 5:
        n138 = n117 / 10 / 10
        print('O resultado é: {}{} kg{}'.format('\033[1;32m', n138, '\033[m'))
    if n118 == 4 and n119 == 6:
        n139 = n117 / 10 / 10 * 2.2046
        print('O resultado é: {}{} lb{}'.format('\033[1;32m', n139, '\033[m'))
    if n118 == 5 and n119 == 1:
        n140 = n117 * 10 * 10 * 10 * 10 * 10 * 10
        print('O resultado é: {}{} mg{}'.format('\033[1;32m', n140, '\033[m'))
    if n118 == 5 and n119 == 2:
        n141 = n117 * 10 * 10 * 10 * 10
        print('O resultado é: {}{} dg{}'.format('\033[1;32m', n141, '\033[m'))
    if n118 == 5 and n119 == 3:
        n142 = n117 * 10 * 10 * 10
        print('O resultado é: {}{} g{}'.format('\033[1;32m', n142, '\033[m'))
    if n118 == 5 and n119 == 4:
        n143 = n117 * 10 * 10
        print('O resultado é: {}{} dag{}'.format('\033[1;32m', n143, '\033[m'))
    if n118 == 5 and n119 == 6:
        n144 = n117 * 2.2046
        print('O resultado é: {}{} lb{}'.format('\033[1;32m', n144, '\033[m'))
    if n118 == 6 and n119 == 1:
        n145 = n117 * 453592.37
        print('O resultado é: {}{} mg{}'.format('\033[1;32m', n145, '\033[m'))
    if n118 == 6 and n119 == 2:
        n146 = n117 * 453592.37 * 10 * 10
        print('O resultado é: {}{} dg{}'.format('\033[1;32m', n146, '\033[m'))
    if n118 == 6 and n119 == 3:
        n147 = n117 * 453592.37 * 10 * 10 * 10
        print('O resultado é: {}{} g{}'.format('\033[1;32m', n147, '\033[m'))
    if n118 == 6 and n119 == 4:
        n148 = n117 * 453592.37 * 10 * 10 * 10 * 10
        print('O resultado é: {}{} dag{}'.format('\033[1;32m', n148, '\033[m'))
    if n118 == 6 and n119 == 5:
        n149 = n117 * 0.4536
        print('O resultado é: {}{} kg{}'.format('\033[1;32m', n149, '\033[m'))

# CONVERSOR DE VELOCIDADE

if n42 == 8:
    n150 = float(input('Coloque o número que deseja converter '))
    print('''[ 1 ] METROS POR SEGUNDO
[ 2 ] METROS POR HORA
[ 3 ] QUILOMETROS POR SEGUNDO
[ 4 ] QUILOMETROS POR HORA
[ 5 ] MILHAS POR SEGUNDO
[ 6 ] MILHAS POR HORA''')
    n151 = int(input('COVERTER: '))
    print('''[ 1 ] METROS POR SEGUNDO
[ 2 ] METROS POR HORA
[ 3 ] QUILOMETROS POR SEGUNDO
[ 4 ] QUILOMETROS POR HORA
[ 5 ] MILHAS POR SEGUNDO
[ 6 ] MILHAS POR HORA''')
    n152 = int(input('PARA: '))
    if n151 > 6 or n152 > 6 or n151 == n152:
        print('METEU ESSA DOIDÃO???')
    if n151 == 1 and n152 == 2:
        n153 = n150 * 3600
        print('O resultado é: {}{} m/h{}'.format('\033[1;32m', n153, '\033[m'))
    if n151 == 1 and n152 == 3:
        n154 = n150 * 0.001
        print('O resultado é: {}{} km/s{}'.format('\033[1;32m', n154, '\033[m'))
    if n151 == 1 and n152 == 4:
        n155 = n150 * 3.6
        print('O resultado é: {}{} km/h{}'.format('\033[1;32m', n155, '\033[m'))
    if n151 == 1 and n152 == 5:
        n156 = n150 * 0.0006213712
        print('O resultado é: {}{} mi/s{}'.format('\033[1;32m', n156, '\033[m'))
    if n151 == 1 and n152 == 6:
        n157 = n150 * 2.2369362921
        print('O resultado é: {}{} mi/h{}'.format('\033[1;32m', n157, '\033[m'))
    if n151 == 2 and n152 == 1:
        n158 = n150 / 3600
        print('O resultado é: {}{} m/s{}'.format('\033[1;32m', n158, '\033[m'))
    if n151 == 2 and n152 == 3:
        n159 = n150 * 2.77777778e-7
        print('O resultado é: {}{} km/s{}'.format('\033[1;32m', n159, '\033[m'))
    if n151 == 2 and n152 == 4:
        n160 = n150 * 0.001
        print('O resultado é: {}{} km/h{}'.format('\033[1;32m', n160, '\033[m'))
    if n151 == 2 and n152 == 5:
        n161 = n150 * 1.72603109e-7
        print('O resultado é: {}{} mi/s{}'.format('\033[1;32m', n161, '\033[m'))
    if n151 == 2 and n152 == 6:
        n162 = n150 * 0.0006213712
        print('O resultado é: {}{} mi/h{}'.format('\033[1;32m', n162, '\033[m'))
    if n151 == 3 and n152 == 1:
        n163 = n150 * 1000
        print('O resultado é: {}{} m/s{}'.format('\033[1;32m', n163, '\033[m'))
    if n151 == 3 and n152 == 2:
        n164 = n150 * 3600000
        print('O resultado é: {}{} m/h{}'.format('\033[1;32m', n164, '\033[m'))
    if n151 == 3 and n152 == 4:
        n165 = n150 * 3600
        print('O resultado é: {}{} km/h{}'.format('\033[1;32m', n165, '\033[m'))
    if n151 == 3 and n152 == 5:
        n166 = n150 * 0.6213711922
        print('O resultado é: {}{} mi/s{}'.format('\033[1;32m', n166, '\033[m'))
    if n151 == 3 and n152 == 6:
        n167 = n150 * 2236.9362920544
        print('O resultado é: {}{} mi/h{}'.format('\033[1;32m', n167, '\033[m'))
    if n151 == 4 and n152 == 1:
        n168 = n150 / 3.6
        print('O resultado é: {}{} m/s{}'.format('\033[1;32m', n168, '\033[m'))
    if n151 == 4 and n152 == 2:
        n169 = n150 * 1000
        print('O resultado é: {}{} m/h{}'.format('\033[1;32m', n169, '\033[m'))
    if n151 == 4 and n152 == 3:
        n170 = n150 * 0.0002777778
        print('O resultado é: {}{} km/s{}'.format('\033[1;32m', n170, '\033[m'))
    if n151 == 4 and n152 == 5:
        n171 = n150 * 0.0001726031
        print('O resultado é: {}{} mi/s{}'.format('\033[1;32m', n171, '\033[m'))
    if n151 == 4 and n152 == 6:
        n172 = n150 * 0.6213711922
        print('O resultado é: {}{} mi/h{}'.format('\033[1;32m', n172, '\033[m'))
    if n151 == 5 and n152 == 1:
        n173 = n150 * 1609.344
        print('O resultado é: {}{} m/s{}'.format('\033[1;32m', n173, '\033[m'))
    if n151 == 5 and n152 == 2:
        n174 = n150 * 5793638.4
        print('O resultado é: {}{} m/h{}'.format('\033[1;32m', n174, '\033[m'))
    if n151 == 5 and n152 == 3:
        n175 = n150 * 1.609344
        print('O resultado é: {}{} km/s{}'.format('\033[1;32m', n175, '\033[m'))
    if n151 == 5 and n152 == 4:
        n176 = n150 * 5793.6384
        print('O resultado é: {}{} km/h{}'.format('\033[1;32m', n176, '\033[m'))
    if n151 == 5 and n152 == 6:
        n177 = n150 * 3600
        print('O resultado é: {}{} mi/h{}'.format('\033[1;32m', n177, '\033[m'))
    if n151 == 6 and n152 == 1:
        n178 = n150 * 0.44704
        print('O resultado é: {}{} m/s{}'.format('\033[1;32m', n178, '\033[m'))
    if n151 == 6 and n152 == 2:
        n179 = n150 * 1609.344
        print('O resultado é: {}{} m/h{}'.format('\033[1;32m', n179, '\033[m'))
    if n151 == 6 and n152 == 3:
        n180 = n150 * 0.00044704
        print('O resultado é: {}{} km/s{}'.format('\033[1;32m', n180, '\033[m'))
    if n151 == 6 and n152 == 4:
        n181 = n150 * 1.609344
        print('O resultado é: {}{} km/h{}'.format('\033[1;32m', n181, '\033[m'))
    if n151 == 6 and n152 == 5:
        n182 = n150 * 0.0002777778
        print('O resultado é: {}{} mi/s{}'.format('\033[1;32m', n182, '\033[m'))

# CONVERSOR DE TEMPO

if n42 == 9:
    n183 = float(input('Coloque o número que deseja converter: '))
    print('''[ 1 ] MILISSEGUNDOS
[ 2 ] SEGUNDOS
[ 3 ] MINUTOS
[ 4 ] HORAS
[ 5 ] DIAS
[ 6 ] SEMANAS
[ 7 ] MESES
[ 8 ] ANOS''')
    n184 = int(input('CONVERTER: '))
    print('''[ 1 ] MILISSEGUNDOS
[ 2 ] SEGUNDOS
[ 3 ] MINUTOS
[ 4 ] HORAS
[ 5 ] DIAS
[ 6 ] SEMANAS
[ 7 ] MESES
[ 8 ] ANOS''')
    n185 = int(input('PARA: '))
    if n184 > 8 or n185 > 8 or n184 == n185:
        print('METEU ESSA DOIDÃO???')
    if n184 == 1 and n185 == 2:
        n186 = n183 * 0.001
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n186, '\033[m'))
    if n184 == 1 and n185 == 3:
        n187 = n183 * 0.0000166667
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n187, '\033[m'))
    if n184 == 1 and n185 == 4:
        n188 = n183 * 2.77777778e-7
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n188, '\033[m'))
    if n184 == 1 and n185 == 5:
        n189 = n183 * 1.15740741e-8
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n189, '\033[m'))
    if n184 == 1 and n185 == 6:
        n190 = n183 * 1.65343915e-9
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n190, '\033[m'))
    if n184 == 1 and n185 == 7:
        n191 = n183 * 1.15740741e-8 * 30
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n191, '\033[m'))
    if n184 == 1 and n185 == 8:
        n192 = n183 * 1.15740741e-8 * 365
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n192, '\033[m'))
    if n184 == 2 and n185 == 1:
        n193 = n183 * 1000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n193, '\033[m'))
    if n184 == 2 and n185 == 3:
        n194 = n183 * 0.0166666667
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n194, '\033[m'))
    if n184 == 2 and n185 == 4:
        n195 = n183 * 0.0002777778
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n195, '\033[m'))
    if n184 == 2 and n185 == 5:
        n196 = n183 * 0.0000115741
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n196, '\033[m'))
    if n184 == 2 and n185 == 6:
        n197 = n183 * 0.0000016534
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n197, '\033[m'))
    if n184 == 2 and n185 == 7:
        n198 = n183 * 0.0000115741 * 30
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n198, '\033[m'))
    if n184 == 2 and n184 == 8:
        n199 = n183 * 0.0000115741 * 365
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n199, '\033[m'))
    if n184 == 3 and n185 == 1:
        n200 = n183 * 60000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n200, '\033[m'))
    if n184 == 3 and n185 == 2:
        n201 = n183 * 60
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n201, '\033[m'))
    if n184 == 3 and n185 == 4:
        n202 = n183 / 60
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n202, '\033[m'))
    if n184 == 3 and n185 == 5:
        n203 = n183 / 1440
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n203, '\033[m'))
    if n184 == 3 and n185 == 6:
        n204 = n183 / 10080
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n204, '\033[m'))
    if n184 == 3 and n185 == 7:
        n205 = n183 * 0.0006944444 * 30
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n205, '\033[m'))
    if n184 == 3 and n185 == 8:
        n206 = n183 * 0.0006944444 * 365
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n206, '\033[m'))
    if n184 == 4 and n185 == 1:
        n207 = n183 * 3600000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n207, '\033[m'))
    if n184 == 4 and n185 == 2:
        n208 = n183 * 3600
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n208, '\033[m'))
    if n184 == 4 and n185 == 3:
        n209 = n183 * 60
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n209, '\033[m'))
    if n184 == 4 and n185 == 5:
        n210 = n183 / 24
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n210, '\033[m'))
    if n184 == 4 and n185 == 6:
        n211 = n183 / 168
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n211, '\033[m'))
    if n184 == 4 and n185 == 7:
        n212 = n183 * 0.0416666667 * 30
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n212, '\033[m'))
    if n184 == 4 and n185 == 8:
        n213 = n183 * 0.0416666667 * 365
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n213, '\033[m'))
    if n184 == 5 and n185 == 1:
        n214 = n183 * 86400000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n214, '\033[m'))
    if n184 == 5 and n185 == 2:
        n215 = n183 * 86400
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n215, '\033[m'))
    if n184 == 5 and n185 == 3:
        n216 = n183 * 1440
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n216, '\033[m'))
    if n184 == 5 and n185 == 4:
        n217 = n183 * 24
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n217, '\033[m'))
    if n184 == 5 and n185 == 6:
        n218 = n183 / 7
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n218, '\033[m'))
    if n184 == 5 and n185 == 7:
        n219 = n183 / 30
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n219, '\033[m'))
    if n184 == 5 and n185 == 8:
        n220 = n183 / 365
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n220, '\033[m'))
    if n184 == 6 and n185 == 1:
        n221 = n183 * 604800000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n221, '\033[m'))
    if n184 == 6 and n185 == 2:
        n222 = n183 * 604800
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n222, '\033[m'))
    if n184 == 6 and n185 == 3:
        n223 = n183 * 10080
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n223, '\033[m'))
    if n184 == 6 and n185 == 4:
        n224 = n183 * 168
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n224, '\033[m'))
    if n184 == 6 and n185 == 5:
        n225 = n183 * 7
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n225, '\033[m'))
    if n184 == 6 and n185 == 7:
        n226 = n183 / 4
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n226, '\033[m'))
    if n184 == 6 and n185 == 8:
        n227 = n183 / 4 / 12
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n227, '\033[m'))
    if n184 == 7 and n185 == 1:
        n228 = n183 * 2629800000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n228, '\033[m'))
    if n184 == 7 and n185 == 2:
        n229 = n183 * 2629800
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n229, '\033[m'))
    if n184 == 7 and n185 == 3:
        n230 = n183 * 43830
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n230, '\033[m'))
    if n184 == 7 and n185 == 4:
        n231 = n183 * 730.5
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n231, '\033[m'))
    if n184 == 7 and n185 == 5:
        n232 = n183 * 30
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n232, '\033[m'))
    if n184 == 7 and n185 == 6:
        n233 = n183 * 4
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n233, '\033[m'))
    if n184 == 7 and n185 == 8:
        n234 = n183 / 12
        print('O resultado é: {}{} yr{}'.format('\033[1;32m', n234, '\033[m'))
    if n184 == 8 and n185 == 1:
        n235 = n183 * 31557600000
        print('O resultado é: {}{} ms{}'.format('\033[1;32m', n235, '\033[m'))
    if n184 == 8 and n185 == 2:
        n236 = n183 * 31557600
        print('O resultado é: {}{} s{}'.format('\033[1;32m', n236, '\033[m'))
    if n184 == 8 and n185 == 3:
        n237 = n183 * 525960
        print('O resultado é: {}{} min{}'.format('\033[1;32m', n237, '\033[m'))
    if n184 == 8 and n185 == 4:
        n238 = n183 * 8766
        print('O resultado é: {}{} hr{}'.format('\033[1;32m', n238, '\033[m'))
    if n184 == 8 and n185 == 5:
        n239 = n183 * 365
        print('O resultado é: {}{} d{}'.format('\033[1;32m', n239, '\033[m'))
    if n184 == 8 and n185 == 6:
        n240 = n183 * 52.1786
        print('O resultado é: {}{} wk{}'.format('\033[1;32m', n240, '\033[m'))
    if n184 == 8 and n185 == 7:
        n241 = n183 * 12
        print('O resultado é: {}{} mth{}'.format('\033[1;32m', n241, '\033[m'))

#SEQUENCIA DE FIBONACCI

if n42 == 10:
    print('━' * 24)
    print('\033[1;3;34m SEQUENCIA DE FIBONACCI\033[m')
    print('━' * 24)
    n242 = int(input('Quantos termos vc quer mostrar? '))
    n243 = 0
    n244 = 1
    print('{} \033[1;34m->\033[m {}'.format(n243, n244), end='')
    n245 = 3
    while n245 <= n242:
        n246 = n243 + n244
        print(' \033[1;34m->\033[m {}'.format(n246), end='')
        n243 = n244
        n244 = n246
        n245 += 1
    print('\033[1;3;31m FIM\033[m')

#CAUCULO FATORIAL

if n42 == 11:
    from math import factorial
    n247 = int(input('Digite um número para calcular seu fatorial: '))
    n248 = factorial(n247)
    n249 = n247
    print('Calculando fatorial de {}'.format(n247))
    print('━━━━━━━━━━━━━━━━')
    print('Este é o calculo passo a passo:')
    while n249 > 0:
        print('{}'.format(n249), end='')
        print(' x ' if n249 > 1 else ' = \033[1;31m{}\033[m'.format(n248), end='')
        n249 -= 1
    print()

#PROGRESSÃO ARITMÉTICA

if n42 == 12:
    print('TERMOS DE UMA PROGRESSÃO ARITMÉTICA ')
    n250 = int(input('Primeiro Termo: '))
    n251 = int(input('Razão: '))
    n252 = n250
    n253 = 1
    n254 = 10
    n255 = 0
    while n254 != 0:
        n255 += n254
        while n253 <= n255:
            n252 += n251
            print('{} \033[1;34m-\033[m '.format(n252), end='')
            n253 += 1
        print('PAUSA')
        n254 = int(input('Mais quantos termos vc quer mostrar? '))
    print('Apareceram \033[1;31m{}\033[m termos em sua tela'.format(n253 - 1))

print('made by:\033[1;34m 𝙀𝙣𝙯𝙤 𝙙𝙚 𝙇𝙪𝙘𝙘𝙖\033[m ')