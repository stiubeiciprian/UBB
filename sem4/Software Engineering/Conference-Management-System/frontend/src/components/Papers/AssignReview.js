import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import { Mutation } from 'react-apollo';

import '../../styles/conference-style.css';
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'
export default class AssignReview extends Component {

  state = {
    email: null
  }

  updateInput = e => {
    console.log(e.target.value);
    this.setState({
      email: e.target.value
    })
  }

  _confirm = () => {
    this.props.history.push(`/myConferences`);
  }


  render() {
    const { match } = this.props;
    console.log(match.params.id);
    return (
      <div>
        <Query query={GET_PAPER_QUERY}
          variables={{
            id: match.params.id
          }
          }>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;
            const { paper } = data.paper;
            console.log(data.paper);
            return <div>
              <Card bg="light" className="mb-4 mx-auto w-50 mt-5">
                <Card.Header as="h5">Assign review</Card.Header>
                <Card.Body>
                  <Card.Text>
                    <h3>This paper was uploaded by</h3>
                    <h5>Firstname: {data.paper.user.firstName}</h5>
                    <h5>Lastname: {data.paper.user.lastName}</h5>
                    <h5>Email: {data.paper.user.email}</h5> <br />
                    <h3>This paper was uploaded for the conference</h3>
                    <h5>Conference name: {data.paper.conference.conferenceName}</h5>
                    <h5>Conference subject: {data.paper.conference.subject}</h5>
                  </Card.Text>
                  <h5>
                    <label>
                      Choose reviewer email: {' '}
                      <select value={''} onChange={this.updateInput}>
                        {<option value={' '}>{' '}</option>}
                        <Query query={GET_EMAILS_QUERY}>
                          {({ data, loading }) => {
                            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                              <span className="sr-only">Loading...</span>
                            </Spinner>;
                            let emails = data.users.data;
                            return emails.map(email => {
                              return <option value={email.email} key={email.email}>{email.email}</option>
                            })
                          }}
                        </Query>
                      </select>
                    </label>
                  </h5>
                  <Mutation mutation={ADD_REVIEW_QUERY}
                    variables={{
                      paper: match.params.id,
                      qualifier: "null",
                      userEmail: this.state.email
                    }}
                    onCompleted={() => this._confirm()}>
                    {mutation => <Button className="button" onClick={mutation} style={{}}>SUBMIT</Button>}
                  </Mutation>
                </Card.Body>
              </Card>
            </div>
          }}
        </Query>
      </div>
    )
  }
}

const GET_EMAILS_QUERY = gql`
query getEmail{
  users{
    data{
      email
    }
  }
}
`;

const GET_PAPER_QUERY = gql`
query getPaperById($id: ID!){
    paper(id: $id){
      gid
      title
      user{
        firstName
        lastName
        email
      }
      conference{
        conferenceName
        subject
      }
      abstract
      paperContent
    }
  }
`;

const ADD_REVIEW_QUERY = gql`
mutation addReviewForPaper($qualifier: String!, $paper: String!, $userEmail: String!){
  createReview(input:{
    qualifier: $qualifier
    paper: $paper
    userEmail: $userEmail
  }){
    errors{
      messages
    }
  }
}
`;