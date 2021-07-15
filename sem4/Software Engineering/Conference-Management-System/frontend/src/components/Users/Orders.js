import React, { Component } from 'react'
import gql from 'graphql-tag';
import { Query } from 'react-apollo';

import Table from 'react-bootstrap/Table'
import Spinner from 'react-bootstrap/Spinner'

export default class Orders extends Component {
  constructor() {
    super();
    this.email = '';
  }

  render() {
    return (
      <div className="w-75 d-flex flex-column ml-auto mr-auto mt-5">
        <h1>Orders</h1>
        <Table responsive striped hover>
          <thead>
            <th>Date</th>
            <th>Conference Name</th>
            <th>Price</th>
          </thead>
          <tbody>
            <Query query={GET_MAIL_QUERY}>
              {({ data, loading }) => {
                if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                  <span className="sr-only">Loading...</span>
                </Spinner>;
                this.email = data.me.email;
                return <Query query={GET_ORDERS_QUERY}
                  variables={{
                    email: this.email
                  }}>
                  {({ data, loading }) => {
                    if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                      <span className="sr-only">Loading...</span>
                    </Spinner>;
                    console.log(data);
                    let orders = data.ordersByEmail.data;
                    console.log(orders);
                    return orders.map(order =>
                      <tr>
                        <td>{order.date}</td>
                        <td>{order.conference.conferenceName}</td>
                        <td>{order.price}</td>
                      </tr>
                    )
                  }}
                </Query>
              }}
            </Query>
          </tbody>
        </Table>
      </div>
    )
  }
}

const GET_MAIL_QUERY = gql`
query getMyMail{
    me{
      email
    }
  }
`;

const GET_ORDERS_QUERY = gql`
query getOrdersByEmail($email: String!) {
    ordersByEmail(email: $email) {
      data {
        gid
        date
        price
        user {
            email
          }
        conference{
            conferenceName
        }
      }
    }
  }
`;