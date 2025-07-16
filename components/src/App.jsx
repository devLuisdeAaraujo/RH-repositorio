import { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function App() {
  const [userList, setuserList] = useState([{}]);
  const [UserNome, setUserNome] = useState('');
  const [UserCPF, setUserCPF] = useState('');
  const [UserEmail, setUserEmail] = useState('');
  const [UserSenha, setUserSenha] = useState('');
  const users = {
    usuario_nome: UserNome,
    usuario_cpf: UserCPF,
    usuario_email: UserEmail,
    usuario_senha: UserSenha
  }
  const CadastroUsuario = () => {
    const id = Date.now();
    axios.post(`http://127.0.0.1:8000/cadastra_usuario/${id}`, users)
      .then((resposta) => {
        setUserNome('');
        setUserCPF('');
        setUserEmail('');
        setUserSenha('');
        alert('Usuário cadastrado com sucesso!');
        setuserList(resposta.data); 
      })
      .catch((err) => console.log('Erro ao inserir jogador', err));
  };

  return (
    <section className="vh-100" style={{ backgroundColor: '#eee' }}>
      <div className="container h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-lg-12 col-xl-11">
            <div className="card text-black" style={{ borderRadius: '40px' }}>
              <div className="card-body p-md-5">
                <div className="row justify-content-center">
                  <div className="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                    <p className="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Cadastre-se</p>
                    <form className="mx-1 mx-md-4">
                      <div className="d-flex flex-row align-items-center mb-4">
                        <i className="fas fa-user fa-lg me-3 fa-fw"></i>
                        <div className="form-outline flex-fill mb-0">
                          <input
                            type="text"
                            className="form-control"
                            value={UserNome}
                            onChange={(e) => setUserNome(e.target.value)}
                          />
                          <label className="form-label">Seu Nome</label>
                        </div>
                      </div>

                      <div className="d-flex flex-row align-items-center mb-4">
                        <i className="fas fa-id-card fa-lg me-3 fa-fw"></i>
                        <div className="form-outline flex-fill mb-0">
                          <input
                            type="number"
                            className="form-control"
                            value={UserCPF}
                            onChange={(e) => setUserCPF(e.target.value)}
                          />
                          <label className="form-label">Seu CPF</label>
                        </div>
                      </div>

                      <div className="d-flex flex-row align-items-center mb-4">
                        <i className="fas fa-envelope fa-lg me-3 fa-fw"></i>
                        <div className="form-outline flex-fill mb-0">
                          <input
                            type="email"
                            className="form-control"
                            value={UserEmail}
                            onChange={(e) => setUserEmail(e.target.value)}
                          />
                          <label className="form-label">Seu E-mail</label>
                        </div>
                      </div>

                      <div className="d-flex flex-row align-items-center mb-4">
                        <i className="fas fa-lock fa-lg me-3 fa-fw"></i>
                        <div className="form-outline flex-fill mb-0">
                          <input
                            type="password"
                            className="form-control"
                            value={UserSenha}
                            onChange={(e) => setUserSenha(e.target.value)}
                          />
                          <label className="form-label">Senha</label>
                        </div>
                      </div>

                      <div className="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                        <button
                          type="button"
                          className="btn btn-primary btn-lg"
                          onClick={CadastroUsuario}
                        >
                          Register
                        </button>
                      </div>
                    </form>
                  </div>
                  <div className="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">
                  
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default App;
