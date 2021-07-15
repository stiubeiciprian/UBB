import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import { Mutation } from 'react-apollo';
import gql from 'graphql-tag';
import { Query } from 'react-apollo';

import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import Spinner from 'react-bootstrap/Spinner'

export default class BuyTicket extends Component {
  _confirm = () => {
    this.props.history.push(`/conferences`)
  }

  ticketPrice = 0;
  render() {
    const { match } = this.props;
    return (
      <div>
        <Query query={GET_CONFERENCE_DATA_QUERY}
          variables={{
            id: match.params.id
          }}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;

            this.ticketPrice = data.conference.ticketPrice;
            this.conferenceName = data.conference.conferenceName;
            this.startDate = data.conference.startDate;
            this.endDate = data.conference.endDate;
            this.subject = data.conference.subject;

            return <div>
              <Card bg="light" className="mb-4 mx-auto w-50 mt-5">
                <Card.Header as="h5">Please confirm your purchase</Card.Header>
                <Card.Body>
                  <Card.Text>
                    <p>You are going to buy a ticket for <b>{this.conferenceName}</b> conference.</p>
                    <p>Subject:{this.subject}</p>
                    <p>Event period: {this.startDate} to {this.endDate}</p>
                    <p>Price: {this.ticketPrice}$</p>
                  </Card.Text>

                  <Mutation mutation={CREATE_ORDER_QUERY}
                    variables={{
                      id: match.params.id,
                      price: this.ticketPrice
                    }}
                    onCompleted={() => this._confirm()}>
                    {mutation => <Button onClick={mutation} className="button" style={{ backgroundColor: "green", width: 'fit-content', marginBottom: '0.5em' }}>CONFIRM</Button>}
                  </Mutation>

                  <Link to={`/conference/${match.params.id}`} className="text-decoration-none w-25" style={{ color: "#000" }}>
                    <Button className="button" style={{ backgroundColor: "red", marginLeft: '0.5rem', width: 'fit-content', marginBottom: '0.5em' }}>CANCEL</Button>
                  </Link>

                </Card.Body>
              </Card>
            </div>
          }}
        </Query>
      </div>
    )
  }
}

const CREATE_ORDER_QUERY = gql`
mutation createOrder($id: String!, $price: Int!){
  createOrder(input:{
    conference: $id
    price: $price
  }){
    errors{
      messages
    }
  }
}
`;

const GET_CONFERENCE_DATA_QUERY = gql`
query getConferenceData($id: ID!){
  conference(id: $id){
    subject
    endDate
    startDate
    conferenceName
    ticketPrice
  }
}
`;