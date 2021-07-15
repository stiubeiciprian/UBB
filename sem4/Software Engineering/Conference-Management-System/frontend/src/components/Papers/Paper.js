import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'

import '../../styles/conference-style.css';
class Paper extends Component {

  render() {
    return (
      <div className="d-flex flex-column w-75 mx-auto mt-5">
        <h1 className="mb-4">My papers</h1>
        <Query query={GET_MAIL}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;
            this.email = data.me.email;
            return <Query query={PAPERS_QUERY}>
              {({ data, loading }) => {
                if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                  <span className="sr-only">Loading...</span>
                </Spinner>;
                this.papers = data.papers.data;
                return this.papers.map(paper => {
                  return paper.user.email === this.email ?
                    <Card bg="light" className="mb-4">
                      <Card.Header as="h5">{paper.title} - {paper.conference.conferenceName}</Card.Header>
                      <Card.Body>
                        <Card.Text>
                          {paper.abstract === true ? <h5>Status: abstract paper submitted</h5> : <h5>Status: full paper submitted</h5>}
                          <Query query={GET_GRADES}
                            variables={{
                              id: paper.gid
                            }}>

                            {({ data, loading }) => {
                              if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                <span className="sr-only">Loading...</span>
                              </Spinner>;
                              console.log(data);
                              this.reviewGrades = data.reviews.data;
                              return this.reviewGrades.map(grade => {
                                return grade.qualifier === "null" ?
                                  <div><h5>Grade: <b>pending</b> from reviewer with email: {grade.user.email}</h5></div>
                                  : <div><h5>Grade: <b>{grade.qualifier}</b> from reviewer with email: {grade.user.email}</h5></div>
                              })
                            }
                            }
                          </Query>
                        </Card.Text>
                      </Card.Body>
                    </Card>
                    : null
                }
                )
              }}
            </Query>
          }}
        </Query>
      </div>
    )
  }
}

export default Paper

const PAPERS_QUERY = gql`
query getPaper{
    papers{
      data{
        gid
        title
        user{
          email
        }
        conference{
          conferenceName
        }
        abstract
        paperContent
      }
    }
  }
`;

const GET_MAIL = gql`
query getMyMail{
    me{
      email
    }
  }
`;

const GET_GRADES = gql`
query getReviewsForPaper($id: ID!){
  reviews(paperId: $id){
    data{
      user{
        email
      }
      qualifier
    }
  }
}
`;