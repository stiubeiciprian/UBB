import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import Overdrive from 'react-overdrive';

import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'
import '../../styles/conference-style.css';
import AOS from 'aos'

export default class Conference extends Component {
    render() {
        AOS.init();
        const { match } = this.props;
        return (
            console.log(match.params.id),
            <div className="d-flex flex-column">
                <Query
                    query={CONFERENCE_QUERY}
                    variables={{
                        id: match.params.id
                    }}
                >
                    {({ data, loading }) => {
                        if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                            <span className="sr-only">Loading...</span>
                        </Spinner>;
                        const { conference } = data;
                        return <div className="conference-banner">
                            <h5>{conference.startDate} - {conference.endDate}</h5>
                            <h1>{conference.conferenceName}</h1>
                            <h3>Subject: {conference.subject}</h3>
                            <Link to="/addPaper" key={{ x: match.params.id }} to={`/addPaper/${match.params.id}`} className="text-center mb-5">
                                <Button className="button" style={{}}>SUBMIT PAPER</Button>
                            </Link>
                            <Link key={match.params.id} to={`/conferenceSchedule/${match.params.id}`} className="text-center mb-5">
                                <Button className="button" style={{}}>SCHEDULE</Button>
                            </Link>

                            {conference.nrTickets > 0 && <div className="conference-tickets">
                                <h4>Remaining tickets: {conference.nrTickets}</h4>
                                <div>
                                    <h4>Ticket price: {conference.ticketPrice}$
                                        <Link key={{ id: match.params.id }, { y: conference.ticketPrice }} to={`/buyTicket/${match.params.id}`}>
                                            <Button className="buttons" style={{ marginLeft: '1.2em', borderRadius: '2.5em', fontWeight: "bold" }}>BUY TICKET</Button>
                                        </Link>
                                    </h4>
                                </div>
                            </div>}
                            {conference.nrTickets === 0 && <h1 style={{ color: "red" }}>SOLD OUT</h1>}
                        </div>
                    }}
                </Query>
                <h2 className="mt-5 mb-5 mx-auto">CONFERENCE SECTIONS</h2>
                <div className="mx-auto w-75 text-center">
                    <Query query={SECTIONS_QUERY}
                        variables={{
                            id: match.params.id
                        }}>
                        {({ data, loading }) => {
                            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                <span className="sr-only">Loading...</span>
                            </Spinner>;
                            let conferenceSections = data.conferenceSections.data;
                            return conferenceSections.map(conferenceSection => {
                                return conferenceSection.conference.gid === match.params.id ?
                                    <Card bg="light"  data-aos="fade-in" data-aos-duration="1000"><Card.Body data-aos="fade-left" data-aos-duration="10000">
                                        <Card.Text data-aos="fade-left" data-aos-duration="1000">
                                            {conferenceSection.sectionName}
                                        </Card.Text>
                                    </Card.Body>
                                    </Card> 
                                    : null
                                
                            })
                        }}
                    </Query>
                </div>
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

const SECTIONS_QUERY = gql`
query allConferenceSections{
    conferenceSections{
      data{
        gid
        sectionName
        conference{
          gid
        }
      }
    }
  }  
`;