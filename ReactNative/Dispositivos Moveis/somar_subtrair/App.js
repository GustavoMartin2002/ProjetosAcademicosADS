import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

function TextContainer(props){
  return(
    <Text style={styles.textContainer}> {props.title}</Text>
  );
}

export default function App() {
  const [number, setNumber] = useState(0);

  function somar(){
    return setNumber(number + 1);
  }

  function subtrair(){
    return setNumber(number - 1);
  }

  return (
    <View style={styles.container}>
      <StatusBar style='light'></StatusBar>

      <Text style={styles.titulo}>UseState</Text>
      <TextContainer title="Aperte no botão para adicionar a contagem."/>
            
      <TouchableOpacity onPress={somar} style={styles.button}>
        <Text style={styles.textButton}>SOMAR</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={subtrair} style={styles.button}>
        <Text style={styles.textButton}>SUBTRAIR</Text>
      </TouchableOpacity>

      <Text style={styles.numberResult}>{number}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },

  titulo:{
    color:'blue',
    fontSize:50,
    textAlign:'center'
  },

  textContainer:{
    color: 'white',
    fontSize: 18,
    textAlign: 'center',
  },

  button:{
    marginTop: 15,
    backgroundColor:'white',
    color: 'black',
    padding: "10",
    borderRadius: 10,
    paddingHorizontal:25,
    paddingVertical:10,
  },

  textButton:{
    fontSize:20,
    fontWeight:"900",
  },

  numberResult:{
    color:'white',
    fontSize: 50,
    marginTop: 15,
    textAlign:'center',
  },
});
