import React from "react";

class DogApp extends React.Component {
  state = {
    nameOfNewDog: "",
    dogs: [],
  };

  handleChange(e) {
    this.setState({
      nameOfNewDog: e.target.value,
    });
  }

  handleAddDogChange() {
    if (!this.state.nameOfNewDog) {
      return;
    }
    this.setState({
      nameOfNewDog: "",
      dogs: [...this.state.dogs, this.state.nameOfNewDog],
    });
  }

  render() {
    return (
      <div>
        <h1>My Dogs</h1>
        <input type="text" value={this.state.nameOfNewDog} placeholder="Enter a dog name." onChange={this.handleChange.bind(this)} name="nameOfNewDog" />
        <ul>
            {this.state.dogs.map((dogs, i) => (
            <Dog key={`${dogs}_${i}`} name={dogs}>
            </Dog>))}
        </ul>
        <button onClick={this.handleAddDogChange.bind(this)}>Add a dog</button>
      </div>
    );
  }
}

class Dog extends React.Component{
    render(){
        return (<li><b>{this.props.name}</b></li>);
    }
}

export default DogApp;
