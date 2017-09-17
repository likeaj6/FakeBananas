import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';
import {Image, Header, Container, Icon, Divider, Table, Segment, Button} from 'semantic-ui-react'
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
            <Container>

            <Header as='h1'>How does it work?</Header>
            <Segment className="howThisWorks">
            <p>Our fake news detection is based on the concept of stance detection.</p>
            <p> Fake news is tough to identify. Many 'facts' are are highly complex and difficult to check, or exist on a 'continum of truth' or are compound sentences with fact and fiction overlapping. The best way to attack this problem is not through fact checking, but by comparing how reputible sources feel about a claim.</p>
            <Divider/>

            <Icon name="keyboard" size="big"/>
            <Header as="h3">
            1. You input a claim like "The afganistan war was bad for the world" or a link to an article.
            </Header>
            <Divider/>
            <Icon name="newspaper" size="big"/>
            <Header as="h3">
            2. Based on your input, our system will search for related articles through thousands of global and local news sources, like <i>Associated Press</i>, <i>New York Times</i>, <i>BBC</i>.
            </Header>
            <Divider/>
            <Icon name="line graph" size="big"/>
            <Header as="h3">
            3. We analyze these sources in our machine learning algorithm to output their stance on your topic or claim.
            </Header>
            <Divider/>
            <Icon name="database" size="big"/>

            <Header as="h3">
            4. These stances are then run through our Reputability Graph. If lots of reputible sources all agree with your article or claim, then it is probably true!
            </Header>
            <Divider/>
            <Icon name="unordered list" size="big"/>

            <Header as="h3">
            5. Then we cite our sources so you can click through and read more about what that source has to say!
            </Header>
            </Segment>
            </Container>
            <Divider hidden={true}/>
            <Button style={{'backgroundColor': '#ffe400', 'color':'#FFFFFF', 'width':'12.5%'}} size="huge"><Icon name="chevron up"/><a href="" style={{'color': '#FFFFFF'}}>Return to Top</a></Button>
            <Divider hidden={true}/>
          </div>
        );
    }
}

export default App;
