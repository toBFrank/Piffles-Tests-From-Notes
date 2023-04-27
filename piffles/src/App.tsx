import React, {Component} from "react";
import "./App.css";
import Title from "./components/Title";
import Uploader from "./components/Uploader";


class App extends Component {
  render() {
    return (
      <div className="App">
        <Title />
        <Uploader />
      </div>
    )
  }
}

export default App;