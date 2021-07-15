import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';

import '../../styles/conference-style.css';
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'

export default class ConferenceSchedule extends Component {

  render() {
    const { match } = this.props;
    console.log(match.params.id);
    return (
      <div>
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
              <h5>{conference.startDate} - {conference.endDate}</h5>
              <h1>{conference.conferenceName}</h1>
              <h3>Subject: {conference.subject}</h3>


              {conference.nrTickets > 0 && <div className="conference-tickets">
                <h4>Remaining tickets: {conference.nrTickets}</h4>
                <div>
                  <h4>Ticket price: {conference.ticketPrice}$
                                    </h4>
                </div>
              </div>}

              {conference.nrTickets === 0 && <h1 style={{ color: "red" }}>SOLD OUT</h1>}

            </div>
          }}
        </Query>
        <Query query={GET_CONFERENCE_PAPERSCHEDULE_QUERY}
          variables={{
            id: match.params.id
          }}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;
            console.log(data);
            let schedules = data.paperschedules.data;
            return schedules.map(schedule => {
              return <Card bg="light" className="mb-4"><Card.Body>
                <Card.Text>
                  <h3>Conference section name: {schedule.conferencesection.sectionName}</h3>
                  <h4>Start date: {schedule.startDate}</h4>
                  <h4>End date: {schedule.endDate}</h4>
                  <h3>Paper</h3>
                  <h4>Paper content: {schedule.paper.paperContent}</h4>
                  <h3>Presented by</h3>
                  <h4>Firstname: {schedule.paper.user.firstName}</h4>
                  <h4>Lastname: {schedule.paper.user.lastName}</h4>
                  <h4>Email: {schedule.paper.user.email}</h4>
                </Card.Text>
              </Card.Body>
              </Card>
            })
          }}
        </Query>
      </div>
    )
  }
}

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

const GET_CONFERENCE_PAPERSCHEDULE_QUERY = gql`
query getPaperScheduleForConference($id: ID!){
    paperschedules(conferenceId: $id){
      data{
        gid
        paper{
            user{
                firstName
                lastName
                email
              }
          paperContent
        }
        conferencesection{
          sectionName
          conference{
            gid
            conferenceName
          }
        }
        startDate
        endDate
      }
    }
  }
`;