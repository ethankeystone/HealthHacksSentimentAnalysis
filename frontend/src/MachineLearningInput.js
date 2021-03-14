import React, {Component} from 'react';
import "./Main.css"

export default class MachineLearningInput extends Component {
  constructor(props) {
    super(props)
    let possibleQuestions = ["How are you feeling today?",
      "Tell us about your day.",
      "How have you been recently?",
      "Tell us how you're feeling.",
    ]
    this.state = {
    input:"Type here...",
    response: "",
    currentQuestion: possibleQuestions[Math.round(Math.random() * 4)]      
    }
    console.log(possibleQuestions[0])
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
        console.log(response)
        let a = Math.round(response["suicidal"][0][0])
        let b = Math.round(response["sad"][0][0])
        console.log(a)
        console.log(b)
        if ((a == 0 && b == 1) || (a == 1 && b == 0)) {
          let quotes =
          ["At the end of the day, remind yourself that you did the best you could today, and that is good enough",
          
          "\"Some changes look negative on the surface but you will soon realize that space is being created in your life for something new to emerge.\" - Eckhart Tolle",
          
          "Everything is going to be okay in the end. If it's not okay, it's not the end."]

          this.setState({response: quotes[Math.round(Math.random() * quotes.length)]}); 
        }
        else if (a == 1 && b == 1) {
          this.setState({response: "It's Ok, we all struggle with life somtimes. Just know that there's always people willing to help. Call 800-273-8255 <3"}); 
        } else {
          this.setState({response: "Just keep winning at life and being you!"}); 
        }
       
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
             <h1>{this.state.currentQuestion}</h1> 
             <textarea class="submissionfield" type="text" name="data" value={this.state.input} onChange={this.handleChange}/>
             <div>
              <button class="button" onClick={this.handleSubmit}>Submit</button>
             </div>
             <div class="text">{this.state.response}</div>
      </div>
    );
  }

}
