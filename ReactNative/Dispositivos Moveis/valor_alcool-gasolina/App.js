import { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet, keybordType } from 'react-native'

/*
1) Façam um app para solicitar o valor do alcool e da gasolina. Depois o app vai informar qual é mais vantajoso abastecer
*/

class Inputs extends Component {
  state = {
    alcool: '',
    gasolina: '',
   }
  
  handleAlcool = (text) => {
    this.setState({ alcool: text })
  }
   
  handleGasolina = (text) => {
    this.setState({ gasolina: text })
  }

  dividir = (alcool, gasolina) => {
    let resultado = parseFloat(alcool) / parseFloat(gasolina)

    if(alcool == 0 || gasolina == 0){
      alert("Insira valores acima de 0")
    }else if(resultado <= 0.7){
      alert("É mais vantajoso usar Álcool.")
    }else{
      alert("É mais vantajoso usar Gasolina.")
    }
  }
   
  render() {
    return (
      <View style = {styles.container}>
        <TextInput style = {styles.input}
          underlineColorAndroid = "transparent"
          placeholder = "Valor do Álcool:"
          placeholderTextColor = "#000"
          autoCapitalize = "none"
          autoFocus={true}
          keyboardType="numeric"
          onChangeText = {this.handleAlcool}
        />
                      
        <TextInput style = {styles.input}
            underlineColorAndroid = "transparent"
            placeholder = "Valor da Gasolina:"
            placeholderTextColor = "#000"
            autoCapitalize = "none"
            keyboardType="numeric"
            onChangeText = {this.handleGasolina}
        />
               
            
        <TouchableOpacity
          style = {styles.submitButton}
          onPress = {
            () => this.dividir(this.state.alcool, this.state.gasolina)
          }>
          <Text style = {styles.submitButtonText}> Resultado </Text>
        </TouchableOpacity>
      </View>
    )
  }
}

export default Inputs

const styles = StyleSheet.create({
   container: {
      flex: 1,
      paddingTop: 25,
      backgroundColor: 'gold'
   },

   input: {
      margin: 15,
      height: 40,
      borderColor: '#000',
      borderWidth: 5,
      paddingLeft: 8.0
   },

   submitButton: {
      backgroundColor: '#000',
      padding: 10,
      margin: 15,
      height: 40,
      textAlign:'center'
   },

   submitButtonText:{
      color: 'white'
   }
})