#!/usr/bin/python3
# -*- coding: utf-8 -*-


# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas ] - - - - - - - - - - - - - - #
try:
    import csv
    import cx_Oracle

except Exception as E:
    print(E)


# - - - - - - - - - - - - - - [ Bloco de Conexao com o BD ] - - - - - - - - - - - - - - #

# [ Efetua conexao com o Banco de Dados ]
try:
    # Connecting to the database. The connect string is comprised of 'username/password@host/SID'
    conn = cx_Oracle.connect('<user>/<password>@(DESCRIPTION=(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = <host>)(PORT = <port>)))(CONNECT_DATA=(SID=DBCLIENT)))')

    # Creating cursor to parse query result
    cur = conn.cursor()

except Exception as E:
    print(E)


# - - - - - - - - - - - - - - [ Bloco de Executar Query e Escrever no CSV ] - - - - - - - - - - - - - - #

# [ Efetua query (SELECT) no Banco de Dados ]
try:
    # Executa Query
    cur.execute('SELECT * FROM table ORDER BY column ASC')

    # Abre o CSV
    with open('file.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escreve o Resultado no CSV
        for line in cur:
            csv_writer.writerow([str(line[0]), str(line[1]), str(line[2]), str(line[3])])

except Exception as E:
    print(E)
