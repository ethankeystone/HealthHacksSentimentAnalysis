import React, {Component} from 'react';


export default class MachineLearningInput extends Component {
  constructor(props) {
    super(props)
    this.state = {
    input:"None",
    response: "None"      
    }
    this.analyze = this.analyze.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  analyze(input) {
    console.log('sent')
    const link =  "http://127.0.0.1:8000/ML/analyze/";
    let data = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.state)
    }
    fetch(link, data)
    .then(response => response.json())  // promise
    .then(response => {
        let a = (response["response"][0][0])
        this.setState({response: a});
       
    }).catch(err => {
    })
  }

  handleChange(event) {
    this.setState({input: event.target.value});
  }

  handleSubmit(event) {
    this.analyze(this.state.input);
    return false
  }

  render() {
    return (
      <div className="Main">     
             <input type="text" name="data" value={this.state.input} onChange={this.handleChange}/>
             <button onClick={this.handleSubmit}>Submit</button>
             <div>{this.state.response}</div>
      </div>
    );
  }

}
