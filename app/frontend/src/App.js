import React, { Component } from "react"
import Board from './components/Board.js'
import Credits from './components/Credits.js'

class App extends Component {
  render() {
    return (
      <div><Board /><Credits /></div>
    )
  }
}

export default App;
