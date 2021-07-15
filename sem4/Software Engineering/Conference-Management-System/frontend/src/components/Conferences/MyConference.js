import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';

import '../../styles/conference-style.css';
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'


export default class MyConference extends Component {
    render() {
        const { match } = this.props;
        return (
            console.log(match.params.id),
            <div className="d-flex flex-column">
            
                <Query
                    query = {CONFERENCE_QUERY}
                    
                    variables = {{
                        id: match.params.id
                    }}
                >
                    {({data, loading}) => {
                        if(loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                                <span className="sr-only">Loading...</span>
                                            </Spinner>;
                        const { conference } = data;
                        return <div className="conference-banner">
                            <h5>{conference.startDate} - {conference.endDate}</h5>
                            <h1>{conference.conferenceName}</h1>
                            <h3>Subject: {conference.subject}</h3>
                            
                            <Link key={match.params.id} to={`/addConferenceSection/${match.params.id}`} className="text-center mb-5">
                                <Button className="button" style={{ fontWeight: 'bold', height: '100%' }}>NEW SECTION</Button>
                            </Link> 
                            <Link key={match.params.id} to={`/conferenceSchedule/${match.params.id}`} className="text-center mb-5">
                                <Button className="button" style={{ fontWeight: 'bold' }}>CHECK SCHEDULE</Button>
                            </Link> 

                                {conference.nrTickets > 0 && <div className="conference-tickets">
                                    <h4>Remaining tickets: {conference.nrTickets}</h4>
                                    <div> 
                                        <h4>Ticket price: {conference.ticketPrice}$
                                        </h4>
                                    </div>
                                </div>}
                                
                                {conference.nrTickets === 0 && <h1 style={{color:"red"}}>SOLD OUT</h1>}
                            
                        </div>
                    }}
                </Query>
                <h2 className="mt-5 mb-5 mx-auto">CONFERENCE SECTIONS</h2>
                <div className="w-75 mx-auto text-center">
                    <Query query = {SECTIONS_QUERY}
                        
                    variables = {{
                        id: match.params.id
                    }}>
                    {({data, loading}) => {
                                if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                                        <span className="sr-only">Loading...</span>
                                                    </Spinner>;

                                let conferenceSections = data.conferenceSections.data;
                                return conferenceSections.map(conferenceSection => {
                                    return conferenceSection.conference.gid === match.params.id ? 

                                        <Card bg="light" className="mb-4"><Card.Body>
                                                    <Card.Text>
                                                       {conferenceSection.sectionName}
                                                    </Card.Text>
                                                </Card.Body>
                                        </Card>
                                    :null
                                })
                            }}
                    </Query>
                </div>

                <h2 className="mx-auto mb-5 mt-5">SUBMITTED PAPERS</h2>
                <div className="d-flex flex-row flex-wrap w-75 mx-auto justify-content-center">
                    <Query query={GET_PAPERS_QUERY}>
                    {({data, loading}) => {
                        if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                                                <span className="sr-only">Loading...</span>
                                            </Spinner>;
                        let papers = data.papers.data;
                        return papers.map(paper => {
                            return paper.conference.gid === match.params.id ?
                            <Card bg="light" className="mb-4 w-25 mr-3">
                                <Card.Header><b>{paper.title}</b></Card.Header>
                                <Card.Body>
                                    <Card.Text>
                                        Name: {paper.user.firstName} {paper.user.lastName}
                                        Email: {paper.user.email}
                                        {paper.abstract === true ? <div>Form: abstract</div> : <div>Form: fully submitted</div>}
                                    </Card.Text>
                                    <footer className="d-flex">
                                        <Link id={paper.gid} to={`/assignReview/${paper.gid}`} className="text-decoration-none" style={{color:"#000"}}>
                                                    <Button className="mr-2"  style={{fontWeight: 'bold', borderRadius: '2.5em'}}>ADD REVIEW</Button>
                                        </Link>
                                        <Link id={paper.gid} cid={match.params.id} to={`/assignSchedule/${paper.gid}`} className="text-decoration-none " style={{color:"#000"}}>
                                                    <Button style={{background: "green", fontWeight: 'bold', borderRadius: "2.5em", border: 'none'}}>ACCEPT PAPER</Button>
                                        </Link>
                                    </footer>
                                </Card.Body>
                            </Card>
                            : null 
                        })
                    }
                    }   
                    </Query>
                </div>
            </div>
        )
    }
}

const GET_PAPERS_QUERY = gql`
query getPaperForConference{
    papers{
      data{
        gid
        title
        user{
          firstName
          lastName
          email
        }
        conference{
          gid
          conferenceName
          startDate
          endDate
        }
        abstract
        paperContent
      }
    }
  }
`;

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