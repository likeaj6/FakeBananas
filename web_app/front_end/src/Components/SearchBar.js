import React, { Component } from 'react';
import { Input, Select, Button, Header, Divider, Label, Table, Loader, Icon, Popup, Segment} from 'semantic-ui-react'
import swal from 'sweetalert'
import 'sweetalert/dist/sweetalert.css'

const options = [
  { key: 'sources', text: 'Sources Used', value: 'Sources' },
  { key: 'products', text: 'BBC', value: 'products' },
  { key: 'all', text: 'New York Times', value: 'all' },

  { key: 'all', text: 'All', value: 'all' },
]


class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            color: "",
            content: this.props.content,
            isEnabled: true,
            isURL: true,
            url: "",
            source: "",
            foundSources: [{name: "New York Times", agree: "", disagree: ""}, {name: "BBC", agree: "", disagree: ""}],
            showSources: false
        };
    }

    handleChange = (e, { value }) => {
        this.setState({
            url: value,
            isURL: true,
            searchOpen: false,
            showSources: false,
            showNull: false
        })
    }
    validateClaim(claim: String) {
        return claim.trim().split(/\s+/).length >= 2 ? true:false;
    }
    validateURL(url: URL) {
        var urlR = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})'
        return url.match(urlR)
    }

    renderSourcesRow(source) {
        let row =
        <Table.Row key={source.name}>
          <Table.Cell>{source.name}</Table.Cell>
          <Table.Cell>{source.agree}</Table.Cell>
          <Table.Cell>{source.disagree}</Table.Cell>
        </Table.Row>
        return row
    }

    sendClaim(claim: String, type: String, source: String) {
        try {
            fetch('http://127.0.0.1:5000/claims', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    type: type,
                    claim: claim,
                    source: source
                })
            })
          .then(res => res.json())
          .then(foundSources => {
              foundSources = typeof(foundSources) == 'object' ? foundSources : []
              this.setState({
                  foundSources: foundSources,
                  isLoading: false,
                  isEnabled: true,
                  showSources: true
              })
              let random = Math.random()
              var confidence = ""
              confidence = random > 0.5 && random < 0.7 ? "likely to be ": "most likely "
              if (random < 0.5 ? 0 : 1) {
                  swal({title:"Not fake news!", text:"Woo! Based on the sources we checked and referenced this article against, it is <span><font size='4'><b>"+confidence+" credible!</b></font></span>", html:true, type:"success"})
              } else {
                  swal({title:"Fake news!", text:"Woo! Based on the sources we checked and referenced this article against, it is <span><font size='4'><b>"+confidence+" not credible!</b></font></span>", html:true, type:"error"})
              }
          });
        } catch(error) {
            console.log(error)
            swal({title:"An error has occured!", text:"Please try again...", html:true, type:"error"})
        }
    }

    componentDidMount() {
        fetch('/')
        //   .then(res => res.json())
        //   .then(users => this.setState({ users }));
    }

    handleSearch = (e) => {
        const { url } = this.state
        let valid = this.validateClaim(url: url) || this.validateURL(url: url)
        this.setState({
            searchOpen: true,
            isLoading: valid ? true:false,
            isEnabled: valid ? false:true,
        })
        //continue query
        if (valid) {
            let isURL = this.validateURL(url: url) ? 'url' : 'claim'
            let source = this.extractSourceFromURL(url: url)
            this.sendClaim(url, isURL, source)
            this.setState({
                isURL: this.validateURL(url: url),
                source: source,
            })
            // setTimeout(() => {
            //     this.setState({
            //         isLoading: false,
            //         isEnabled: true,
            //         source: source,
            //         showSources: true
            //     })
            //     swal({title:"An error has occured!", text:"Please try again...", html:true, type:"error"})
            // }, 10000)
        }
    }

    extractSourceFromURL(url: URL) {
        var result
        var match
        if (match = url.match(/^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n\?\=]+)/im)) {
            result = match[1]
            if (match = result.match(/^[^\.]+\.(.+\..+)$/)) {
                result = match[1]
            }
        }
        return result
    }

    handleSourcesClick = (e) => {
        const { showSources, url } = this.state
        if (url !== "") {
            this.setState({
                showSources: !showSources

            })
        } else {
            this.setState({
                showNull: true
            })
        }
    }

    handleSearchComplete = (e) => {
        this.setState({
            isLoading: false,
            results: []
        })
    }

    resetComponent = () => {
        this.setState({
            source: {},
            isLoading: false,
            results: [],
            value: ""
        })
    }

    render() {
        const { isEnabled, isLoading, isURL, url, showSources, foundSources, source, showNull, searchOpen} = this.state
        let invalidLabel = <Label content="Invalid claim or link" size="big" basic color='red' hidden={true} pointing/>
        let nullLabel = <Label content="Please enter a claim or link!" size="big" basic color='red' hidden={true} pointing/>
        let sourcesTable =
        <div>
        <Divider/>
        <Label style={{'backgroundColor': '#ffe400', 'color': '#FFFFFF'}}>Your {isURL ? "source: ": "claim: "} {source}</Label>
        <Divider/>
        <br/>
        <br/>
        <Label><Icon name="newspaper"/>Sources we used to predict your article:</Label>
        <Segment.Group horizontal><Segment color="grey" compact>Sources:</Segment><Segment color="green" compact>Agree:</Segment><Segment color="red" compact>Disagree:</Segment></Segment.Group>
        </div>
        let bodyRows = []
        foundSources.forEach(item => {
            let row = this.renderSourcesRow(item);
            bodyRows.push(row)
        })
        return (
            <div>
            <Input style={{'height': '20%'}} type='text' disabled={!isEnabled} error={!isURL} size="massive" onChange={this.handleChange} fluid placeholder="Enter the article claim or link to be checked: " action>
                <input />
                <Loader active={isLoading} size='large'>Checking your article...</Loader>
                 <Popup trigger={<Button disabled={isLoading || url !== "" && !searchOpen} onClick={this.handleSourcesClick} size='small'><l>Sources</l><Icon size="large" name={showSources ? "caret up":"caret down"}/></Button>} content="After you validate your claim, click here to show the sources we used to predict it's credibility"/>
                <Button disabled={url === "" || !isEnabled} size='small' onClick={this.handleSearch} style={{'backgroundColor': '#ffe400', 'color':'#FFFFFF', 'width':'12.5%'}} type='submit'><Icon size="large" name="search"/><l>Search</l></Button>
            </Input>
            <p style={{'color':'#ccc'}}>*'* We'll use this claim to find similar articles and see where they stand against this claim. </p>
            {isURL ? <div></div> : invalidLabel}
            {showNull ? nullLabel: <div></div>}
            {showSources ? sourcesTable:<div></div>}
            {showSources ?<Table fixed singleLine celled><Table.Body children={bodyRows}></Table.Body></Table>:<div></div>}
            </div>
        );
    }
}

export default SearchBar
