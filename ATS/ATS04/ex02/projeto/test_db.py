def test_conexao_db(db_connection):
    conexao = db_connection
    assert conexao == 'Conexão Global Estabelecida'

def test_conexao_db_2(db_connection):
    conexao_2 = db_connection
    assert conexao_2 == 'Conexão Global Estabelecida'