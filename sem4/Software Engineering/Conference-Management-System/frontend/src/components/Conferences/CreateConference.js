import React, { Component } from 'react'
import { Mutation } from 'react-apollo';
import gql from 'graphql-tag';
import ConferenceForm from './ConferenceForm';

export default class CreateConference extends Component {
  _confirm = () => {
    this.props.history.push(`/conferences`)
  }

  render() {
    return (
      <Mutation mutation={NEW_CONFERENCE} onCompleted={() => this._confirm()}>
        {createConference => (
          <ConferenceForm onSubmit={createConference} />
        )}
      </Mutation>
    )
  }
}

const NEW_CONFERENCE = gql`
mutation createConference($conferenceName: String!, $startDate: Date!, $endDate: Date!, $subject: String!, $nrTickets: Int!, $ticketPrice: Int!){
    createConference( input:{
      conferenceName: $conferenceName
      startDate: $startDate
      endDate: $endDate
      subject: $subject
      nrTickets: $nrTickets
      ticketPrice: $ticketPrice
    }) {
      conference{
        conferenceName
      }
    }
  } 
`;

