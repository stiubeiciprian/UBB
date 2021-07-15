import React, { Component } from 'react'
import { Link } from 'react-router-dom';

import { Mutation } from 'react-apollo';
import gql from 'graphql-tag';
import { Query } from 'react-apollo';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import Spinner from 'react-bootstrap/Spinner'

export default class Review extends Component {
  state = {
    qualifier: 'Excellent'
  }

  updateInput = e => {
    console.log(e.target.value);
    this.setState({
      qualifier: e.target.value
    })
  }

  _confirm = () => {
    this.props.history.push(`/myReviews`)
  }

  render() {
    const { match } = this.props;
    return (
      <div>
        <Query query={GET_REVIEW_QUERY}
          variables={{
            id: match.params.id
          }}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;

            console.log(match.params.id);
            this.review = data.review;
            console.log(this.review);
            return <div>
              <Card bg="light" className="mb-4 mx-auto w-50 mt-5">
                <Card.Header as="h5">Please confirm your grade submission</Card.Header>
                <Card.Body>
                  <Card.Text>
                    <p>Submitting a grade for: <b>{this.review.paper.title} - {this.review.paper.conference.conferenceName}</b>.</p>
                    <p>Author: <b>{this.review.user.firstName} {this.review.user.lastName}</b></p>
                    <p>Contact: <b>{this.review.user.email}</b></p>
                  </Card.Text>
                  <footer className="d-flex"> {/* Qualifier: <input type="text" name="qualifier" onChange={e => this.updateInput(e)} /><br /><br /> */}
                    <label>Qualifier: {' '}
                    <select value={this.state.qualifier} onChange={this.updateInput}>
                      <option value={'Excellent'}>Excellent</option>
                      <option value={'Very good'}>Very good</option>
                      <option value={'Good'}>Good</option>
                      <option value={'Bad'}>Bad</option>
                      <option value={'Very bad'}>Very bad</option>
                    </select>
                    </label> 
                  <Mutation mutation={UPDATE_REVIEW}
                    variables={{
                      id: match.params.id,
                      qualifier: this.state.qualifier,
                      paper: this.review.paper.gid
                    }}
                    onCompleted={() => this._confirm()}>
                    {mutation => <Button className="ml-auto" onClick={mutation} style={{fontWeight: 'bold', borderRadius: '2.5em'}}>UPDATE</Button>}
                  </Mutation>
                </footer>
                </Card.Body>
               
              </Card>
            </div>
          }}


        </Query>
      </div>
    )
  }
}

const GET_REVIEW_QUERY = gql`
query getReview($id: ID!){
    review(id: $id){
      gid
      user{
        email
        firstName
        lastName
      }
      paper{
        gid
        title
        conference{
          conferenceName
        }
        paperContent
        
      }
      qualifier
    }
  }
`;

const UPDATE_REVIEW = gql`
mutation updateReviewGrade($id: ID!, $qualifier: String!, $paper: String!){
  updateReview(id: $id, input: {
    qualifier: $qualifier
    paper: $paper
  }){
    errors{
      messages
    }
  }
}
`;