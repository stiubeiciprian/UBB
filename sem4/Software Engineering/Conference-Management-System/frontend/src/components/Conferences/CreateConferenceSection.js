import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import Spinner from 'react-bootstrap/Spinner'
import { Mutation } from 'react-apollo';
import Button from 'react-bootstrap/Button'

export default class CreateConferenceSection extends Component {

  state = {
    sectionName: ''
  }

  updateInput(e) {
    console.log(e.target.value);
    this.setState({
      sectionName: e.target.value
    })
  }

  _confirm = (id) => {
    this.props.history.push(`/myConference/${id}`);
  }

  render() {
    const { match } = this.props;

    return (
      <div className="d-flex flex-column">
        <Query query={CONFERENCE_QUERY}
          variables={{
            id: match.params.id
          }}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;
            const { conference } = data;
            return <div className="conference-banner">
              <h3>Adding a new conference section for this conference</h3>
              <h5>{conference.startDate} - {conference.endDate}</h5>
              <h1>{conference.conferenceName}</h1>
              <h3>Subject: {conference.subject}</h3>
              <h2 className="mt-5 mx-auto">Name of the new conference section:</h2>
        <input className="mx-auto w-50 mt-3" type="text" name="conferenceSection" onChange={e => this.updateInput(e)} /><br /><br />
              <Mutation mutation={ADD_CONFERENCESECTION_QUERY}
                variables={{
                  sectionName: this.state.sectionName,
                  conference: match.params.id
                }}
                onCompleted={() => this._confirm(match.params.id)}>
                {mutation => <Button className="button mx-auto" onClick={mutation} style={{}}>CREATE SECTION</Button>}
              </Mutation>
            </div>
          }}
        </Query>
        
        
      </div>
    )
  }
}

const ADD_CONFERENCESECTION_QUERY = gql`
mutation addConferenceSection($conference: String!, $sectionName: String!){
    createConferenceSection(input:{
      sectionName: $sectionName
      conference: $conference
    }){
      conferenceSection{
        sectionName
        conference{
          conferenceName
        }
      }
    }
  }
  
`;

const CONFERENCE_QUERY = gql`
query getConference($id: ID!) {
    conference(id: $id){
      conferenceName
      startDate
      endDate
      subject
      nrTickets
      ticketPrice
    }
  }
`;