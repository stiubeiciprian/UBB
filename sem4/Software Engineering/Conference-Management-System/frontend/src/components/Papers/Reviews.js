import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';

import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'
import Spinner from 'react-bootstrap/Spinner'

export default class Reviews extends Component {

  render() {
    return (
      <div className="w-75 d-flex flex-column ml-auto mr-auto mt-5">
        <h1>To review</h1>
        <Table responsive striped hover>
          <thead>
            <th>Paper Title</th>
            <th>Author</th>
            <th>Conference</th>
            <th>Grade</th>
          </thead>
          <tbody>
          <Query query={GET_MAIL_QUERY}>
            {({ data, loading }) => {
              if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                <span className="sr-only">Loading...</span>
              </Spinner>;
              this.email = data.me.email;
              return <Query query={GET_REVIEWS_QUERY}
                            variables={{
                              email: this.email
                            }}>
                            {({ data, loading }) => {
                              if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                <span className="sr-only">Loading...</span>
                              </Spinner>;
                              let reviews = data.reviews.data;
                              return reviews.map(review => {
                                return review.user.email === this.email ?
                                  <tr>
                                    <td>{review.paper.title}</td>
                                    <td>{review.user.firstName}  {review.user.lastName}</td>
                                    <td>{review.paper.conference.conferenceName}</td>
                                    <td> {review.qualifier === "null" ?
                                      <Link key={review.gid} to={`/review/${review.gid}`} className="text-decoration-none" style={{ color: "#000" }}>
                                          <Button>SUBMIT GRADE</Button>
                                      </Link>
                                      : <span>{review.qualifier}</span>}
                                      </td>
                                  </tr>
                                  : null
                              })

                            }}

                      </Query>
            }}
          </Query></tbody>
        </Table>
      </div>
    )
  }
}

const GET_REVIEWS_QUERY = gql`
query getReviews{
  reviews{
    data{
      gid
      user{
        email
        firstName
        lastName
      }
      paper{
        title
        conference{
          conferenceName
        }
        paperContent
        
      }
      qualifier
    }
  }
}
`;

const GET_MAIL_QUERY = gql`
query getMyMail{
    me{
      email
    }
  }  
`;
