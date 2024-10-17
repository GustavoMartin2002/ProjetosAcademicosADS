import { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet, keybordType } from 'react-native'

/*
2) Façam um app para um garçom digitar o valor pago em dinheiro e o valor da conta e informar troco se houver.
*/

class Inputs extends Component {
  state = {
    conta: '',
    pago: '',
  }
  
  handleConta = (text) => {
    this.setState({ conta: text })
  }
  
  handlePago = (text) => {
    this.setState({ pago: text })
  }

  subtrair = (conta, pago) => {
    let resultado = Math.abs(parseFloat(conta) - parseFloat(pago))

    if(conta == ''){
      alert("Insira valor no campo 'Valor da Conta'.")
    }else if(pago == ''){
      alert("Insira valor no campo 'Valor Pago'.")
    }else if(conta == 0 || pago == 0){
      alert("Insira valores acima de 0")
    }else if(conta > pago){
      alert("Valor íntegro não pago, valor devedouro: "+ resultado)
    }else if(pago > conta){
      alert("Valor pago, seu troco é de: "+ resultado)
    }else{
      alert("Valor íntegro Pago.")
    }
  }
  
  render() {
    return (
      <View style = {styles.container}>
        <TextInput style = {styles.input}
          underlineColorAndroid = "transparent"
          placeholder = "Valor da Conta:"
          placeholderTextColor = "#000"
          autoCapitalize = "none"
          autoFocus={true}
          keyboardType="numeric"
          onChangeText = {this.handleConta}
        />
  
        <TextInput style = {styles.input}
            underlineColorAndroid = "transparent"
            placeholder = "Valor Pago:"
            placeholderTextColor = "#000"
            autoCapitalize = "none"
            keyboardType="numeric"
            onChangeText = {this.handlePago}
        />

        <TouchableOpacity
          style = {styles.submitButton}
          onPress = {
            () => this.subtrair(this.state.conta, this.state.pago)
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
      backgroundColor: 'orange',
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