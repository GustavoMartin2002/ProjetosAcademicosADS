import {
    StyleSheet,
    Text,
    View,
    SafeAreaView,
    SectionList,
    StatusBar,
  } from 'react-native';
  
  /*
  ATIVIDADE 2
  FAZER UMA LISTA DE TIPOS DE TECNOLOGIAS
  
   
  
  LINGUAGEM PROGRAMAÇÃO
  JAVA
  PYTHON
  REACT
  REACT NATIVE
  
   
  
  BANCO DE DADOS
  MONGODB
  ORACLE
  POSTGRESQL
  
   
  
  INFRAESTRUTURA
  SWITCH
  ROTEADOR
  */
  
  const DATA = [
    {
      titulosecao: 'LINGUAGEM DE PROGRAMAÇÃO',
      data: ['Java', 'Python', 'React', 'React Native'],
    },
    {
      titulosecao: 'BANCO DE DADOS',
      data: ['MongoDB', 'Oracle', 'PostgreSQL'],
    },
    {
      titulosecao: 'INFRAESTRUTURA',
      data: ['Switch', 'Roteador'],
    },
  ];
  
  const CadaItem = ({ dado }) => (
    <View style={styles.item}>
      <Text style={styles.title}>{dado}</Text>
    </View>
  );
  
  const App = () => (
    <SafeAreaView style={styles.container}>
      <SectionList
        sections={DATA}
        renderItem={({ item }) => <CadaItem dado={item} />}
        renderSectionHeader={({ section: { titulosecao } }) => (
          <Text style={styles.header}>{titulosecao}</Text>
        )}
      />
    </SafeAreaView>
  );
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: StatusBar.currentHeight,
      marginHorizontal: 15,
    },
  
    item: {
      backgroundColor: '#B9D9EB',
      padding: 10,
      marginVertical: 10,
    },
  
    header: {
      fontSize: 25,
      backgroundColor: '#fff',
    },
    
    title: {
      fontSize: 20,
    },
  });
  
  export default App;
  