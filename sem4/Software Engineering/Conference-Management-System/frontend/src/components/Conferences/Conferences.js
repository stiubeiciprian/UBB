import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import Overdrive from 'react-overdrive';

import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import CardDeck from 'react-bootstrap/CardDeck'
import Spinner from 'react-bootstrap/Spinner'

export default class Conferences extends Component {
    render() {
        return (

            <div className="d-flex flex-column w-75 mt-5 mx-auto">

                <Link to="/createConference" className="text-center mb-5 mx-auto">
                    <Button className="button" style={{ fontWeight: "bold" }}>ADD CONFERENCE</Button>
                </Link>

                <CardDeck>
                    <Query query={CONFERENCES_QUERY}>
                        {({ data, loading }) => {
                            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                <span className="sr-only">Loading...</span>
                            </Spinner>;

                            let conferences = data.conferences.data;
                            return conferences.map(conference => (
                                <Link key={conferences.gid} to={`/conference/${conference.gid}`} className="text-decoration-none w-25" style={{ color: "#000" }}>
                                    <Card bg="light" className="mb-4">
                                        <Card.Header as="h5">{conference.conferenceName}</Card.Header>
                                        <Card.Body>
                                            <Card.Text>
                                                Subject: {conference.subject}
                                                <footer className="blockquote-footer">
                                                    From {conference.startDate} to {conference.endDate}
                                                </footer>
                                            </Card.Text>
                                        </Card.Body>
                                    </Card>
                                </Link>
                            ))
                        }}
                    </Query>
                </CardDeck>
            </div>
        );
    }
}

const CONFERENCES_QUERY = gql`
query allConferences {
    conferences {
      data {
        gid
        conferenceName
        startDate
        endDate
        subject
        nrTickets
      }
    }
  }
`;