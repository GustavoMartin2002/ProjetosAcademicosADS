import { Component } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  StyleSheet,
} from 'react-native';

/*
Façam uma tela de cadastro simulada, onde os serão pedido os dados:
- nome
-telefone
- email
- endereco
- observacoes

onde nome, email, endereco sao obrigatorios
*/

class Inputs extends Component {
  state = {
    nome: '',
    telefone: '',
    email:'',
    endereco:'',
    observacoes:'',
  };

  handleNome = (text) => {
    this.setState({ nome: text });
  };

  handleTelefone = (text) => {
    this.setState({ telefone: text });
  };

  handleEmail = (text) => {
    this.setState({ email: text });
  };

  handleEndereco = (text) => {
    this.setState({ endereco: text })
  };

  handleObservacoes = (text) => {
    this.setState({ observacoes: text });
  };

  cadastrar = (nome, email, endereco) => {
    if(nome == ""){
      alert('O nome deve ser preenchido.');
    }else if(email == ""){
      alert("O email deve ser preenchido.")
    }else if(endereco == ""){
      alert("o Endreço deve ser preenchido.")
    }else{
      alert('Cliente cadastrado com sucesso!');
    }
  }

  render(){
    return (
      <View style={styles.container}>
        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Nome"
          placeholderTextColor="#000"
          autoCapitalize="none"
          autoFocus={true}
          keyboardType="default"
          onChangeText={this.handleNome}
        />

        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Telefone"
          placeholderTextColor="#000"
          autoCapitalize="none"
          keyboardType="numeric"
          onChangeText={this.handleTelefone}
        />

        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Email"
          placeholderTextColor="#000"
          autoCapitalize="none"
          keyboardType="email-address"
          textContentType="emailAddress"
          onChangeText={this.handleEmail}
        />

        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Endereço"
          placeholderTextColor="#000"
          autoCapitalize="none"
          keyboardType="default"
          onChangeText={this.handleEndereco}
        />

        <textarea
          style={styles.inputObservacoes}
          underlineColorAndroid="transparent"
          placeholder="Observações"
          placeholderTextColor="#000"
          autoCapitalize="none"
          keyboardType="default"
          onChangeText={this.handleObservacoes}
        />

        <TouchableOpacity
          style={styles.submitButton}
          onPress={() => this.cadastrar(this.state.nome, this.state.email, this.state.endereco)}>
          <Text style={styles.submitButtonText}> Cadastrar </Text>
        </TouchableOpacity>
      </View>
    );
  }
}
export default Inputs;

const styles = StyleSheet.create({
  container:  {
    flex: 1,
    paddingTop: 25,
    backgroundColor:"grey"
  },

  input: {
    margin: 15,
    height: 40,
    borderColor: '#000',
    borderWidth: 5,
    paddingLeft: 8.0,
    backgroundColor:"white"
  },

  inputObservacoes: {
    fontSize:14,
    margin: 15,
    height: 100,
    borderColor: '#000',
    borderWidth: 5,
    paddingLeft: 8.0,
    backgroundColor:"white"
  },

  submitButton: {
    backgroundColor: '#000',
    padding: 10,
    margin: 15,
    height: 40,
    textAlign: 'center',
  },
  
  submitButtonText: {
    color: 'white',
  },
});
