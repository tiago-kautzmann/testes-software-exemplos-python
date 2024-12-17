from myapp.database import conectar_db, buscar_usuario

def test_buscar_usuario():
    conexao = conectar_db()
    usuario = buscar_usuario(conexao, user_id=1)
    assert usuario["nome"] == "João"