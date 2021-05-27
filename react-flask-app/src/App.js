import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { openDatabase } from 'react-native-sqlite-storage';
import SQLite from 'react-native-sqlite-storage';

function App() {
  const [currentWindiest, setCurrentWindiest] = useState();
  let count;
  count = 0;
  /*
  useEffect(() => {
    fetch('http://127.0.0.1:5000/hello').then(res => res.json()).then(data => {
      console.log(data.result)
      setCurrentWindiest(data.result)
    });
  }, []);
   */

  return (
    <div className="App">
      <header className="App-header">
        <button text="Windiest city" style={{height: '100px', width : '150px'}} onClick={() => {
          if (count % 4 == 0) {
            fetch('http://127.0.0.1:5000/hello').then(res => res.json()).then(data => {
              console.log(data.result)
              setCurrentWindiest(data.result)
              alert("Searching is finished")
            });
          }
          /*
          else {
            var db = SQLite.openDatabase({ name: 'citiesWindSpeed.db', createFromLocation: 1});

            db.transaction((tx) => {
              tx.executeSql('SELECT * FROM windSpeeds WHERE Windiest_City_And_Speed = ' +
                  '(SELECT MAX(Windiest_City_And_Speed) FROM windSpeeds)', "", (tx,result) => {
                  console.log(result);
              });
            })
          }*/

        }}>Windiest city in California</button>

        <p>{currentWindiest}</p>
      </header>
    </div>
  );
}

export default App;