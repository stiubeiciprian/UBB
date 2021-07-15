import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import { Mutation } from 'react-apollo';

import '../../styles/conference-style.css';
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form';
export default class AssignSchedule extends Component {

  state = {
    startDate: '',
    endDate: '',
    dropdownValue: '',
  }

  handleChange = event => {
    console.log("event=" + event.target.value);
    console.log("dropdownValue= " + this.state.dropdownValue);
    this.setState({
      dropdownValue: event.target.value
    });
    console.log("dropdownValue= " + this.state.dropdownValue);
    console.log("event=" + event.target.value);
  }

  updateInputStartDate(e) {
    console.log("startDate=" + e.target.value);
    this.setState({
      startDate: e.target.value
    })
  }

  updateInputEndDate(e) {
    console.log("endDate=" + e.target.value);
    this.setState({
      endDate: e.target.value
    })
  }

  updateInputConferenceSection(e) {
    this.setState({
      conferencesection: e.target.value
    })
    console.log("conferencesection=" + e.target.value);
  }

  _confirm = (id) => {
    this.props.history.push(`/myConference/${id}`);
  }

  render() {
    const { match } = this.props;
    console.log("pid=" + match.params.id);
    return (
      <div>
        <Query query={GET_PAPER_QUERY}
          variables={{
            id: match.params.id
          }}>
          {({ data, loading }) => {
            if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
              <span className="sr-only">Loading...</span>
            </Spinner>;
            const { paper } = data.paper;
            this.confId = data.paper.conference.gid;
            return <Card bg="light" className="mb-4 mx-auto w-50 mt-5">
              <Card.Header as="h5">Assign schedule</Card.Header>
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
                <h5>Enter start date: <input type="text"
                  name="startDate" onChange={e => this.updateInputStartDate(e)} /><br /><br /></h5>
                <h5>Enter end date: <input type="text"
                  name="endDate" onChange={e => this.updateInputEndDate(e)} /><br /><br /></h5>
                <h5>Choose a conference section:{' '}
                  <Form.Control as="select" value={this.state.dropdownValue} onChange={this.handleChange}>
                    <Query query={GET_CONFERENCE_SECTIONS_QUERY}>
                      {({ loading, data }) => {
                        if (loading) return "Loading ...";
                        let conferenceSections = data.conferenceSections.data;
                        return conferenceSections.map(conferenceSection => {
                          return conferenceSection.conference.gid === this.confId ?
                            <option key={conferenceSection.sectionName}
                              value={conferenceSection.sectionName}>
                              {conferenceSection.sectionName}
                            </option>
                            : null
                        });
                      }}
                    </Query>
                  </Form.Control></h5>
                <Mutation mutation={ADD_PAPERSCHEDULE_QUERY}
                  variables={{
                    paper: match.params.id,
                    conferencesection: this.state.dropdownValue,
                    startDate: this.state.startDate,
                    endDate: this.state.endDate
                  }}
                  onCompleted={() => this._confirm(data.paper.conference.gid)}>
                  {mutation => <Button className="button" onClick={mutation} style={{ fontWeight: 'bold' }}>SUBMIT</Button>}
                </Mutation>
              </Card.Body>
            </Card>
          }}
        </Query>
      </div>
    )
  }
}

const GET_PAPER_QUERY = gql`
query getPaperById($id: ID!){
    paper(id: $id){
      gid
      user{
        firstName
        lastName
        email
      }
      conference{
          gid
        conferenceName
        subject
      }
      abstract
      paperContent
    }
  }
`;

const ADD_PAPERSCHEDULE_QUERY = gql`
mutation createPaperSchedule($paper: String!, $conferencesection: String!, $startDate: Date!, $endDate: Date!){
    createPaperschedule(input:{
      paper: $paper
      conferenceSectionName: $conferencesection
      startDate: $startDate
      endDate: $endDate
    }){
      errors{
        messages
      }
    }
  }
`;

const GET_CONFERENCE_SECTIONS_QUERY = gql`
query allConferenceSections{
  conferenceSections{
    data{
      gid
      sectionName
      conference{
        gid
        conferenceName
      }
    }
  }
}
`;