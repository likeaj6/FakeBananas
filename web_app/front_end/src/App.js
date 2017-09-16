import React, { Component } from 'react';
import logo from './logo.png';

import './App.css';
import {Image, Header, Container, Divider, Table} from 'semantic-ui-react'
import SearchBar from './Components/SearchBar';
import MainMenu from './Components/Menu';

class App extends Component {
    state = {users: []}

    componentDidMount() {
        fetch('/')
        //   .then(res => res.json())
        //   .then(users => this.setState({ users }));
    }

    render() {
        return (
          <div className="App">
            <div className="App-header">
                <Header size="huge" as='h1' className="App-title" inverted>
                <img src={logo} className="App-logo" alt="logo" />
                Fake Bananas
                </Header>
            </div>
                <Divider hidden={true}/>
                <Header>
                Check your facts before you slip on them
                <p>Validate your article claims against our machine learning system to predict its credibility</p>

                </Header>
                <Image/>
                <Divider/>
                <Container className="searchBar" textAlign="center">
                    <SearchBar/>
                </Container>
                <Divider/>

            <Header as='h1'>How does it work?</Header>
          </div>
        );
    }
}

export default App;
