import React from "react";
import axios from 'axios';
import Button from './components/Buttons/Upload/index';
import Frame from './components/Frames/index';
import './App.css';


class App extends React.Component{

    constructor(props){
        super(props);
        this.state={selectedFile:null}
    }

    onChangeHandler = (event) =>{
        this.setState({selectedFile:event.state.files[0]})
    }
    onClickHandler = (event) =>{
        event.preventDefault(); 
        let formData = new FormData();
        formData.append('file',this.state.selectedFile)
        axios.post("http://localhost:3000/",formData,{})
        .then(result=>
            console.log(result.statusText))    
  }

    render() {
        return (
          <div className="main">
            <div className="Banner">
              <h1>Scan Files</h1>
              <Button value="Upload" OnClickHandler={this.onClickHandler} />
              <Button value="Scan" OnChangeHandler={this.onChangeHandler} />
            </div>
            <div className="ImageView">
              <Frame alt="XXXX" />
              <Button value="Download" onChangeHandler={this.onChangeHandler} />
              <Frame alt="XXXX" />
            </div>
          </div>
        );
    }

} export default App