import { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'

class Inputs extends Component {
  state = {
    cep: '',
    logradouro: '',
    localidade: '',
  }

  handleCEP = (text) => {
    this.setState({ cep: text })
  }
  
  handleLogradouro = (text) => {
    this.setState({ logradouro: text })
  }

  handleLocalidade = (text) => {
    this.setState({ localidade: text })
  }

  consultar = async (cep) => {
    if (cep.length !== 8) {
      alert('CEP inválido. Deve conter 8 dígitos.');
      return;
    }

    try {
      const response = await fetch('https://viacep.com.br/ws/'+ cep + '/json/');
      const json = await response.json();

      this.handleLogradouro(json.logradouro);
      this.handleLocalidade(json.localidade);      
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }
  
  render() {
    return (
      <View style = {styles.container}>
        <TextInput style = {styles.input}
          underlineColorAndroid = "transparent"
          placeholder = "Digite o seu CEP:"
          placeholderTextColor = "#black"
          autoCapitalize = "none"
          autoFocus={true}
          keyboardType = 'numeric'
          onChangeText = {this.handleCEP}
        />
        
        <TextInput style = {styles.inputGet}
          underlineColorAndroid = "transparent"
          placeholder = "Rua:"
          placeholderTextColor = "#black"
          autoCapitalize = "none"
          autoFocus={true}
          editable={false}
          value = {this.state.logradouro}
        />
          
        <TextInput style = {styles.inputGet}
          underlineColorAndroid = "transparent"
          placeholder = "Municipio:"
          placeholderTextColor = "#black"
          autoCapitalize = "none"
          autoFocus={true}
          editable={false}
          value = {this.state.localidade}
        />

        <TouchableOpacity
          style = {styles.submitButton}
            onPress = {
              () => this.consultar(this.state.cep)
            }>
          <Text style = {styles.submitButtonText}> Consultar Endereco </Text>
        </TouchableOpacity>
      </View>
    )
  }
}

export default Inputs

const styles = StyleSheet.create({
  container: {
    paddingTop: 20
  },

  input: {
  margin: 15,
  height: 40,
  borderColor: '#000',
  borderWidth: 5,
  paddingLeft: 8.0,
  backgroundColor:"white"
  },

  inputGet: {
  margin: 15,
  height: 40,
  borderColor: '#000',
  borderWidth: 5,
  paddingLeft: 8.0,
  backgroundColor:"grey"
  },

  submitButton: {
    backgroundColor: '#000000',
    padding: 10,
    margin: 15,
    height: 40,
  },
  
  submitButtonText:{
    color: 'white'
  }
});